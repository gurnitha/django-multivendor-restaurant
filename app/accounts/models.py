# app/accounts/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

""" 
About BaseUserManager:
This BaseUserManager will allow you to edit the way how the users and superusers are created.
As you can see, we have created two methods that is one for creating a user and another for creating
a superuser
"""

"""
About UserManager class:
UserManager class will: 
1. contain 2 methods: create_user and create_superuser
2. not have any field
"""
class UserManager(BaseUserManager):
    # Defining create_user method with parameters:self, first_name, last_name, username, email, password=None
    def create_user(self, first_name, last_name, username, email, password=None):
        # Check email
        if not email:
            raise ValueError('User must have an email address')

        # Check username
        if not username:
            raise ValueError('User must have an username')

        # Create user using the model with values: email, username, first_name, and last_name
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        # Set password using set_password method with password as parameter.
        # set_password encodes the password because we can not store password in the database.
        user.set_password(password)
        # Save user in the default database.
        user.save(using=self._db)
        return user

    # Defining create_superuser method with parameters:self, first_name, last_name, username, email, password=None
    def create_superuser(self, first_name, last_name, username, email, password=None):
        # The 'normal user' actually has been created using the create_user method above. 
        # Now assigning it as superuser with these values: email, username, password, first_name, and last_name.
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        # Assigning the created user as admin, active, staff, and superadmin and save it to the default db.
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


""" 
About AbstractBaseUser:
This AbstractBaseUser will give you full control over Django's user model.
You can do whatever you want to do with this AbstractBaseUser model.
"""

# User will contain fields
class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    """
    About Login field:
    Django uses username as a login field by default.
    But we want to use email as login filed, instead of username.
    So we have to override the username.

    We also define the required fields: username, first_name, and last_name.
    So the required field is username.
    Email is also required field, but we don't need to put that email inside the required
    fields list because username field itself is a required field.
    So that's why we don't need to put email here. username, first_name and last_name
    also be required fields. 
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # To tell django which class to use. In this case we use UserManager class.
    # In the settings.py file we have to define to using User
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    """
    About has_module_perms:
    We'll return True if the user is an active superuser or is an admin.
    And for inactive users it will be always return false.
    That means by default, only admin and superadmin can have access to this model.
    """
    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role


# User profile
class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email




"""
Well, the signals are the utilities or feature that helps us 
to connect the events with the actions.
So this simply means that signals are used to perform some actions 
on every modification or creation
of a particular entry in the database.

So the most common use cases of using signal is to automatically 
creating a profile instance as soon as the user is created.
"""

"""
About Receiver and Sender:

Receiver is a function, in this case: post_save_create_profile_receiver, 
it takes 4 parameters:
- sender (CustomeUser),
- instance (that is something created by CustomeUser),
- created (a boolean value, will show up when something is created), and
- **kwargs.
Sender is the CustomeUser model itself.
"""
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    '''
    So as soon as the user is created, 
    or as soon as we get the response of created equal to true, 
    then what we need to do, we need to actually create the user profile.

    Steps:
    1. Check created flag is being true or false.
    2. If it is true, then create UserProfile
    '''
    print(created) # print something if user is created.
    if created:
        UserProfile.objects.create(user=instance)
        print('User profile is created')
        ''' User profile is created.
        So now we have to create profile instance
        to be able to update User profile
        '''
    else:
        '''
        1. If User profile is updated, then 'created' is false.
        2. Create User profile and save it.
        3. Jika User profile dihapus, kemudian user di-update, akan error.
        4. Gunakan try block untuk menghindari situasi ini.
        '''
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print('Profile was not exist, but I created one')
        print('User is updated') 

@receiver(pre_save, sender=User)
def post_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')

# @receiver(post_save, sender=User)
# def post_save_create_profile_receiver(sender, instance, created, **kwargs):
#     '''
#     So as soon as the user is created, 
#     or as soon as we get the response of created equal to true, 
#     then what we need to do, we need to actually create the user profile.

#     Steps:
#     1. Check created flag is being true or false.
#     2. If it is true, then create UserProfile
#     '''
#     print(created) # print something if user is created.
#     if created:
#         UserProfile.objects.create(user=instance)
#         print('User profile is created')
#         ''' User profile is created.
#         So now we have to create profile instance
#         to be able to update User profile
#         '''
#     else:
#         '''
#         1. If User profile is updated, then 'created' is false.
#         2. Create User profile and save it.
#         3. Jika User profile dihapus, kemudian user di-update, akan error.
#         4. Gunakan try block untuk menghindari situasi ini.
#         '''
#         try:
#             profile = UserProfile.objects.get(User=instance)
#             profile.save()
#         except:
#             # Create user profile if not exist
#             UserProfile.objects.create(user=instance)
#             print('Profile was not exist, but I created one')
#         print('User is updated') 


'''Bellow is the way to connect with the receiver.
But we will use @ (decocator), see above''' 
# post_save.connect(post_save_create_profile_receiver, sender=User)