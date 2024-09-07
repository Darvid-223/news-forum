from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, CustomUserCreationForm


# User signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# View for user account settings (requires login)
@login_required
def account_settings(request):
    return render(request, 'news/account_settings.html')


# View to display a list of posts, optionally filtered by category
def post_list(request, category_id=None):
    if category_id:
        posts = Post.objects.filter(category_id=category_id).order_by(
            '-created_at')
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        posts = Post.objects.all().order_by('-created_at')
        selected_category = None

    categories = Category.objects.all()
    return render(request, 'news/post_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': selected_category
    })


# View to display details of a specific post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    return render(request, 'news/post_detail.html',
                  {'post': post, 'form': form})


# View to delete the user's account (requires login)
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect('post_list')
    return render(request, 'news/delete_account.html')


# View to create a new post (requires login)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'news/post_form.html', {'form': form})


# View to edit an existing post (requires login)
@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You are not allowed to edit this post.')
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_form.html', {'form': form})


# View to delete a post (requires login)
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')
    return render(request, 'news/post_confirm_delete.html', {'post': post})


# View to add a comment to a post (requires login)
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'news/post_detail.html', {
        'post': post, 'form': form})


# View to edit an existing comment (requires login)
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'news/edit_comment.html', {'form': form})


# View to delete a comment (requires login)
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', id=post_id)
    return render(request, 'news/delete_comment.html', {'comment': comment})
