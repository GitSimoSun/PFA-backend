import json
from django.http.response import HttpResponse
from rest_framework.views import APIView
from api.models import Category, Tool, ParentCategory, User, Company
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import CategorySerializer, ToolSerializer, ParentCategorySerializer, CompanySerializer, UserSerializer

# Create your views here.


class ParentCategoryView(generics.ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class getTools(APIView):
    serializer_class = ToolSerializer
    def get(self, request, category):
        if category != None:
            p_id= ParentCategory.objects.get(name=category).id
            cats = Category.objects.filter(parent=p_id)
            c_ids = [cat.id for cat in cats]
            tools = Tool.objects.filter(category_id__in=c_ids).order_by("-stacks_num")[:20]
            tools = [ToolSerializer(tool).data for tool in tools]
            for tool in tools:
                tool["category"] = Category.objects.get(pk=tool["category_id"]).name
            tools = json.dumps(tools)
        return HttpResponse(tools, status=200)

class getMoreTools(APIView):
    serializer_class = ToolSerializer
    def get(self, request, category, index):
        if index != None and category != None:
            p_id = ParentCategory.objects.get(name=category).id
            cats = Category.objects.filter(parent=p_id)
            c_ids = [cat.id for cat in cats]
            tools = Tool.objects.filter(category_id__in=c_ids).order_by("-stacks_num")[index: index + 20]
            tools = [ToolSerializer(tool).data for tool in tools]
            for tool in tools:
                tool["category"] = Category.objects.get(pk=tool["category_id"]).name
            tools = json.dumps(tools)
        return HttpResponse(tools, status=200)

class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()[:25]
    serializer_class = CompanySerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
