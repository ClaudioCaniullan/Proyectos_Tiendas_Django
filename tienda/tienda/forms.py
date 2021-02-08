from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(
		required=True, 
		min_length=4, 
		max_length=50,
		# aplicamos estilo a nuestro input con widget
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'id':'username',
			})
		)
	
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'id':'email',
			'placeholder':'tienda@tienda.com'
			})
		)
		
	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			'id':'password',
			})
			)

	def claean_username(self):
		#obtenemos los inputs del formulario
		username = self.cleaned_data.get('username')
		#verificamos si existen en db
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('El username ya se encuentra en uso')
		# de no existir
		return username






