from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from .forms import PostForm


# Test class for the Post model
class PostModelTest(TestCase):

    # Setup method to create a user and a post before each test
    def setUp(self):
        # Creating a test user
        user = User.objects.create(username='testuser')

        # Creating a test category
        category = Category.objects.create(name='TestCategory')

        # Creating a test post
        Post.objects.create(
            title='Test Post', content='Just a test',
            author=user, category=category
        )

    # Test to check if the post is created correctly
    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')

        # Asserting that the title matches
        self.assertEqual(post.title, 'Test Post')

        # Asserting that the author matches
        self.assertEqual(post.author.username, 'testuser')

        # Asserting that the category matches
        self.assertEqual(post.category.name, 'TestCategory')


# Test class for the Comment model
class CommentModelTest(TestCase):

    # Setup method to create a user, post, and comment before each test
    def setUp(self):
        # Creating a test user
        user = User.objects.create(username='testuser')

        # Creating a test category
        category = Category.objects.create(name='TestCategory')

        # Creating a test post
        post = Post.objects.create(
            title='Test Post', content='Just a test',
            author=user, category=category
        )

        # Creating a test comment
        Comment.objects.create(
            post=post, user=user, content='This is a test comment'
        )

    # Test to check if the comment is created correctly
    def test_comment_creation(self):
        comment = Comment.objects.get(content='This is a test comment')

        # Asserting that the comment content matches
        self.assertEqual(comment.content, 'This is a test comment')

        # Asserting that the comment's post title matches
        self.assertEqual(comment.post.title, 'Test Post')

        # Asserting that the comment's user matches
        self.assertEqual(comment.user.username, 'testuser')


# Test class for the post list view
class PostListViewTests(TestCase):

    # Setup method to create a user, category, and post before each test
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )

        # Creating a test category
        self.category = Category.objects.create(name='Test Category')

        # Creating a test post
        Post.objects.create(
            title='Test Post', content='Test Content',
            author=self.user, category=self.category
        )

    # Test to check the status code of the post list view
    def test_post_list_view_status_code(self):
        response = self.client.get(reverse('post_list'))

        # Asserting that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    # Test to check if the correct template is used
    def test_post_list_view_template(self):
        response = self.client.get(reverse('post_list'))

        # Asserting that the correct template is used
        self.assertTemplateUsed(response, 'news/post_list.html')

    # Test to check if the posts context is passed correctly
    def test_post_list_view_context(self):
        response = self.client.get(reverse('post_list'))

        # Asserting that 'posts' is in the context
        self.assertIn('posts', response.context)

        # Asserting that there is exactly 1 post in the context
        self.assertEqual(len(response.context['posts']), 1)


# Test class for the post form
class PostFormTests(TestCase):

    # Setup method to create a category before each test
    def setUp(self):
        # Creating a test category
        self.category = Category.objects.create(name='News')

    # Test to check if the form is valid with correct data
    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': 'Test Content',
            'category': self.category.id
        })

        # Asserting that the form is valid with correct data
        self.assertTrue(form.is_valid())

    # Test to check if the form is invalid when the title is missing
    def test_post_form_missing_title(self):
        form = PostForm(data={
            'title': '',
            'content': 'Test Content',
            'category': self.category.id
        })

        # Asserting that the form is invalid without a title
        self.assertFalse(form.is_valid())

    # Test to check if the form is invalid when the content is missing
    def test_post_form_missing_content(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': '',
            'category': self.category.id
        })

        # Asserting that the form is invalid without content
        self.assertFalse(form.is_valid())


def test_edit_other_users_post(self):
    # Creating another user
    another_user = User.objects.create(username='anotheruser')

    # Creating a test post
    post = Post.objects.create(
        title='Test Post', content='Just a test', author=another_user
    )

    response = self.client.get(reverse('post_edit', args=[post.id]))

    # Expect redirection to post list or error page
    self.assertEqual(response.status_code, 302)


def test_delete_other_users_post(self):
    # Creating another user
    another_user = User.objects.create(username='anotheruser')

    # Creating a test post
    post = Post.objects.create(
        title='Test Post', content='Just a test', author=another_user
    )

    response = self.client.post(reverse('post_delete', args=[post.id]))

    # Expect redirection to post list or error page
    self.assertEqual(response.status_code, 302)
