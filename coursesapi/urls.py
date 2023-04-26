"""
URLs for coursesapi.
"""
from django.urls import path

from coursesapi.views import get_courses, CourseListAPIView

urlpatterns = [
    path("courses/", get_courses, name="courses"),
    path("courses-list/", CourseListAPIView.as_view(), name="courses_list")
]
