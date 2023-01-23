from django.shortcuts import render
from .models import MyModel
# Create your views here.

def MyView(request):
    my_model = MyModel.objects.all()
    return render(request, 'mytemplate.html', {'my_model': my_model})