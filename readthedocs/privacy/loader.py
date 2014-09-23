from django.utils.module_loading import import_by_path
from django.conf import settings

# Managers
ProjectManager = import_by_path(getattr(settings, 'PROJECT_MANAGER', 'privacy.backend.ProjectManager'))
VersionManager = import_by_path(getattr(settings, 'VERSION_MANAGER', 'privacy.backend.VersionManager'))

# Permissions
AdminPermission = import_by_path(getattr(settings, 'ADMIN_PERMISSION', 'privacy.backend.AdminPermission'))
