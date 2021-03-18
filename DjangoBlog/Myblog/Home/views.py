from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Blog.models import Post
# Create your views here.
def home(request):
    homepost = Post.objects.all()[::-1]
    onlypost = homepost[:4]
    context={
        'posts':onlypost,
    }
    return render(request,'home/home.html',context)

def contact(request):
    #messages.success(request, 'Welcome to contact')
    if(request.method=='POST'):
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']

        if len(name)< 2 or len(email)<5 or len(phone)<6 or len(content)<5:
            messages.error(request,"Please Fill The Form Correctly ")
        else:
            contact=Contact(name = name,email=email,phone=phone,content = content)

            contact.save()
            messages.success(request,"Form is submitted successfully")


    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')
def search(request):
    query = request.GET['search']
    if(len(query)>75):
        allpost=POST.objects.none()
        
        
    else:
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpost=allposttitle.union(allpostcontent)
        
    if(allpost.count()==0):
        messages.warning(request,"No search result found ")
        
    print("All the posts " + str(len(allpost)))
    params={'allpost':allpost,
            'query':query}
    return render(request,'home/search.html',params)

def handlesignup(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm=request.POST['password2']
        if(password!=confirm):
            messages.error(request,"Password didn't match")
            return redirect('home')
        if(len(username)<5 and len(username)>25):
            messages.error(request,"Please change your username .")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"Please change your username . Username should only contain Alpha nummeric value")
            return redirect('home')
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"Your account has been created")
        return redirect('home')
        
            
        
    else:
        messages.error(request,"Enter valid details")
        return redirect('home')
    
def handlelogout(request):
    
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')

    

def handlelogin(request):
        if request.method =="POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpass']
            user = authenticate(username=loginusername,password = loginpassword)
            print("Fetched login username is "+loginusername )
            if user != None:
                login(request,user)
                messages.success(request,"Logged in ")
                return redirect('home')
            else:
                messages.error(request,"Invalid ! Try again")
                return redirect('home')
        else:
            return HttpResponse("ERROR 404")
            

