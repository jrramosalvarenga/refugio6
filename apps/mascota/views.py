from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from django.core.urlresolvers import reverse_lazy

from apps.mascota.form import MascotaForm
from apps.mascota.models import Mascota




def index(request):
    context = {'message': 'hello'}
    return render(request, 'mascota/index.html', context)


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
    mascota=Mascota.objects.all()
    contexto={'mascotas':mascota}
    return render(request,'mascota/mascota_list.html',contexto)

def mascota_edit(request,id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form=MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_form.html',{'form':form })

def mascota_delete(request,id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method=='POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return  render(request,'mascota/eliminar_form.html',{'mascota':mascota})


class Mascota_list(ListView):
    model=Mascota
    template_name = 'mascota/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url =   reverse_lazy('mascota:mascota_listar')





