from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
class HomePageView(TemplateView): 
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 

    template_name = 'pages/about.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Pascual Gómez", 

        })

        return context 

class ContactPageView(TemplateView): 

    template_name = 'pages/contact.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "email": "pascualgomz@email.com",
            "address": "North Street 151",
            "phone_number": "3003003030",

        })

        return context 

class Product: 

    products = [ 

        {"id":"1", "name":"TV", "description":"Best TV", "price":"$100"}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"$1000"}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"$100"}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"$10"},

    ]
 
class ProductIndexView(View): 

    template_name = 'products/index.html' 

    def get(self, request): 

        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 

        return render(request, self.template_name, viewData) 

class ProductShowView(View): 
    template_name = 'products/show.html' 

    def get(self, request, id): 
        try:
            viewData = {} 
            product = Product.products[int(id)-1] 
            viewData["title"] = product["name"] + " - Online Store" 
            viewData["subtitle"] =  product["name"] + " - Product information" 
            viewData["product"] = product 
        
        except:
            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, viewData)
 
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect(reverse('created'))

        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class ProductCreatedPageView(TemplateView): 
    template_name = 'products/created.html'