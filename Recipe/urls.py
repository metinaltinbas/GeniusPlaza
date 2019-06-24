from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeListAPIView,RecipeCreateAPIView,RecipeByUserAPIView,RecipeUpdate,RecipeDelete

urlpatterns = [
    url(r'^RecipeList/$', RecipeListAPIView.as_view()),
    url(r'^RecipeCreate/$',RecipeCreateAPIView.as_view()),
    url(r'^RecipeByUser/$', RecipeByUserAPIView.as_view()),
    url('RecipeUpdate/<int:pk>', RecipeUpdate.as_view()),
    url('RecipeDelete/<int:pk>', RecipeDelete.as_view()),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
