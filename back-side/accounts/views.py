from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('servers:getmovie')    # 완성후 메인 페이지로 수정
        
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, '', context)    # 이동할 페이지 수정필요
