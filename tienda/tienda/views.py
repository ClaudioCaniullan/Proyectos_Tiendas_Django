# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import RegisterForm

def index(request):
	return render(request,'index.html', {
		'message': 'listado de productos', 
		'title': 'Productos', 
		'products': [ 
		        {'title':'camisa', 'price':10 ,'stock':True},
		        {'title':'gorro', 'price':20 ,'stock':True},
		        {'title':'pantalon', 'price':30 ,'stock':False},
		]

		})


def login_usuario(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# si user existe en nuestra base de datos hay login
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			# una vez logeado enviamos un mensaje desde el servidor
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('index')
		else:
			messages.error(request, 'Usuario o contraseña no validos')

	return render(request, 'users/login.html', {})



def logout_usuario(request):
	logout(request)
	messages.success(request, 'Sesión cerrada exitosamente')
	return redirect('login_usuario')


def registro(request):
	form = RegisterForm()
	return render(request, 'users/registro.html', {'form':form})