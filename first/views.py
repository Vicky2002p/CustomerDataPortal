from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from service.models import Customer, Service
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def homePage(request):
    # data={
    #     'title':'Landmark Builders'
    # }
    return render(request, "starter.html")

def ActivePage(request):
    return render(request, "index2.html")

def Inactive(request):
    return render(request, "index3.html")



def vivek(request):
    servicesData = Customer.objects.all()[:5]
    data={
        'servicesData':servicesData
    }
    return render(request, "Vivek.html", data)

def saveEnquiry(request):
    print('in view')
    print(request.POST)

    if request.method == "POST":
        id = request.POST.get('id')
        Name = request.POST.get('name')
        Age = request.POST.get('age')
        dob = request.POST.get('dob')
        Address = request.POST.get('address')

        if request.POST.get('id').isnumeric():
            data=Customer(customerID =id,
                            customerName = Name, 
                            customerAge = Age, 
                            customerDob = dob, 
                            customerAddress = Address  )
            data.save()
            messages.success(request, "Message sent." )
            return redirect('/form')
            # return render(request, "form.html", messages.add_message(request, messages.INFO, "Form has been submitted"))
        else:
            return render(request, "form.html", {'error' : True})

def home(request):
    return render(request, "Vivek.html")

def login(request):
    return render(request, "login.html")

def form(request):
    return render(request, "form.html")


def aboutUs(request):
    return HttpResponse("Welcome to my practice")

def slug(request, courseid):
    return HttpResponse(courseid)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
        
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'log.html',{'form':form})