from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CreateAppSerializer
from .serializers import UpdateAppSerializer
from urllib.parse import unquote
from .models import App
# Create your views here.
@login_required(login_url="login")
def home(request):
   apps = App.objects.select_related('user').filter(user = request.user)
   return render(request,'dashboard.html',{'apps':apps})




def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            print('invalid password or username')
            return render(request,'login.html',{'login_status':'invalid password or username'})
    else:
        return render(request, "login.html",{"login_status":''})



def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 :
            if User.objects.filter(username=username).exists():

                return render('signup.html',{'signup_status':'Username Already Registered'})

            elif User.objects.filter(email=email).exists():

                return render('signup.html',{'signup_status':'Username Already Registered'})

            else:
                user = User.objects.create_user(
                    username=username, first_name=username, password=password1, email=email)
                user.save()
                return redirect('login')

        else:
            return render('signup.html',{"signup_status":'Password Miss match'})
    else:
        return render(request, "signup.html")


def logout_form(request):
    logout(request)
    return redirect('login')

@api_view(['POST'])
def create_app(request):
    if request.user.is_authenticated:
        app_name = request.data['app_name']
        app_description = request.data['app_description']
        
        data = {
            'app_name':app_name,
            'app_description':app_description,
            'user':request.user.id
        }

        srlzr = CreateAppSerializer(data=data)
        if srlzr.is_valid():
            srlzr.save()
            return Response({"msg":"app is created"})
        else:
            return Response({'msg':srlzr.errors})
    else:
        return Response({'msg':'unauthenticated request'},403)

@api_view(["PUT"])
def update_app(request, pk):
    if request.user.is_authenticated:
        try:
            app = App.objects.get(id=pk)
            app_name = request.data['app_name']
            app_description = request.data['app_description']
            data = {
                'app_name':app_name,
                'app_description':app_description,
                'user':request.user.id
            }

            serializer = UpdateAppSerializer(instance=app, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"app is updated"})
            else:
                return Response({'msg':serializer.errors})
        except:
            return Response({'msg':f"No row to update with id:{pk}"})
    else:
        return Response({'msg':'unauthenticated request'},403)
        
@api_view(["DELETE"])
def delete_app(request, pk):
    if request.user.is_authenticated:
        try:
            app = App.objects.get(id=pk)
            app.delete()
            return Response({"msg":"app is deleted"})
        except:
            return Response({"msg":f"No app to delete with id:{pk}"})

    else:
        return Response({'msg':'unauthenticated request'},403)

@api_view(["PUT"])
def change_plan(request):
    if request.user.is_authenticated:
        app_id = request.data['app_id']
        selected_text = request.data['selected_text']
        
        if selected_text.strip() == '$ Plan - 0 Dollars':
            plan = 1
        elif selected_text.strip() == '$ Plan - 10 Dollars':
            plan = 2
        else:
            plan = 3
        try:
            app = App.objects.get(id=app_id)
            data = {
                'app_name':app.app_name,
                'app_description':app.app_description,
                'user':request.user.id,
                "plan":plan
            }
            print(data)
            serializer = UpdateAppSerializer(instance=app, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"plan is changed"})
            else:
                return Response({'msg':serializer.errors})
        except:
            return Response({'msg':f"No row to changed the app plan:{app_id}"})
    else:
        return Response({'msg':'unauthenticated request'},403)