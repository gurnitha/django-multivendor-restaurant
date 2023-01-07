# app/accounts/signals.py

# Django modules
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from app.accounts.models import User, UserProfile

"""
Well, the signals are the utilities or feature that helps us 
to connect the events with the actions.
So this simply means that signals are used to perform some actions 
on every modification or creation of a particular entry in the database.

So the most common use cases of using signal is to automatically 
creating a profile instance as soon as the user is created.
"""

"""
About Receiver and Sender:

Receiver is a function, in this case: post_save_create_profile_receiver, 
it takes 4 parameters:
- sender (User),
- instance (that is something created by User),
- created (a boolean value, will show up when something is created), and
- **kwargs.
Sender is the User model itself.
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
    print(created) # print something if user is created (True or False).
    if created:
        UserProfile.objects.create(user=instance)
        print('User profile is created')
        ''' User profile is created.
        So now we have to create profile instance
        to be able to update userprofile
        '''
    else:
        '''
        1. If User profile was updated, then 'created' is false.
        2. Create userprofile and save it.
        3. Jika userprofile dihapus, kemudian user di-update, akan terjadi error.
        4. Gunakan try block untuk menghindari situasi ini (poin 3).
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

'''Bellow is the way to connect with the receiver.
But we will use @ (decocator), see above''' 
# post_save.connect(post_save_create_profile_receiver, sender=User)