from django.shortcuts import render
from .models import Resources

datas=Resources.objects.all()



def home(request):

    return render(request,'index.html',{'datas':datas})
