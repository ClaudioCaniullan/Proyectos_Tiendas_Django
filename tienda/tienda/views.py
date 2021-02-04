# Django
from django.shortcuts import render 

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