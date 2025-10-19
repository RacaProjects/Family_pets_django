from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Mascota
from .forms import MascotaForm
from .filters import MascotaFilter
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Mascota
from .MascotaSerializer import MascotaSerializer
from django.shortcuts import render, get_object_or_404
# Create your views here.

def lista_mascotas(request):
    f = MascotaFilter(request.GET, queryset=Mascota.objects.all())
    mascotas = f.qs  # QuerySet filtrado
    return render(request, 'mascotas/Ver_mascotas.html', {'filter': f, 'mascotas': mascotas})

def crear_mascota(request):
    form = MascotaForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('mascotas:ver_mascotas')
    return render(request, 'mascotas/form.html', {'form': form})

def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, request.FILES or None, instance=mascota)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('mascotas:ver_mascotas')
    return render(request, 'mascotas/form.html', {'form': form})

def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas:ver_mascotas')
    return render(request, 'mascotas/confirm_delete.html', {'mascota': mascota})

def index(request):
    mascotas_destacadas = Mascota.objects.order_by('-fecha_registro')[:6]
    # Para mostrar el tipo de usuario en index:
    es_admin = request.user.is_staff
    es_fundacion = request.user.groups.filter(name="Fundacion").exists()
    return render(request, 'mascotas/index.html', {
        'mascotas_destacadas': mascotas_destacadas,
        'es_admin': es_admin,
        'es_fundacion': es_fundacion
    })


def registro(request):
    return render(request, 'mascotas/registro.html')

def ver_mascotas(request):
    # Lógica de roles
    es_admin = request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
    es_fundacion = request.user.groups.filter(name='Fundacion').exists()

    # Lógica del filtro (igual que lista_mascotas, pero para tu template nuevo)
    filtro = MascotaFilter(request.GET, queryset=Mascota.objects.all())
    mascotas = filtro.qs

    context = {
        'es_admin': es_admin,
        'es_fundacion': es_fundacion,
        'filter': filtro,
        'mascotas': mascotas,
    }
    return render(request, 'mascotas/Ver_Mascotas.html', context)

CODIGO_FUNDACION = "FAMI2025"  # se puede cambiar si es necesario

def registro(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        codigo = request.POST.get('codigo', '')

        # Validar duplicados y contraseñas
        if User.objects.filter(username=username).exists():
            error = "Ese nombre de usuario ya existe."
        elif User.objects.filter(email=email).exists():
            error = "Ese correo ya está en uso."
        elif password != password2:
            error = "Las contraseñas no coinciden."
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=nombre)
            if tipo == "fundacion" and codigo == CODIGO_FUNDACION:
                grupo = Group.objects.get(name="Fundacion")
                user.groups.add(grupo)
            user.save()
            return redirect('login')
    return render(request, 'mascotas/registro.html', {'error': error})



def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'mascotas/detalle.html', {'mascota': mascota})


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer