from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.views.generic import CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import BlogPost
from .utils import slugfy_title

# Create your views here.


class BlogHomeView(TemplateView):
    template_name = "home.html"


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

            return redirect("blog_list")
        else:
            return render(request, "blog_post.html", {"form": form})


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "blogs"
    ordering = ["created_at"]


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = BlogPost.objects.get(slug=self.kwargs["slug"])
        return context


class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog_update.html"
    # fields = ['title', 'body', 'image']
    success_url = "/list/"


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog_delete.html"
    success_url = "/list/"
