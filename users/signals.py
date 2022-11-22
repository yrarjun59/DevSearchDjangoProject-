from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings


from .models import Profile

def createProfile(sender, instance , created, **kwargs):
  print("Profile signal triggered")
  if created:
    user = instance
    profile = Profile.objects.create(
      user = user,
      username = user.username,
      email = user.email,
      name = user.first_name
    )

    subject = 'Welcome to DevSearch Club'
    message = 'We are glad that you join here'
    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [profile.email],
      fail_silently=False,
)

def updateUser(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user

  if created == False:
    user.first_name = profile.name
    user.email = profile.email
    user.username = profile.username
    user.save()
    
def deleteUser(sender,instance, **kwargs):
  user = instance.user
  user.delete()

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)