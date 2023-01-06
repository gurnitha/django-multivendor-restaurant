# app/accounts/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# UserManager class will: 
# 1. contain 2 methods: create_user and create_superuser
# 2. not have any field
class UserManager(BaseUserManager):
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

        
# CustomUser will contain fields
class User(AbstractBaseUser):
	pass
