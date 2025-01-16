from rest_framework import permissions


class CarOwnerPermission(permissions.BasePermission):
    """
    Permissão personalizada para restringir o acesso à lista de objetos e objetos individuais
    apenas ao proprietário do carro.
    """

    def has_permission(self, request, view):
        if view.action == 'list':
            # Filtra a queryset para incluir apenas os objetos do usuário autenticado
            if hasattr(view, 'queryset') and view.queryset is not None:
                view.queryset = view.queryset.filter(owner=request.user)
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # Garante que apenas o proprietário pode acessar o objeto
        return obj.owner == request.user
