# from django.urls import path
# from api.views import RecipeCreateView

# urlpatterns = {
#     path('',RecipeCreateView.as_view(), name='recipe')
# }

# urls.py

from django.urls import path
from .views import RecipeCreateView, RecipeUpdateDeleteView, RecipeListDetail

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='create'),
    path('<int:pk>/', RecipeListDetail.as_view(), name='details'),
    path('<int:pk>/', RecipeUpdateDeleteView.as_view(), name='update'),

]