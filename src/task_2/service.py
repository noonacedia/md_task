from collections import defaultdict
import msgspec

from django.core.files.uploadedfile import TemporaryUploadedFile


class GoodsCounter:
    @classmethod
    def count_goods(cls, file: TemporaryUploadedFile) -> dict[str, int]:
        '''Use set to exclude already met ids

        Also we can use multiprocessing (CPU bound task) here to speed up, but there is no need since
        single-process unit is doing pretty well rn (~1.5sec)

        and also we always can move the task to the background using somethingl like Celery
        if we consider fast response to the user here and store result somewhere later
        '''
        parsed_file = msgspec.json.decode(file.read())
        file.close()
        met_ids = set()
        result = defaultdict(int)
        for d in parsed_file:
            if d['id'] not in met_ids:
                met_ids.add(d['id'])
                result[d['category']] += d['price']
        return result
