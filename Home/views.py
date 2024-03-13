from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemsDetails,Cart
from .formsHome  import CreateUserForm,LoginUserForm
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/loginHome/')
def checkoutHome(request):
       template=loader.get_template('checkoutHome.html')
       current_user = request.user.id
       cart=Cart.objects.all().filter(Id_user=current_user).first()
       product=Items.objects.get(id=cart.Id_product)
       context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context)) 
def indexHome(request):
    template=loader.get_template('indexHome.html')
    return HttpResponse(template.render({'request':request}))
def add_to_cartHome(requset,id):
    currentuser=requset.user
    discount=2
    state=False
    Home=ItemsDetails.objects.select_related('itemsid').filter(id=id)
   
    for item in Home:
           net=item.total-discount
         
    cart = Cart(
        Id_product=item.id,
        Id_user=currentuser.id,
        price=item.price,
        qty=item.qty,
        tax=item.tax,
        total=item.total,
        discount=discount,
        net=net,
        status=state
    )
    currentuser=requset.user.id
    count=Cart.objects.filter(Id_user=currentuser).count()
    print(count)
    cart.save()
    requset.session['countcart']=count
    return redirect("/showHome")


def detailsHome(request , id):
     template=loader.get_template('detailsHome.html')
     
     currentuser=request.user
     print(currentuser.id)
     Home=ItemsDetails.objects.select_related('itemsid').filter(id=id)
    
     context={
         'Home':Home,
         'request':request
     }
     return HttpResponse(template.render(context))

def showHome(request):
    template=loader.get_template('showHome.html')
    Home=ItemsDetails.objects.select_related('itemsid')
   
    print(Home.query)
    return HttpResponse(template.render({'Home':Home, 'request':request}))

@csrf_exempt
def registerHome(request):
      template=loader.get_template('registerHome.html')
      form=CreateUserForm()
      if request.method=="POST":
           form=CreateUserForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('loginHome')
      context={'registerform':form}
      return HttpResponse(template.render(context=context))
@csrf_exempt
def logoutHome(request):
     if request.method=="POST" :
          logout(request)
          return redirect("/")
@csrf_exempt
def loginHome(request):
     form=LoginUserForm()
     if request.method=="POST":
          form=LoginUserForm(data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']

              user=authenticate(username=username,password=password)
              if user:
                   if user.is_active:
                        login(request,user)
                        return render(request,'indexHome.html')
     context={'form':form}
     return render(request,'loginHome.html',context)
                        

# Create your views here.
