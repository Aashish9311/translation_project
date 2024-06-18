from django.shortcuts import render

# Create your views here.

from .forms import TranslationForm
from googletrans import Translator

def translate_view(request):
    translation = ''
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            src_lang = form.cleaned_data['src_lang']
            dest_lang = form.cleaned_data['dest_lang']

            translator = Translator()
            try:
                translation = translator.translate(input_text, src=src_lang, dest=dest_lang).text
            except Exception as e:
                translation = f"Error: {e}"
    else:
        form = TranslationForm()

    return render(request, 'translate_app/translate.html', {'form': form, 'translation': translation})
