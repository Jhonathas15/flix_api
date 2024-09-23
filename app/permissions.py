from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):

    def has_permissions(self, request, view):
        model_permission = self.__get_model_permission(method=request.method, view=view)

        if not model_permission:
            return False
        return request.user.has_perm(model_permission)

    def __get_model_permission(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = ''
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTION': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
