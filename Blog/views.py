from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import BlogPostForm, RegistrationForm, UserLoginForm
from django.views.generic import CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = "../login"
    context_object_name = "form"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
            )

            user.set_password(form.cleaned_data["password1"])
            user.is_active = True
            user.save()
            return redirect("../login")

        else:
            return render(request, self.template_name, {"form": form})


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = UserLoginForm
    

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "You have successfully logged in.")
                    return redirect("../")
                else:
                    messages.error(request, "Your account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
        return render(request, "login.html", {"form": form})


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("blog_home")

    def dispatch(self, request):
        logout(request)
        return redirect(self.next_page)


class PasswordUpdateView(UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = "blog_update.html"
    # fields = ['title', 'body', 'image']
    success_url = "/"


class BlogHomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        context = {"user": request.user}
        return render(request, self.template_name, context=context)


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
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()

            return redirect("blog_list")
        else:
            return render(request, "blog_post.html", {"form": form})


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "blogs"
    ordering = ["created_at"]
    
    def get(self, request):
        blogs = BlogPost.objects.filter(user = request.user)
        return render(request, self.template_name, {"blogs": blogs})


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
