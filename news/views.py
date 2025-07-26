from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView


def start(request):
    data = {
        'title': 'News'
    }
    news = Articles.objects.order_by("-date")
    return render(request, 'news/newsstart.html', {'news': news, 'data': data})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

