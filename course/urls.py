from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('api/course', course_api, name='course'),
    path('api/course_details/<int:pk>', course_details, name='course_details'),
]
