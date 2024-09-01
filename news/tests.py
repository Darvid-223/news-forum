from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='TestCategory')
        Post.objects.create(title='Test Post', content='Just a test', author=user, category=category)


    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.category.name, 'TestCategory')


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='TestCategory')
        post = Post.objects.create(title='Test Post', content='Just a test', author=user, category=category)
        Comment.objects.create(post=post, user=user, content='This is a test comment')


    def test_comment_creation(self):
        comment = Comment.objects.get(content='This is a test comment')
        self.assertEqual(comment.content, 'This is a test comment')
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.user.username, 'testuser')
