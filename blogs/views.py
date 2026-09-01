from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from .models import Blog, Category
# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # use get_object_or_404 whaen you want to show 4040
    context = {
        'posts': posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)
