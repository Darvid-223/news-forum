from django.db import models
from django.contrib.auth.models import User

# Model for representing a category of posts
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the category, must be unique
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name  # Display the category name when referenced as a string


# Model for representing a blog post
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Main content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update when the post is modified
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who authored the post
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Link to the category of the post, allows null
    upvotes = models.IntegerField(default=0)  # Number of upvotes for the post
    downvotes = models.IntegerField(default=0)  # Number of downvotes for the post

    def __str__(self):
        return self.title  # Display the post title when referenced as a string


# Model for representing comments on a post
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Link to the post being commented on
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who made the comment
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when the comment is created

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'  # Display a string representation of the comment
