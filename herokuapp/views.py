from django.shortcuts import redirect, render, get_object_or_404
from .models import Alimentos
from .forms import AlimentosForm
def inicio(request):
    alimentos = Alimentos.objects.all()
    context ={
        'alimentos' : alimentos
    }
    return render(request,'herokuapp/inicio.html',context)

# def detail(request, id):
#     detail_alimento = get_object_or_404(Alimentos, pk = id)
#     context = {
#         'detail_alimento' : detail_alimento
#     }
#     return render(request,'cadenarestaurantes/detail.html',context)
    

def crear(request):
    if request.method == "POST":
        alimento_form = AlimentosForm(request.POST)
        if alimento_form.is_valid():
            alimento_form.save()
            return redirect('aplication:inicio')
    else:
        alimento_form = AlimentosForm()
    return render(request,'herokuapp/agregar.html', {'alimento_form': alimento_form} )
