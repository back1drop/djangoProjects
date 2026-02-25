from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Order,OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'product_detail.html',{'product':product})

def add_to_cart(request,pk):
    product=get_object_or_404(Product,pk=pk)
    cart=request.session.get('cart',{})
    if str(pk) in cart:
        cart[str(pk)] +=1
    else:
        cart[str(pk)]=1
    request.session['cart']=cart
    return redirect('cart')

def cart_view(request):
    cart=request.session.get('cart',{})
    items= []
    total=0
    for product_id,quantity in cart.items():
        product=Product.objects.get(id=product_id)
        subtotal=product.price * quantity
        total += subtotal
        items.append({
            'product':product,
            'quantity':quantity,
            'subtotal':subtotal
        })
        return render(request,'cart.html',{
            'items':items,
            'total':total
        })

def update_cart(request,pk):
    cart=request.session.get('cart',{})
    quantity=int(request.POST.get('quantity'))
    if quantity>0:
        cart[str(pk)]=quantity
    else:
        cart.pop(str(pk))
    request.session['cart']=cart
    return redirect('cart')

def checkout(request):
    cart=request.session.get('cart',{})
    if not cart:
        return redirect('product_list')
    order=Order.objects.create(user=request.user)
    for product_id,quantity in cart.items():
        product=Product.objects.get(id=product_id)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )
    request.session['cart']={}
    return redirect('order_history')


def order_history(request):
    orders = Order.objects.filter(user=request.user, completed=False)
    return render(request, 'order_history.html', {'orders': orders})