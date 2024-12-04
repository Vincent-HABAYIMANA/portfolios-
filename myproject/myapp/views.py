from django.shortcuts import render,redirect
from .models import Users
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse('hello django!')
def home(request):
    return render(request, 'index.html')
def request1(request):
    return render(request, 'request2.html')
  
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        userrole = request.POST.get('userrole', '')
        district = request.POST.get('district', '')
        sector = request.POST.get('sector', '')
        cell = request.POST.get('cell', '')
        village = request.POST.get('village', '')
        
        new_users = Users(
            userName=username,
            password=password,
            phone=phone,
            userrole=userrole,
            district=district,
            sector=sector,
            cell=cell,
            village=village,
            
        )
        new_users.save()
        return render(request, 'login.html', {})
        
       
    return render(request, 'signup.html')  
  
def verify(request):
    return render(request, 'verify.html')
def started(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Retrieve the user based on the email
            user = Users.objects.get(email=email)

            # Check if the provided password matches the stored hash
            if check_password(password, user.password):
                # Redirect to the dashboard or appropriate page
                return redirect('started')
            else:
                # Add error message for incorrect password
                messages.error(request, "Invalid email or password.")
        except Users.DoesNotExist:
            # Add error message for non-existent user
            messages.error(request, "Invalid email or password.")
        except Users.MultipleObjectsReturned:
            # Handle duplicate users in the database (shouldn't occur if email is unique)
            messages.error(request, "Multiple accounts found with this email. Please contact support.")

    # Render the login page for GET requests or after a failed POST
    return render(request, 'login.html')

def register_user(request):
    if request.method == "POST":
        email = request.POST.get('email', '')  # Extract email
        print(f"Email received: {email}") 
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        email= email.POST.get()
        userrole = request.POST.get('userrole', '')
        district = request.POST.get('district', '')
        sector = request.POST.get('sector', '')
        cell = request.POST.get('cell', '')
        village = request.POST.get('village', '')
        confirm_password = request.POST.get("confirm_password")

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        try:
            # Save the new user
            user = Users(
                phone=phone,
                password=make_password(password), # This will be hashed in the model's save method
                userName=username,
                email=email,
                userrole=userrole,
                district=district,
                sector=sector,
                cell=cell,
                village=village,
                
            )
            user.save()
            messages.success(request, "User registered successfully!")
            return redirect('signup')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')

    return render(request, "login.html")