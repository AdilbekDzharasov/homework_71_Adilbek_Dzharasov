from django.http import JsonResponse, HttpResponse
from rest_framework.viewsets import ModelViewSet
from api.serializers import PostSerializer
from posts.models import Post


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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

