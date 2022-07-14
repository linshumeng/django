from django.urls import path
# from article.views import article_detail, article_list
from . import views

urlpatterns = [    
    path('<article_id>', views.article_detail, name="article_detail"),
    path('', views.article_list, name="article_list"),
]   
