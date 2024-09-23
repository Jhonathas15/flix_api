from rest_framework import permissions


class GenresPermissions(permissions.BasePermission):

    def has_permissions(self, request, view):

        if request.method == ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')

        if request.method == ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False
