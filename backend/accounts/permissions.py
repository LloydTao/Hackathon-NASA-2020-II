from rest_framework import permissions


class AllowIfRegistrationOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Blocking GET right now for data privacy reasons. Should make it so user can request info about themselves
        if request.method == "GET":
            return False
        if request.user.is_authenticated:
            # Do not allow registration (POST) if logged in
            return request.method != "POST"
        else:
            # If not logged in, only allow registration (POST)
            return request.method == "POST"
