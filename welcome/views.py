from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from decimal import Decimal
from .models import Order, OrderItem
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem, UserProfile
from .forms import ProductForm

def home(request):
    return render(request, 'cafeteria/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if user_profile.is_admin:
        return redirect('admin_dashboard')
    else:
        return redirect('customer_dashboard')

@login_required
def customer_dashboard(request):
    products = Product.objects.filter(is_available=True)
    cart_items = Cart.objects.filter(user=request.user)
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    # Search and filter
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if category_filter:
        products = products.filter(category=category_filter)
    
    cart_total = sum(item.total_price for item in cart_items)
    
    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'recent_orders': recent_orders,
        'search_query': search_query,
        'category_filter': category_filter,
    }
    return render(request, 'cafeteria/customer_dashboard.html', context)

@login_required
def admin_dashboard(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not user_profile.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('customer_dashboard')
    
    products = Product.objects.all()
    orders = Order.objects.all()
    
    context = {
        'products': products,
        'orders': orders,
    }
    return render(request, 'cafeteria/admin_dashboard.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    return redirect('customer_dashboard')

@login_required
def update_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        elif action == 'remove':
            cart_item.delete()
    
    return redirect('customer_dashboard')

@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('dashboard')

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
    user=request.user,
    total_amount=total,
    status="Pending"
)


    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    
    cart_items.delete()

    return redirect('dashboard')

@login_required
def add_product(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not user_profile.is_admin:
        messages.error(request, 'Access denied.')
        return redirect('customer_dashboard')
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    
    return render(request, 'cafeteria/add_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not user_profile.is_admin:
        messages.error(request, 'Access denied.')
        return redirect('customer_dashboard')
    
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('admin_dashboard')

@login_required
def update_order_status(request, order_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not user_profile.is_admin:
        messages.error(request, 'Access denied.')
        return redirect('customer_dashboard')
    
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Completed']:
            order.status = new_status
            order.save()
            messages.success(request, f'Order #{order.id} status updated!')
    
    return redirect('admin_dashboard')