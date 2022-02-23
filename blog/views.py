from email import message
from re import template
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Post, Category, Comment
from .forms import CommentForm
from django.contrib import messages

class PostList(ListView):
    template_name = 'blog/blog_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all().order_by('-created')


class BlogCategoryList(ListView):
    template_name = 'blog/blog_category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs.get('pk')
        context['category'] = get_object_or_404(self.model, pk=pk)
        return context


class PostDetail(View):
    template_name = 'blog/blog_detail.html'
    form_class = CommentForm

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        form = self.form_class
        return render(request, self.template_name, {"post": post, "form": form, "comments": comments})

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = self.form_class(request.POST or None)
        if form.is_valid():
            comment = Comment(
            author=form.cleaned_data["author"], body=form.cleaned_data["body"], post=post)
            comment.save()
            comments = Comment.objects.filter(post=post)
            messages.success(request, 'You add a comment.', 'success')
            form = self.form_class
        else:
            messages.error(request, 'an error occurred', 'warning')

        return render(request, self.template_name, {"post": post, "form": form, "comments": comments})
