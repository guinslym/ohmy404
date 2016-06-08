from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from .models import website404

class WebsitesListView(ListView):

    model = website404
    template_name = "websites_list.html"
    ordering = '-created'

    def get_context_data(self, **kwargs):
        context = super(WebsitesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class WebsitesDetailView(DetailView):

    model = website404
    template_name = "websites404_detail.html"

    def get_context_data(self, **kwargs):
        context = super(WebsitesDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
