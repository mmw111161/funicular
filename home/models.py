from django.db import models

from wagtail.models import Page


class HomePage(Page):
    
    templates = "home/home_page.html"
