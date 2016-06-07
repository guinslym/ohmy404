from django.conf.urls import url

from .views import WebsitesListView

urlpatterns = [
    url(r'^$', WebsitesListView.as_view(), name='websites-list'),
]
