from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class Users(models.Model):
    userN = models.AutoField(primary_key=True, unique=True)  # Auto-incremented primary key
    Name = models.CharField(max_length=150)
    email = models.EmailField(validators=[EmailValidator()])
    password = models.CharField(max_length=128)  
    phone = models.CharField(max_length=15)  # Assuming phone number format 
    district = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    # user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="collectors")
    def __str__(self):
        return f"{self.Name}"
 

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
from django.db import models

class Collector1(models.Model):
    
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    email = models.EmailField(max_length=255)  # Ensure emails are unique
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.name

 
class Branch(models.Model):
    brancher=models.CharField(max_length=20, primary_key=True, blank=True)
    branchName=models.CharField(max_length=100)
    location=models.CharField(max_length=50, blank=True)
    NameCollector = models.ForeignKey(Collector1, on_delete=models.CASCADE, related_name='ItemNam')
    
    
    def __str__(self) -> str:
        return f"{self.branchName}"   
    
    
class WasteSubmission(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
    NameCollector = models.ForeignKey(Collector1, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='waste_images/')
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(default=-1.9441)  # Default to Kigali latitude
    longitude = models.FloatField(default=30.0619)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(default="Pending", max_length=26)

    def __str__(self):
        return f"{self.item_name} - {self.category} - {self.NameCollector}"

class PaymentInfo(models.Model):
    waste_submission = models.OneToOneField(WasteSubmission, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment Info for {self.waste_submission.item_name}"
    
class CardDetail(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100)
    number = models.CharField(max_length=16)  # Adjust length for card number
    card_provider = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} ({self.card_provider})"

class RecyclingInfo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100)
    button_description = models.TextField()

    def __str__(self):
        return self.title
    
    
    

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Step(models.Model):
    description = models.TextField()

class Message(models.Model):
    content = models.TextField() 
    
class RecyclingInfo1(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
    
class PaymentRequest(models.Model):
    full_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bank = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    
class Payment1(models.Model):
    collector = models.ForeignKey(WasteSubmission, on_delete=models.CASCADE, related_name='collector_payment')
    name_requester = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Handles both RWF and $
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_requester} - {self.item_name} - {self.amount}"