from django import forms
from .models import Fornecedor

class PostForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = ['nameforn','cnpj', ]