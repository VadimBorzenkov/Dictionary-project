from common.views import TitleMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from editing.models import Dictionary
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from editing.forms import WordCreateForm
from django.http import HttpResponse


class IndexView(TitleMixin, TemplateView):
    template_name = 'editing/index.html'
    title = 'Home page'
    
class DictionaryView(TitleMixin, ListView):
    model = Dictionary
    template_name = 'editing/dictioary.html'
    title = 'Dictionary'
    
class EditDictionaryView(TitleMixin, CreateView):
    model = Dictionary
    template_name = 'editing/edit.html'
    success_url = reverse_lazy('index')
    title = 'Добавление в словарь'
    form_class = WordCreateForm

def export_txt(request):
    response = HttpResponse(content_type='text/plan')
    response['Content-Disposiyion'] = 'attachment; filename="dictionary.txt"'
    
    words = Dictionary.objects.all()
    with open('dictionary.txt', 'w') as file:    
        for word in words:
            file.write(f'{word.english} - {word.russian}\n')
            
    with open('dictionary.txt', 'r') as file:
        response.write('The text file was created successfully')
        
    return response
        