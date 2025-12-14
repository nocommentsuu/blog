from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import *



def index(request):
    blogs = Blog.objects.all().order_by('-create')

    if request.method == "POST" and request.user.is_authenticated:
        blog_id = request.POST.get("blog_id")
        blog = get_object_or_404(Blog, id=blog_id)
        message = request.POST.get("message")
        parent_id = request.POST.get("parent_id")

        parent_comment = None
        if parent_id:
            parent_comment = Comment.objects.filter(id=parent_id).first()

        Comment.objects.create(
            new=blog,
            user=request.user.username,  # имя автоматически берём из пользователя
            message=message,
            parent=parent_comment
        )
        return redirect("home")  # или redirect("home"), если так у тебя в urls

    return render(request, "index.html", {"blogs": blogs})
from django.shortcuts import render
from .models import Blog


def filter_author(request):
    search_query = request.GET.get("post_name", "")

    if search_query:
        blogs = Blog.objects.filter(title__icontains=search_query).order_by('-create')
    else:
        blogs = Blog.objects.none()  # ничего не показываем, если поле пустое

    context = {
        "blogs": blogs,
        "search_query": search_query,
    }
    return render(request, "filter-author.html", context)
@login_required
def create_post(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        defaults={"name": request.user.username}
    )

    if request.method == "POST":
        Blog.objects.create(
            author=author,
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            image=request.FILES.get("file")  # mp4 / image
        )
        return redirect("home")

    return render(request, "add-post.html")