from rest_framework.permissions import BasePermission


class UserTypes:
    admin = 1
    trainer = 2
    mentor = 3
    intern = 4
    guest = 5


class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.status.id == UserTypes.intern)


class IsMentor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.status.id == UserTypes.mentor)


class IsTrainer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.status.id == UserTypes.trainer)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.status.id == UserTypes.admin)
