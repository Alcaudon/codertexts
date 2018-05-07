from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):
    def has_permission(self, request, view):

        #  Puede conectarse cualquiera mediante POST para garantizar el alta de nuevos usuarios en el sistema
        if request.method == 'POST':
            return True

        # Si quieres ver el listado de usuarios completo debes ser superadmin
        if request.method == 'GET' and request.user.is_superuser:
            return True

        # Si queremos recuperar el detalle de un usuario debemos ser o superuser o nosotros mismos
        if request.method == 'GET' and request.user.is_authenticated:
            return True

        # Si queremos actualizar o borrar los datos de un usuario debemos ser superuser o nosotros mismos
        if (request.method == 'PUT' or request.method == 'DELETE') and request.user.is_authenticated:
            return True

        # Para cualquier otro método HTTP devolvemos False
        return False

    def has_object_permission(self, request, view, obj):
        # Si soy administrador o pido los datos de mi propio usuario, entonces puedo verlos
        return request.user == obj or request.user.is_superuser


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsSuperUser(BasePermission):
    message = 'You must be a superuser.'

    def has_permission(self, request, view):
        return request.user.is_superuser
