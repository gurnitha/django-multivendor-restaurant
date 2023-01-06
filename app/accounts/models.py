# app/accounts/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# UserManager class will: 
# 1. contain 2 methods: create_user and create_superuser
# 2. not have any field
class UserManager(BaseUserManager):
	pass

# CustomUser will contain fields
class User(AbstractBaseUser):
	pass
