"""
URLs for x_courses.
"""
from django.urls import path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from x_courses.views import get_courses

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="x_courses/base.html")),
    path(
        'hina/', get_courses, name='x_courses_list'
    ),
]
