from django import forms

"""
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
"""

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, help_text="Enter your comment")

