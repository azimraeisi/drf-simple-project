from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import Article, User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAutherOrReadOnly

# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,IsAutherOrReadOnly)

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,IsAutherOrReadOnly)    

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)




