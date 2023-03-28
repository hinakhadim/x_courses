"""
x_courses Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    ProjectType, PluginURLs
)


class XCoursesConfig(AppConfig):
    """
    Configuration for the x_courses Django application.
    """

    name = 'x_courses'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.APP_NAME: 'x_courses',
                PluginURLs.REGEX: r'^api/x_courses/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
    }
