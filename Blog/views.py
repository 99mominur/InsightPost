from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.views.generic import CreateView
from .models import BlogPost
from .utils import slugfy_title
# Create your views here.


class BlogPostView(CreateView):
    form_class = BlogPostForm
    model = BlogPost
    template_name = "blog_post.html"

    def get(self, request):
        form = BlogPostForm()
        return render(request, "blog_post.html", {"form": form})

    def post(self, request):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            return redirect("blog_post")
        else:
            return render(request, "blog_post.html", {"form": form})
