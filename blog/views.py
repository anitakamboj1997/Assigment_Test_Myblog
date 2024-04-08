from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, PostTags
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

class BlogPageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
        else:
            search_query = self.request.GET.get('search_query')
            if search_query:
                queryset = queryset.filter(title__icontains=search_query) | queryset.filter(content__icontains=search_query)
        return queryset

@login_required
def create_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        selected_tags = request.POST.get('selected_tags')
        post = form.save(commit=False)
        post.created_by = request.user
        post.tags = str(selected_tags)
        post.save()
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(user=request.user)
        tags = PostTags.objects.all()
    return render(request, 'blog/add_post.html', {'form': form, 'tags': tags})
