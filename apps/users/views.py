from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
from operation.models import TableOne,TableTwo

from users.models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class GalleryView(View):
    def get(self,request):
        table1=TableOne.objects.all()
        table2 = TableTwo.objects.all()
        return render(request,'gallery.html',{
            'table_one':table1,
            'table_two':table2
        })


class AboutView(View):
    def get(self,request):
        return render(request,'about.html')


class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')


class ProductsView(View):
    def get(self,request):
        return render(request,'products.html')