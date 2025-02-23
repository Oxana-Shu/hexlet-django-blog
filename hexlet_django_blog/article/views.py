from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .forms import ArticleForm
from django.contrib import messages

from hexlet_django_blog.article.models import Article

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
#    def get(self, request):
#       return redirect(reverse('article', kwargs={'tags' : 'python', 'article_id' : '42'}))


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


#class ArticleCommentsView(View):

#    def get(self, request, *args, **kwargs):
#        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

#        return render( ... )


def index(request, tags=None, article_id=None):
    if tags == None:
        article_id = 42
        tags = 'python'
    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        messages.error(request, "The article was not created.")
        return render(request, 'articles/create.html', {'form': form, 'messages': messages})