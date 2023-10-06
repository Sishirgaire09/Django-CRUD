from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required 
def product_list(request):
  print(request.user)
  products = Product.objects.all()
  context = {'product_list': products}
  return render(request , "table/product_list.html" , context=context)

@login_required 
def table_form(request, id =0):   #her we create and edit the daata from database
  if request.method == "POST": 
      name = request.POST.get("product-name")      
      category_id = request.POST.get("category-select")
      try:
        category = Category.objects.get(id = category_id)
        if id == 0:          
          Product.objects.create(product_name=name, category=category)
        else:
          product = Product.objects.get(id = id)
          product.update(product_name = name, category = category)
          product.save()
      except [Category.DoesNotExist, Product.DoesNotExist] as e:
        print("Exception ayo")
        print(e)
      return HttpResponseRedirect(reverse('table:table-list'))
    
  if request.method == "GET":
    categories = Category.objects.all()
    
    if id == 0:
      return render (request = request , template_name="table/table_form.html", 
                   context={"categories" : categories })
      
    product = Product.objects.get(pk = id)
    return render (request = request , template_name="table/table_form.html", 
                   context={"product" : product,"categories" : categories })

def table_delete(request , id):
  
  product = Product.objects.get(pk = id)
  product.delete()
  
  return render (request = request , template_name="table/table_form.html"     )

