from rest_framework import permissions

from .permissions import IsStaffEditorPermissions


class StaffEdiorPermissionMixin():
	permissions_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
