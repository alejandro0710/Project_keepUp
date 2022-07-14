from django.urls import path
# from . import views
from .views import NewsHome, NewsDetail, CreateNews, UpdateNews, DeleteNews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', NewsHome.as_view(), name="home"),
    path('news/<int:pk>', NewsDetail.as_view(), name="news-detail"),
    path('create', CreateNews.as_view(), name="create_news"),
    path('news/update/<int:pk>', UpdateNews.as_view(), name="update_news"),
    path('news/delete/<int:pk>', DeleteNews.as_view(), name="delete_news"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
