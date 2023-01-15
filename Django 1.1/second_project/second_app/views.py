from django.shortcuts import render
from second_app.models import User
from second_app.forms import NewUserForm
# Create your views here.

def index(request):
    names = User.objects.order_by('first_name')
    my_dict = {'users':names}

    return render(request,'second_app/index.html',context=my_dict)

def users(request):
    form = NewUserForm()
    if(request.method == 'POST'):
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('FORM Invalid')
    return render(request,'second_app/users.html',{'form':form})

