import json
import operator
from functools import reduce
from django.http.response import HttpResponse
from django.core import serializers
from rest_framework.views import APIView
from django.db.models import Q
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

class getToolByName(APIView):
    serializer_class = ToolSerializer
    def get(self, request, name):
        if name != None:
            if "-sharp" in name:
                name = name.replace("-sharp", '#')
            tool = Tool.objects.values().filter(name__exact=name).order_by("-stacks_num")[0]
            tool = json.dumps(tool)
        return HttpResponse(tool, status=200)

class getToolsByName(APIView):
    serializer_class = ToolSerializer
    def get(self, request, name):
        if name != None:
            if "-sharp" in name:
                name = name.replace("-sharp", '#')
            if name == "simosun":
                tools = Tool.objects.order_by('name').values('name').distinct().order_by("-stacks_num")[:12]
                tools = [Tool.objects.filter(name__exact=t["name"]).order_by("-stacks_num")[0] for t in tools]    
            else:
                tools = Tool.objects.filter(name__icontains=name).order_by('name').values('name').distinct().order_by("-stacks_num")[:12]
                tools = [Tool.objects.filter(name__exact=t["name"]).order_by("-stacks_num")[0] for t in tools]
            tools = serializers.serialize('json', tools)
            tools = json.loads(tools)
            for tool in tools:
                tool["fields"]["category"] = Category.objects.get(pk=tool["fields"]["category_id"]).name
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
    queryset = Company.objects.all()[:21]
    serializer_class = CompanySerializer

class getMoreCompanies(APIView):
    serializer_class = CompanySerializer
    def get(self, request, index):
        if index != None:
            companies = Company.objects.all()[index: index + 21]
            companies = [CompanySerializer(company).data for company in companies]
            companies = json.dumps(companies)
        return HttpResponse(companies, status=200)

class getCompanyByName(APIView):
    serializer_class = CompanySerializer
    def get(self, request, name):
        if name != None:
            company = Company.objects.values().get(name__exact=name)
            company = json.dumps(company)
        return HttpResponse(company, status=200)

class getCompaniesByTools(APIView):
    serializer_class = CompanySerializer
    def post(self, request, index ,format=None):
        if index != None:
            userTools = request.data.get("userTools")
            tools = [tool["name"] for tool in userTools]
            companies = Company.objects.filter(reduce(operator.or_, (Q(tools__icontains=tool) for tool in tools)))[index: index + 18]
            companies = serializers.serialize('json', companies)
        return HttpResponse(companies, status=200)

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
