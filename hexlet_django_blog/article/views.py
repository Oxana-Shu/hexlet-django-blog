from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

class IndexView(View):

    def get(self, request):
        return redirect(reverse('article', kwargs={'tags' : 'python', 'article_id' : '42'}))
    
def index(request, tags=None, article_id=None):
    if tags == None:
        article_id = 42
        tags = 'python'
    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})
