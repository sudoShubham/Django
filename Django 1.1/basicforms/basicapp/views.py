from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')


def view_form_page(request):
    form = forms.FormName()

    if(request.method == 'POST'):
        form = forms.FormName(request.POST)

        if(form.is_valid()):
            print('Validation Done')
            print(form.cleaned_data)

    return render(request,'basicapp/form_page.html',{'form':form})