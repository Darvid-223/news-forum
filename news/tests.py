from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from .forms import PostForm


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


class PostListViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        Post.objects.create(title='Test Post', content='Test Content', author=self.user, category=self.category)

    def test_post_list_view_status_code(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'news/post_list.html')

    def test_post_list_view_context(self):
        response = self.client.get(reverse('post_list'))
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), 1)


class PostFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='News')

    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': 'Test Content',
            'category': self.category.id
        })
        self.assertTrue(form.is_valid())

    def test_post_form_missing_title(self):
        form = PostForm(data={
            'title': '',
            'content': 'Test Content',
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())

    def test_post_form_missing_content(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': '',
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())