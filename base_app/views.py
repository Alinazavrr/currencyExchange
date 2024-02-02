from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class homePage(TemplateView):
    template_name = 'baseApp/homePage.html'


