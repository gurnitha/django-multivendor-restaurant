# app/accounts/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

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

# CustomUser will contain fields
class CustomUser(AbstractBaseUser):
	pass

