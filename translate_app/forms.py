from django import forms
from googletrans import LANGUAGES

LANGUAGE_CHOICES = [(key, value.title()) for key, value in LANGUAGES.items()]

class TranslationForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}), label='Enter Text')
    src_lang = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Input Language')
    dest_lang = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Output Language')
