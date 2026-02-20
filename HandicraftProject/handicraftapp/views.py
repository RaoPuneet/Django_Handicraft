from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from .models import UserProfile
from django.db import IntegrityError
from .models import Product, Category
from django.shortcuts import render, get_object_or_404

from django.db import models

def home(request):
    return render(request, 'main_home.html')
def p1(request):
    return render(request, 'p1.html')
def p2(request):
    return render(request, 'p2.html')
def p3(request):
    return render(request, 'p3.html')
def p4(request):  
    return render(request, 'p4.html')
def p5(request):
    return render(request, 'p5.html')
def p6(request):
    return render(request, 'p6.html')
def p7(request):
    return render(request, 'p7.html')
def p8(request):
    return render(request, 'p8.html')
def p9(request):
    return render(request, 'p9.html')
def p10(request):
    return render(request, 'p10.html')
def p11(request):
    return render(request, 'p11.html')
def p12(request):
    return render(request, 'p12.html')
def p13(request):
    return render(request, 'p13.html')
def payment(request):
    return render(request, 'payment.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirect based on role
            if user and hasattr(user, 'userprofile'):
                if user.userprofile.role == 'seller':
                    return redirect("seller_dashboard")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    return render(request, "cart.html")



# 📝 SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        # ✅ Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken ❌")
            return redirect("signup")

        # ✅ Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address ❌")
            return redirect("signup")

        # ✅ Duplicate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered ❌")
            return redirect("signup")

        # ✅ Password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match ❌")
            return redirect("signup")

        # ✅ Create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # ✅ Create profile safely
        try:
            UserProfile.objects.create(user=user, role=role)
        except IntegrityError:
            messages.warning(request, "Profile already exists")

        # ✅ Send welcome email
        send_mail(
            "Welcome to Handicraft Khazana Shop 🎉",
            f"Hi {first_name},\n\n"
            f"Thank you for registering.\n"
            f"Your account has been successfully created.\n\n"
            f"Happy Shopping!\n"
            f"Handicraft Khazana Team",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )

        messages.success(request, "Account created successfully ✅")
        return redirect("login")

    return render(request, "signup.html")

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    new_arrivals = Product.objects.order_by('-created_at')[:7]
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())

    return render(request, 'main_home.html', {
        'products': products,
        'categories': categories,
        'new_arrivals': new_arrivals,
        'cart_count': cart_count
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })

# views.py
@login_required
def seller_dashboard(request):
    if request.user.userprofile.role != 'seller':
        messages.error(request, "Access denied. Buyers cannot view the dashboard.")
        return redirect('home')
    
    # Get only products belonging to this seller
    my_products = Product.objects.filter(seller=request.user)
    return render(request, 'seller_dashboard.html', {'my_products': my_products})
    

@login_required
def add_category(request):
    # Security check: only allow sellers
    if request.user.userprofile.role != 'seller':
        messages.error(request, "Only sellers can add categories.")
        return redirect('home')

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image') # Note: Use request.FILES for images
        Category.objects.create(name=name, image=image)
        messages.success(request, "Category added successfully! ✅")
        return redirect('home')

    return render(request, 'add_category.html')
@login_required
def add_product(request):
    if request.user.userprofile.role != 'seller':
        messages.error(request, "Only sellers can add products.")
        return redirect('home')

    categories = Category.objects.all()

    if request.method == "POST":
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        
        # We now include seller=request.user
        Product.objects.create(
            category=category,
            seller=request.user,  # This links the product to the logged-in seller
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            image=request.FILES.get('image')
        )
        messages.success(request, "Product added successfully! ✅")
        return redirect('seller_dashboard') # Send them to their dashboard

    return render(request, 'add_product.html', {'categories': categories})

@login_required
def delete_product(request, product_id):
    # Security: Ensure only sellers can access this view
    if request.user.userprofile.role != 'seller':
        messages.error(request, "Access denied.")
        return redirect('home')

    # Fetch product or 404
    product = get_object_or_404(Product, id=product_id)

    # Ownership Check: Only the seller who created it can delete it
    if product.seller == request.user:
        product.delete()
        messages.success(request, f"'{product.name}' has been removed from the shop. ❌")
    else:
        messages.error(request, "You do not have permission to delete this item.")

    return redirect('seller_dashboard')



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})
    pid = str(product_id)

    if pid in cart:
        cart[pid]['quantity'] += 1
    else:
        cart[pid] = {
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url if product.image else '',
            'quantity': 1
        }

    request.session['cart'] = cart
    messages.success(request, f"{product.name} added to cart ✅")

    return redirect('home')


def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'cart.html', {
        'cart': cart,
        'total': total
    })

def checkout_view(request):
    cart = request.session.get('cart', {})
    # 1. Calculate the total (needed for the UI)
    total = sum(float(item['price']) * int(item['quantity']) for item in cart.values())

    if request.method == "POST":
        # 2. Save info to session
        request.session['customer_info'] = {
            "name": request.POST.get("name"),
            "address": request.POST.get("address"),
            "phone": request.POST.get("phone")
        }
        # 3. Move to next step
        return redirect('payment')

    # 4. If not POST, just show the page with the cart data
    return render(request, "checkout.html", {'cart': cart, 'total': total})


# views.py

@login_required
def payment_view(request):
    cart = request.session.get('cart', {})
    customer = request.session.get('customer_info', {})
    
    # Calculate Total
    total = sum(float(item['price']) * int(item['quantity']) for item in cart.values())

    if request.method == "POST":
        # 1. Create a readable list of products for the email
        product_list = ""
        for item in cart.values():
            product_list += f"- {item['name']} (Qty: {item['quantity']}) : ₹{item['price']}\n"

        # 2. Get the logged-in user's email
        user_email = request.user.email

        # 3. Send Payment Confirmation Email
        subject = "Order Confirmed - Handicraft Khazana Shop 🏺"
        message = (
            f"Hi {request.user.first_name},\n\n"
            f"Thank you for your purchase! We have received your payment of ₹{total}.\n\n"
            f"Order Details:\n{product_list}\n"
            f"Shipping to:\n{customer.get('address')}\n"
            f"Phone: {customer.get('phone')}\n\n"
            f"Your masterpieces will be delivered soon!\n\n"
            f"Happy Shopping,\nHandicraft Khazana Team"
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=True,
        )

        # 4. Clear the cart and customer info after success
        request.session['cart'] = {}
        request.session['customer_info'] = {}
        
        messages.success(request, "Order placed successfully! Check your email for receipt. ✅")
        return redirect('home')

    return render(request, "payment.html", {"total": total})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)

    if pid in cart:
        del cart[pid]

    request.session['cart'] = cart
    messages.warning(request, "Item removed ❌")

    return redirect('cart')

