from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

def lista_posts(request):
    post = Post.objects.all().order_by('-creado')
    return render(request, 'blog/lista_posts.html', {'posts': post})


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.autor = request.user
            new_post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk = pk )
    
    if post.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista de posts')
        
    else:
        form = PostForm(instance=post)
        
    return render(request, 'blog/editar_post.html', {'form': form })

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    
    return render(request, 'blog/eliminar_post.html', {'post': post})