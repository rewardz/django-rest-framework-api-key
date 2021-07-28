from django.urls import re_path
from django.contrib import admin
from tests.views import TestView, TestAPIView


urlpatterns = [

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^test/$', TestView.as_view(), name="test-view"),
    re_path(r'^api/$', TestAPIView.as_view(), name="test-api-view"),

]
