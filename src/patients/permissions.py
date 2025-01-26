from rest_framework import permissions
from django.utils.translation import gettext_lazy as _


class IsDoctor(permissions.BasePermission):
    message = _('You should be a doctor to see this list')

    def has_permission(self, request, view):
        return request.user.groups.filter(name='doctor').exists()
