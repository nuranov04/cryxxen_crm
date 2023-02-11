from rest_framework.permissions import BasePermission


class UserTypes:
    admin = 1
    trainer = 2
    mentor = 3
    intern = 4
    guest = 5


class IsIntern(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) == UserTypes.intern)
        return False


class IsMentor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) == UserTypes.mentor)
        return False


class IsTrainer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) == UserTypes.trainer)
        return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) == UserTypes.admin)
        return False


class GrTrainer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) <= UserTypes.trainer)
        return False


class GrMentor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) <= UserTypes.mentor)
        return False


class GrInter(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) <= UserTypes.intern)
        return False


class LsInter(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) >= UserTypes.intern)
        return False


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(int(request.user.status) in (
                UserTypes.intern,
                UserTypes.mentor,
                UserTypes.trainer,
                UserTypes.admin,
            ))
        return False
