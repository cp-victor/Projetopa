from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm
from .models import Fornecedor


def home(request):
	return render(request, 'home.html')

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('forn_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})

def forn_detail(request, pk):
	forn = get_object_or_404(Fornecedor, pk=pk)
	return render(request, 'forn_detail.html', {'forn': forn})