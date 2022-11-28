from rest_framework.viewsets import ModelViewSet
from api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        self.update(request)

    def delete(self, request, pk):
        self.destroy(request)

