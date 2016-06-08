from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.utils import timezone

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from .models import website404

class WebsitesListView(ListView):

    model = website404
    template_name = "websites_list.html"
    ordering = '-created'
    paginate_by=2

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

def handler404(request):
    response = render(request, 'page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response
