from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=250, required=True)
    message = forms.CharField(widget=forms.Textarea)