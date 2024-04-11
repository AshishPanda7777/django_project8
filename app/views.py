from django.shortcuts import render

# Create your views here.
def send_data(request):
    d={'name':'ASHISH','age':'23'}
    return render(request,'data.html',context=d)