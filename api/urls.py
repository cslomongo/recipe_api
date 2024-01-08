# from django.urls import path
# from api.views import RecipeCreateView

# urlpatterns = {
#     path('',RecipeCreateView.as_view(), name='recipe')
# }

# urls.py

from django.urls import path
from .views import RecipeCreateView

urlpatterns = [
    path('', RecipeCreateView.as_view()),
    # Add other URL patterns as needed
]
