from django.shortcuts import redirect, render
from .models import Producto 
from  .forms import ProductoForm


def index(request):
    return render(request, 'index.html')
def tienda(request):
    return render(request, 'tienda.html')
def preventa(request):
    mercancias=Producto.objects.all()#entrega todos los objetos de la clase Producto
    
  
    return render(request,'preventa.html',context={'datos':mercancias})


def form_producto(request):
    if request.method=='POST':
        
        producto_form =ProductoForm(request.POST,request.FILES)

        if producto_form.is_valid():
            producto_form.save() #save reemplaza al insert en sql
            return redirect('index')
    else:
        producto_form=ProductoForm()
    return render(request,'form_crearproducto.html',{'producto_form':producto_form})

def ver(request):
    productos=Producto.objects.all()

    return render(request,'ver.html',context={'productos':productos})

def form_mod_producto(request,id):
    producto=Producto.objects.get(numeroSerie=id)
    datos={
        'form':ProductoForm(instance=producto)
    }
    if request.method =='POST':
        formulario=ProductoForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('ver')
    return render(request,'form_mod_producto.html',datos)
def form_del_producto(request,id):
    producto=Producto.objects.get(numeroSerie=id)
    producto.delete()
    return redirect('ver')




    

