from django.contrib import admin
from django.urls import path

from editing.views import IndexView, DictionaryView, EditDictionaryView, export_txt
app_name = 'editing'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('dictionary/', DictionaryView.as_view(), name='dictionary'),
    path('edit/', EditDictionaryView.as_view(), name='edit'),
    path('export_txt/', export_txt, name='export_txt'),
]
