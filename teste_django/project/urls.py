
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    print('home')
    return HttpResponse('home')



def blog(request):
    print('salv')
    return HttpResponse('Testeee')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog),
    path("teste/", ),
    path('', home),
]
