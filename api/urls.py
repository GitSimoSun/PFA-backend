from django.urls import path
from .views import CategoryView, getMoreTools, ParentCategoryView, CompanyView, getTools, getMoreCompanies, getToolByName, getCompanyByName, getToolsByName, getCompaniesByTools

urlpatterns = [
    path('categories', CategoryView.as_view()),
    path('tools&category=<str:category>&index=<int:index>', getMoreTools.as_view()),
    path('tools&category=<str:category>', getTools.as_view()),
    path('tools&name=<str:name>', getToolByName.as_view()),
    path('tools&namecontain=<str:name>', getToolsByName.as_view()),
    path('parent_categories', ParentCategoryView.as_view()),
    path('companies', CompanyView.as_view()),
    path('companies&index=<int:index>', getMoreCompanies.as_view()),
    path('companies&name=<str:name>', getCompanyByName.as_view()),
    path('post/userTools&index=<int:index>', getCompaniesByTools.as_view()),
]