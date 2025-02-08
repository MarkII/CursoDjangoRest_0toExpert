from rest_framework.permissions import BasePermission
from comentarios.models import Comentarios


class IsOwnerOrReadAndCreationOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            comment_id = view.kwargs['pk']
            get_comment = Comentarios.objects.get(id=comment_id)
            
            user_id = request.user.id
            user_comment_id = get_comment.user_id
            
            check_on = True if user_id == user_comment_id else False
            
            return check_on
        # return super().has_permission(request, view)