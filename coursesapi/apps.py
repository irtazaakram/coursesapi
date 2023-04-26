"""
coursesapi Django application initialization.
"""

from django.apps import AppConfig


class CoursesapiConfig(AppConfig):
    """
    Configuration for the coursesapi Django application.
    """

    name = "coursesapi"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "coursesapi",
                "regex": "^api/coursesapi/",
                "relative_path": "api.urls",
            }
        },
    }
