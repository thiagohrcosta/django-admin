from django.shortcuts import render
from .forms import UserForm

def index(request):
  return render(request, 'user/index.html')

def create(request):

  if request.method == 'GET':
    form = UserForm()
   
    context = {
      'form': form, 
    }
    return render(request, 'user/create.html', context=context)

  else:
    form = UserForm(request.POST)
    if form.is_valid():
      print(form)
      form.save()

      context = {
          'form': form,
      }
      
      return render(request, 'user/index.html', context=context)

  # elif request.method == 'POST':
  #   return render(request, 'user/')
