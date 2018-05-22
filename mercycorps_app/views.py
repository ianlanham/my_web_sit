from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonForm

def home(request):

    return HttpResponse("Hello, MercyCorps app <br> Add Student")

def add_student(request):
    print("add_student called")
    if request.method == 'POST':
        
        form = PersonForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ..
            # redirect to a new URL:
            
            if form.is_duplicate_record() == False:
                print('duplicate record')
            
            return HttpResponseRedirect('/thanks/')

        
    else:
        form = PersonForm()
        
    return render(request, 'mercycorps_app/addstudent.html', {'form': form})