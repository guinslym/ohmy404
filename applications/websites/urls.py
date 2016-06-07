from django.conf.urls import url

from .views import WebsitesListView, WebsitesDetailView

urlpatterns = [
    url(r'^$', WebsitesListView.as_view(), name='websites-list'),
    url(r'^(?P<slug>[-\w]+)/$', WebsitesDetailView.as_view(), name='websites-detail'),
]
