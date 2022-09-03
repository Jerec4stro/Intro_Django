
from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy



from .forms import PostCreateForm

# Create your views here.


class BlogListView(View):
    def get(self, request, *args, **kargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request,'blog_list.html',context)


class BlogCreateView(View):
    def get(self, request, *args, **kargs):
        form= PostCreateForm()
        context = {
            'form': form
        }
                
        return render(request, "blog_create.html", context)

    def post(self, request, *args, **kargs):
        if request.method=="POST":
            form= PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title,content=content)

                p.save()
            
                return redirect('blog:home')



        context = {
        
        }
                
        return render(request, "blog_create.html", context)

 


class blogDetailView(View):
    def get(self, request, pk, *args, **kwars):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post': post
        }
        return render(request, 'blog_detail.html', context)


class blogUpdateView(UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kargs={'pk':pk})

class blogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url= reverse_lazy('blog:home')