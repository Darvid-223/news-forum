from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from .forms import PostForm

# Test class for the Post model
class PostModelTest(TestCase):

    # Setup method to create a user and a post before each test
    def setUp(self):
        user = User.objects.create(username='testuser')  # Creating a test user
        category = Category.objects.create(name='TestCategory')  # Creating a test category
        Post.objects.create(title='Test Post', content='Just a test', author=user, category=category)  # Creating a test post

    # Test to check if the post is created correctly
    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')  # Asserting that the title matches
        self.assertEqual(post.author.username, 'testuser')  # Asserting that the author matches
        self.assertEqual(post.category.name, 'TestCategory')  # Asserting that the category matches


# Test class for the Comment model
class CommentModelTest(TestCase):

    # Setup method to create a user, post, and comment before each test
    def setUp(self):
        user = User.objects.create(username='testuser')  # Creating a test user
        category = Category.objects.create(name='TestCategory')  # Creating a test category
        post = Post.objects.create(title='Test Post', content='Just a test', author=user, category=category)  # Creating a test post
        Comment.objects.create(post=post, user=user, content='This is a test comment')  # Creating a test comment

    # Test to check if the comment is created correctly
    def test_comment_creation(self):
        comment = Comment.objects.get(content='This is a test comment')
        self.assertEqual(comment.content, 'This is a test comment')  # Asserting that the comment content matches
        self.assertEqual(comment.post.title, 'Test Post')  # Asserting that the comment's post title matches
        self.assertEqual(comment.user.username, 'testuser')  # Asserting that the comment's user matches


# Test class for the post list view
class PostListViewTests(TestCase):

    # Setup method to create a user, category, and post before each test
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')  # Creating a test user
        self.category = Category.objects.create(name='Test Category')  # Creating a test category
        Post.objects.create(title='Test Post', content='Test Content', author=self.user, category=self.category)  # Creating a test post

    # Test to check the status code of the post list view
    def test_post_list_view_status_code(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)  # Asserting that the status code is 200 (OK)

    # Test to check if the correct template is used
    def test_post_list_view_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'news/post_list.html')  # Asserting that the correct template is used

    # Test to check if the posts context is passed correctly
    def test_post_list_view_context(self):
        response = self.client.get(reverse('post_list'))
        self.assertIn('posts', response.context)  # Asserting that 'posts' is in the context
        self.assertEqual(len(response.context['posts']), 1)  # Asserting that there is exactly 1 post in the context


# Test class for the post form
class PostFormTests(TestCase):

    # Setup method to create a category before each test
    def setUp(self):
        self.category = Category.objects.create(name='News')  # Creating a test category

    # Test to check if the form is valid with correct data
    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': 'Test Content',
            'category': self.category.id
        })
        self.assertTrue(form.is_valid())  # Asserting that the form is valid with correct data

    # Test to check if the form is invalid when the title is missing
    def test_post_form_missing_title(self):
        form = PostForm(data={
            'title': '',
            'content': 'Test Content',
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())  # Asserting that the form is invalid without a title

    # Test to check if the form is invalid when the content is missing
    def test_post_form_missing_content(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': '',
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())  # Asserting that the form is invalid without content


def test_edit_other_users_post(self):
    another_user = User.objects.create(username='anotheruser')
    post = Post.objects.create(title='Test Post', content='Just a test', author=another_user)
    
    response = self.client.get(reverse('post_edit', args=[post.id]))
    self.assertEqual(response.status_code, 302)  # Expect redirection to post list or error page

def test_delete_other_users_post(self):
    another_user = User.objects.create(username='anotheruser')
    post = Post.objects.create(title='Test Post', content='Just a test', author=another_user)
    
    response = self.client.post(reverse('post_delete', args=[post.id]))
    self.assertEqual(response.status_code, 302)  # Expect redirection to post list or error page
