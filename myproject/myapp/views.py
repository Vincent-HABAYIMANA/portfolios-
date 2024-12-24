from django.shortcuts import render,redirect
from .models import Users ,Collector1,PaymentInfo,RecyclingInfo,WasteSubmission,Category,CardDetail,Payment1
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
import json


# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse('hello django!')
def home(request):
    features = Feature.objects.all()  # Fetch all features from the database
    steps = Step.objects.all()         # Fetch all steps from the database
    messages = Message.objects.all()   # Fetch messages if applicable

    return render(request, 'index.html', {
        'features': features,
        'steps': steps,
        'messages': messages,
    })
    return render(request, 'index.html')

def request(request,pk):
    collectors = Collector1.objects.all()
    categories = Category.objects.all()
    user=Users.objects.get(pk=pk)
    
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        selected_category_id = request.POST.get('selected_category')  # ID from hidden input
        collector_id = request.POST.get('collector')
        address = request.POST.get('address')
        latitude = request.POST.get('latitude')  # Latitude from hidden field or manual input
        longitude = request.POST.get('longitude')  
        image = request.FILES.get('file_upload')  

        # Validate and retrieve foreign key objects
        category = Category.objects.get(id=selected_category_id) if selected_category_id else None
        collector = Collector1.objects.get(id=collector_id) if collector_id else None

        # Create WasteSubmission instance
        waste_submission = WasteSubmission(
            item_name=item_name,
            category=category,
            NameCollector=collector,
            image=image,
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        waste_submission.save()

        return redirect('dashboardUser', pk=user.userN)
    
    return render(request, 'request.html', {
        'collectors': collectors,
        'categories': categories,
        
        })
  
def paymentInfo(request):
    return render(request, 'paymentInfo.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        email=request.POST.get('email','')
        district = request.POST.get('district', '')
        sector = request.POST.get('sector', '')
        cell = request.POST.get('cell', '')
        village = request.POST.get('village', '')
        
        new_users = Users(
            Name=username,
            email=email,
            password=password,
            phone=phone,
            district=district,
            sector=sector,
            cell=cell,
            village=village,
            
        )
        new_users.save()
        return render(request, 'signup.html', {})
        
       
    return render(request, 'signup.html')  
  
def verify(request):
    return render(request, 'verify.html')
def started(request,pk):
    user=Users.objects.get(userN=pk)
    recycling_info = RecyclingInfo.objects.first()
    return render(request, 'home.html', {'recycling_info': recycling_info,'user':user})

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Retrieve the user based on the email
            user = Users.objects.get(email=email)

            # Check if the provided password matches the stored hash
            if (password, user.password):
                # Redirect to the dashboard or appropriate page
                return redirect('dashboardUser', pk=user.userN)
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
        username = request.POST.get('name', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        email= email.POST.get()
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
                Name=username,
                email=email,
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

def dashboardUser(request,pk):
    waste_submissions = WasteSubmission.objects.all()
    user=Users.objects.get(userN=pk)
    wastes=WasteSubmission.objects.filter(user=user)
    
   
    payment=PaymentInfo.objects.all()
    context={
        'user':user,
        'wastes':wastes,
        'payment':payment,
        'waste_submissions': waste_submissions,
    }
    
    return render(request, 'dashboardUser.html',context)

def dashboardAdmin(request):
    category=Category.objects.all()
    waste_submissions = WasteSubmission.objects.filter( status='Pending').count()
    waste_submissions1 = WasteSubmission.objects.filter(
    (Q(status='Accepted') | Q(status='Rejected'))).count()
    users = Users.objects.all()
    collectors=Collector1.objects.all()
    waste_submissions = WasteSubmission.objects.all()
    return render(request, 'dashboardAdmin.html',{
        'users':users,
        'waste_submissions': waste_submissions,
        'collectors':collectors,
        'waste_submissions':waste_submissions,
         'waste_submissions1':waste_submissions1,
         'category': category,
                                                  })


def collector(request, pk):
    collector_instance = get_object_or_404(Collector1, pk=pk)  # Fetch the Collector1 instance
    farmers = WasteSubmission.objects.all().values('NameCollector', 'address')
    farmers_data = json.dumps(list(farmers))

    waste_submissions = WasteSubmission.objects.filter(NameCollector=collector_instance, status='Pending')
    waste_submissions2 = WasteSubmission.objects.filter(NameCollector=collector_instance, status='Accepted')
    waste_submissions1 = WasteSubmission.objects.filter(
        Q(NameCollector=collector_instance) & (Q(status='Accepted') | Q(status='Rejected'))
    )
    new_requests_count = waste_submissions.count()

    if request.method == 'POST':
        # Get form data
        waste_submission_id = request.POST.get('collector')  # Pass WasteSubmission ID from the form
        name_requester = request.POST.get('name')
        item_name = request.POST.get('item_name')
        amount = request.POST.get('amount')

        # Fetch the WasteSubmission instance
        waste_submission_instance = get_object_or_404(WasteSubmission, id=waste_submission_id)

        # Save the Payment1 object
        Payment1.objects.create(
            collector=waste_submission_instance,  # Assign the WasteSubmission instance
            name_requester=name_requester,
            item_name=item_name,
            amount=amount,
        )
        return redirect('collector', pk=pk)  # Redirect after saving

    return render(request, 'collector.html', {
        'waste_submissions': waste_submissions,
        'new_requests_count': new_requests_count,
        'collector': collector_instance,
        'collectors': Collector1.objects.all(),
        'waste_submissions1': waste_submissions1,
        'waste_submissions2': waste_submissions2,
        'farmers_data': farmers_data,
    })
    return render(request, "collector.html")

# views.py


def get_categories(request):
    categories = Category.objects.all().values('name')
    return JsonResponse(list(categories), safe=False)


# views.pyfrom django.shortcuts import render
from .models import WasteSubmission, Collector1, Category

def submit_waste(request):
    collectors = Collector1.objects.all()  # Fetch all collectors
    categories = Category.objects.all()  # Fetch all categories

    # Check if the user is authenticated
    if 'user_id' not in request.session:  # Assuming user_id is stored in session
        return redirect('login')  # Redirect unauthenticated users to login page

    # Retrieve the logged-in user from the session
    user_id = request.session.get('user_id')
    try:
        logged_in_user = Users.objects.get(userN=user_id)
    except Users.DoesNotExist:
        return redirect('login')  # Handle invalid session

    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        selected_category_id = request.POST.get('selected_category')
        collector_id = request.POST.get('collector')
        address = request.POST.get('address')
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        image = request.FILES.get('file_upload')

        # Validate and retrieve foreign key objects 
        try:
            category = Category.objects.get(id=selected_category_id) if selected_category_id else None
        except Category.DoesNotExist:
            category = None

        try:
            collector = Collector1.objects.get(id=collector_id) if collector_id else None
        except Collector1.DoesNotExist:
            collector = None

        # Set defaults for latitude and longitude if not provided
        latitude = float(latitude) if latitude not in [None, ''] else -1.9441
        longitude = float(longitude) if longitude not in [None, ''] else 30.0619

        # Create WasteSubmission instance
        waste_submission = WasteSubmission(
            item_name=item_name,
            category=category,
            NameCollector=collector,
            image=image,
            address=address,
            latitude=latitude,
            longitude=longitude,
            user=logged_in_user  # Assign the logged-in user here
        )
        waste_submission.save()

        # Return with a success message and the categories and collectors
        return render(request, 'request.html', {
            'message': 'Submission successful!',
            'collectors': collectors,
            'categories': categories
        })

    # For GET requests, return the form with all collectors and categories
    return render(request, 'request.html', {
        'collectors': collectors,
        'categories': categories
    })
def home_view(request):
    recycling_info = RecyclingInfo.objects.first()  # Fetch the first entry
    return render(request, 'your_template.html', {'recycling_info': recycling_info})


from .models import Feature, Step, Message ,RecyclingInfo1 # Adjust based on your actual models

def home_view(request):
    features = Feature.objects.all()  # Fetch all features from the database
    steps = Step.objects.all()         # Fetch all steps from the database
    messages = Message.get_messages()  # Assuming you have a method to get messages

    return render(request, 'index.html', {
        'features': features,
        'steps': steps,
        'messages': messages,
    })
    
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request):
    user = request.user  # Get the logged-in user
    context = {
        'user': user,  # Pass the user to the template
    }
    return render(request, 'payment.html', context)  # Create a new template for the profile


def your_view(request):
    # Fetch recycling information from the database
    recycling_info = RecyclingInfo1.objects.first()  # Adjust the query as needed

    return render(request, 'home.html', {
        'recycling_overlay_info': recycling_info
    })
    
    
    
    
    
def role_login(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if role == 'user':
            try:
                user = Users.objects.get(email=email)
                # Directly compare plain-text passwords for users (insecure)
                if password == user.password:
                    request.session['user_id'] = user.userN
                    messages.success(request, f"Welcome {user.Name}")
                    return redirect('dashboardUser')  # Replace with actual user dashboard
                else:
                    messages.error(request, "Invalid password")
            except Users.DoesNotExist:
                messages.error(request, "User not found")

        elif role == 'admin':
                try:
                    admin = User.objects.get(email=email, is_superuser=True)
                    # Use check_password for admin (hashed password)
                    if check_password(password, admin.password):
                        from django.contrib.auth import login  # Ensure the correct login is used
                        login(request, admin)  # Correctly pass the request and user object
                        messages.success(request, "Admin login successful")
                        return redirect('dashboardAdmin')  # Replace with actual admin dashboard
                    else:
                        messages.error(request, "Invalid password")
                except User.DoesNotExist:
                    messages.error(request, "Admin not found")

        elif role == 'collector':
            try:
                collector = Collector1.objects.get(email=email)
                # Directly compare plain-text passwords for collectors (insecure)
                if password == collector.password:
                    request.session['collector_id'] = collector.id
                    messages.success(request, f"Welcome {collector.name}")
                    return redirect('collector', pk=collector.id)  # Replace with actual collector dashboard
                else:
                    messages.error(request, "Invalid password")
            except Collector1.DoesNotExist:
                messages.error(request, "Collector not found")

        else:
            messages.error(request, "Invalid login role")
    
    return render(request, 'login.html')

#chat






def get_paid(request):
    # Fetch the associated WasteSubmission object
   
    if 'user_id' not in request.session:  # Assuming user_id is stored in session
        return redirect('login')  # Redirect unauthenticated users to login page

    # Retrieve the logged-in user from the session
    user_id = request.session.get('user_id')
    try:
        logged_in_user = Users.objects.get(userN=user_id)
    except Users.DoesNotExist:
        return redirect('login')  # Handle invalid session

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        number = request.POST.get('number')
        card_provider = request.POST.get('card_number')

        # Check if a CardDetail already exists for this WasteSubmission
       

        # Save the data to the CardDetail model
        card_detail = CardDetail.objects.create(
            
            full_name=full_name,
            number=number,
            card_provider=card_provider,
            user=logged_in_user 
            
            
        )
        card_detail.save()

        return HttpResponse("Card details submitted successfully!")

    return render(request, "paymentInfo.html")


def paymentInfo(request):
    # Example: Fetch a WasteSubmission
    waste_submission = WasteSubmission.objects.first()  # Replace with actual logic

    if waste_submission:
        return render(request, 'paymentInfo.html', {'waste_submission': waste_submission})
    else:
        return render(request, 'paymentInfo.html', {'waste_submission': None}) 
    
    
def update_status(request, submission_id):
   
    if request.method == 'POST':
        status = request.POST.get('status')  # Get the status from the form
        submission = get_object_or_404(WasteSubmission, id=submission_id)
        if status in ['Accepted', 'Rejected']:
            submission.status = status
            submission.save()
            collector = submission.NameCollector 
            return redirect('collector',pk=collector.id)  # Redirect to the appropriate page
        else:
            return HttpResponse("Invalid status", status=400)
    return HttpResponse("Invalid request", status=405)