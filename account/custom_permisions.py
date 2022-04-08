from rest_framework.permissions import IsAuthenticated


class IsPatient(IsAuthenticated):
    def has_permission(self, request, view):
        access = super(IsPatient, self).has_permission(request, view)
        if not access:
            return False
        auth = request.auth
        if auth.get('role') == 'patient':
            return True
        return False


class IsDoctor(IsAuthenticated):
    def has_permission(self, request, view):
        if not super(IsDoctor, self).has_permission(request, view):
            return False
        if request.auth.get('role') == 'expert':
            return True
        return False
