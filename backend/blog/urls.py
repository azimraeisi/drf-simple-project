from django.urls import path, include
from .views import Articlelist, ArticleDetail

app_name = "blog"

urlpatterns = [
    path("", Articlelist.as_view(), name="list"),
    path("<int:pk>", ArticleDetail.as_view(), name="list"),



]
