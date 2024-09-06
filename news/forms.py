from django import forms
from .models import Post, Comment, Category

# Form for creating and editing posts
class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Pre-select "News" category as default
        self.fields['category'].initial = Category.objects.get(name="News")

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    # Custom validation for the title field
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long")
        return title

    # Custom validation for the content field
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Content must be at least 5 characters long")
        return content


# Form for creating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Custom validation for the content of the comment
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long")
        return content
