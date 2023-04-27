"""
coursesapi Django application initialization.
"""

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import ProjectType
from edx_django_utils.plugins import PluginURLs


class CoursesapiConfig(AppConfig):
    """
    Configuration for the coursesapi Django application.
    """

    name = "coursesapi"
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: "coursesapi",
                PluginURLs.REGEX: rf"^api/coursesapi/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        }
    }
