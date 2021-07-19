from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    # ModelForm: 모델과 필드를 지정하면 모델폼이 자동으로 생성
    class Meta:
        model = Blog
        # pud_date는 자동 생성이므로 필드에 넣지 않는다.
        fields = ['title', 'body', 'image']

