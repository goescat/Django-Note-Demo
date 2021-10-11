from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(help_text='Enter note title', widget=forms.TextInput(attrs={'placeholder': 'Enter note title', 'class': 'form-control'}))
    content = forms.CharField(help_text='Enter note content', widget=forms.Textarea(attrs={'placeholder': 'Enter note content', 'class': 'form-control'}))