from django.shortcuts import get_object_or_404, render_to_response
from .models import Blog, BlogType

# Create your views here.

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)

def blogs_with_type(request, blogs_with_type):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blogs_with_type)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)

