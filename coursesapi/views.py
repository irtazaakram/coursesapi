from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.content.course_overviews.serializers import CourseOverviewBaseSerializer
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


@api_view(["GET"])
def get_courses(request):
    courses = CourseOverview.objects.all()
    serializer = CourseOverviewBaseSerializer(courses, many=True)
    return Response(serializer.data)


class CourseListAPIView(ListAPIView):
    queryset = (
        CourseOverview.get_all_courses()
        .prefetch_related("modes")
        .select_related("image_set")
    )
    serializer_class = CourseOverviewBaseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["display_name", "language"]
