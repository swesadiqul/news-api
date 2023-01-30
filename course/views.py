from django.shortcuts import render
from .serializers import CourseSerializer
from django.http import JsonResponse, HttpResponse
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import requests
import json
API_KEY = 'ffd12ea1418548eb85f16b1aee8d3d89'

# Create your views here.
@csrf_exempt
def course_api(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def course_details(request, pk):
    try:
        course = Course.objects.get(pk=pk)

    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

    elif request.method == "DELETE":
        course.delete()
        return HttpResponse(status=204)
    


#show data into html template
def index(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    q = request.GET.get('q')

    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif category:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif q:
        url = f"https://newsapi.org/v2/everything?q={q}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f"https://newsapi.org/v2/everything?q=keyword&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'course/index.html', context)

        
