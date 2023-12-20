from django import forms

from editing.models import Dictionary

class WordCreateForm(forms.ModelForm):
    english = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-2',
        'placeholder' : 'Enter english word',
    }))
    russian = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-2',
        'placeholder' : 'Enter russian word',
    }))
    
    class Meta:
        model = Dictionary
        fields = ('english', 'russian',)