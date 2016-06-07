from django.shortcuts import render

from django.views.generic.list import ListView
from django.utils import timezone

from .models import website404

class WebsitesListView(ListView):

    model = website404
    template_name = "websites/websites_list.html"
    ordering = '-created'

    def get_context_data(self, **kwargs):
        context = super(WebsitesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
