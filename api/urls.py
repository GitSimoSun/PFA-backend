from django.urls import path
from .views import CategoryView, getMoreTools, ParentCategoryView, CompanyView, UserView, getTools

urlpatterns = [
    path('categories', CategoryView.as_view()),
    path('tools&category=<str:category>&index=<int:index>', getMoreTools.as_view()),
    path('tools&category=<str:category>', getTools.as_view()),
    path('parent_categories', ParentCategoryView.as_view()),
    path('companies', CompanyView.as_view()),
    path('users', UserView.as_view()),
]