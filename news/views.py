from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


# User signup view
def signup(request):
    if request.method == 'POST':  # Check if the request is a form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Validate the form data
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()  # Display an empty form for GET request
    return render(request, 'registration/signup.html', {'form': form})  # Render the signup form


# View for user account settings (requires login)
@login_required
def account_settings(request):
    return render(request, 'news/account_settings.html')  # Render account settings page


from django.shortcuts import get_object_or_404

# View to display a list of posts, optionally filtered by category
def post_list(request, category_id=None):
    if category_id:
        # Filter posts by the selected category
        posts = Post.objects.filter(category_id=category_id).order_by('-created_at')
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        # Fetch all posts if no category is selected
        posts = Post.objects.all().order_by('-created_at')
        selected_category = None
    
    categories = Category.objects.all()  # Fetch all categories for displaying in the template
    return render(request, 'news/post_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': selected_category
    })



# View to display details of a specific post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Get the post by ID or return 404 if not found
    form = CommentForm()  # Create an empty comment form
    return render(request, 'news/post_detail.html', {'post': post, 'form': form})  # Render post detail page


# View to delete the user's account (requires login)
@login_required
def delete_account(request):
    if request.method == 'POST':  # Check if form submission is a POST request
        user = request.user
        user.delete()  # Delete the current user's account
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('post_list')  # Redirect to post list after account deletion
    return render(request, 'news/delete_account.html')  # Render the delete account page


# View to create a new post (requires login)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')  # Flash message
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'news/post_form.html', {'form': form})


# View to edit an existing post (requires login)
@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check if user is the author or superuser of the post
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You are not allowed to edit this post.')  
        return redirect('post_list')  # Redirect to home 
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')  # Flash message
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_form.html', {'form': form})



@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check if user is the author or superuser of the post
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You are not allowed to delete this post.')  
        return redirect('post_list')  # Redirect to home
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')  # Flash message
        return redirect('post_list')
    return render(request, 'news/post_confirm_delete.html', {'post': post})




# View to add a comment to a post (requires login)
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Get the post by ID
    if request.method == 'POST':
        form = CommentForm(request.POST)  # Create comment form with POST data
        if form.is_valid():  # Validate the form
            comment = form.save(commit=False)
            comment.post = post  # Associate the comment with the post
            comment.user = request.user  # Set the user who made the comment
            comment.save()  # Save the comment
            return redirect('post_detail', id=post.id)  # Redirect to the post's detail page
    else:
        form = CommentForm()  # Display an empty comment form for GET request
    return render(request, 'news/post_detail.html', {'post': post, 'form': form})  # Render the post detail page with the form


# View to edit an existing comment (requires login)
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # Get the comment by ID
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # Create form with POST data and existing comment
        if form.is_valid():  # Validate the form
            form.save()  # Save the updated comment
            return redirect('post_detail', id=comment.post.id)  # Redirect to the post's detail page
    else:
        form = CommentForm(instance=comment)  # Display form with existing comment data for GET request
    return render(request, 'news/edit_comment.html', {'form': form})  # Render the edit comment form


# View to delete a comment (requires login)
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # Get the comment by ID
    if request.method == 'POST':
        post_id = comment.post.id  # Get the associated post ID before deleting the comment
        comment.delete()  # Delete the comment
        return redirect('post_detail', id=post_id)  # Redirect to the post's detail page after deletion
    return render(request, 'news/delete_comment.html', {'comment': comment})  # Render the comment delete confirmation page

