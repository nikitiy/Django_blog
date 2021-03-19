from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView


# Create your views here.


def home(request):
    data = {
        'title': 'First page',
        'article': Blog.objects.all()
    }

    return render(request, 'blog/home.html', data)


class NewsView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'article'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(NewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Новости'
        return ctx


class NewsDetailView(DetailView):
    model = Blog
    template_name = 'blog/blogDetail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = Blog.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
