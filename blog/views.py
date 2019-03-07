from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "hello"
        return context


class BasicBlogView(TemplateView):
    template_name = "blog/base_blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "hello"
        return context
