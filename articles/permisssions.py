from rest_framework.permissions import BasePermission


class ArticlePermissions(BasePermission):
    def has_permission(self, request, view):

        # Si quieres ver listado de artículos o el detalle de un artículo publicado está permitido
        if request.method == 'GET':
            return True

        #  Con Post solo pueden conectarse los usuarios autenticados
        if request.method == 'POST' and request.user.is_authenticated:
            return True

        # Si queremos actualizar o borrar los datos de un artículo debemos ser superuser o nosotros mismos
        if (request.method == 'PUT' or request.method == 'DELETE') and request.user.is_authenticated:
            return True

        # Para cualquier otro método HTTP devolvemos False
        return False

    def has_object_permission(self, request, view, obj):
        # Si soy administrador o pido los datos de mi propio usuario, entonces puedo verlos
        return request.user == obj.id_user or request.user.is_superuser