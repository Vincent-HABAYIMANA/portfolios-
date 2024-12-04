from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class Collector(models.Model):
    collectorID = models.AutoField(primary_key=True ,unique=True)
    UserName = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    Site = models.CharField(max_length=255)
    InventoryN = models.TextField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="collect")
    def __str__(self):
        return self.UserName
    
    
    
class Users(models.Model):
    userN = models.AutoField(primary_key=True, unique=True)  # Auto-incremented primary key
    userName = models.CharField(max_length=150)
    email = models.EmailField(validators=[EmailValidator()])
    password = models.CharField(max_length=128)  
    phone = models.CharField(max_length=15)  # Assuming phone number format
    userrole = models.CharField(max_length=50)  # E.g., admin, customer, etc.
    district = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    # user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="collectors")
    def __str__(self):
        return f"{self.userName} ({self.userrole})"
    
class Items(models.Model):
    item = models.AutoField(primary_key=True)
    userN = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Used')
    category = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='items_pictures/')
    itemname = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.itemname

class Inventory(models.Model):
    Inventory = models.AutoField(primary_key=True ,unique=True, null=False)
    InventoryName = models.CharField(max_length=150)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='supplies')
    site = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usern")
    def __str__(self):
        return self.InventoryName 
      
class Transactions(models.Model):
    Transaction = models.AutoField(primary_key=True)
    userN = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Useid')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Useid')
    pending = models.BooleanField(default=True)
    collected = models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="userp")
    def __str__(self):
        return f"Transaction {self.Transaction}: User {self.user}, Item {self.item}"
    

    
class Account(models.Model):
    userN = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Useraccount',null=True, blank=True)
    AccountNumber = models.CharField(max_length=20, primary_key=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account {self.AccountNumber} - {self.username}"
class Payment(models.Model):
    Transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, related_name='Userid')  # Auto-incremented primary key
    userN = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Userid')
    accountNUMBER = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Userid')
    username = models.CharField(max_length=150)

    def __str__(self):
        return f"Transaction {self.Transaction} by {self.username}"
class Supplies(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='ItemName')
    item1= models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Item1')
    Category = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Category')
    ItemName = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='ItemName')
    Accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ItemName} - {self.Category}"

class Branch(models.Model):
    brancher=models.CharField(max_length=20, primary_key=True, blank=True)
    branchName=models.CharField(max_length=100)
    location=models.CharField(max_length=50, blank=True)
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='ItemNam')
    
    
    def __str__(self) -> str:
        return f"{self.branchName} - {self.collector}"