from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from .models import Article

# Create your views here.
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {}
        context["article_obj"] = article
        return render(request, "article_detail.html", context)
        # return render_to_response("article_detail.html", context)
    except Article.DoesNotExist:
        # return HttpResponse("不存在")
        raise Http404("not exist")
    return HttpResponse("" % (article.title, article.content))

def article_list(request):
    articles = Article.objects.all()
    context = {}
    context["articles"] = articles
    return render(request, "article_list.html", context)
