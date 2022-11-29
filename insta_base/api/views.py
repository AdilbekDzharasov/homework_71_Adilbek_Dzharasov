from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework.viewsets import ModelViewSet
from api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class IsWriteUser(permissions.BasePermission):

    def has_object_permission(self, request, view, post):
        if request.user == post.author:
            return True
        return False


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if (
            handler
            and self.permission_classes_per_method
            and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class PostApiView(PermissionPolicyMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_per_method = {
        'create': [IsAuthenticated],
        'destroy': [IsAuthenticated, IsWriteUser],
        'update': [IsAuthenticated, IsWriteUser],
        'like': [IsAuthenticated],
        'dislike': [IsAuthenticated]
    }

    def get(self, request):
        return self.list(request)

    def post(self, request, pk):
        return self.create(request)

    def put(self, request, pk):
        self.update(request)

    def delete(self, request, pk):
        self.destroy(request)

    def like(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        post.likes.add(author)
        html = "<html><body>like added</body></html>"
        return HttpResponse(html)

    def dislike(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        post.likes.remove(author)
        html = "<html><body>like removed</body></html>"
        return HttpResponse(html)


class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_per_method = {
        'create': [IsAuthenticated, IsWriteUser],
        'destroy': [IsAuthenticated, IsWriteUser],
        'update': [IsAuthenticated, IsWriteUser]
    }

    def get(self, request):
        return self.list(request)

    def post(self, request, pk):
        return self.create(request)

    def put(self, request, pk):
        self.update(request)

    def delete(self, request, pk):
        self.destroy(request)

