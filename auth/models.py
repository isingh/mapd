"""Definition of all the models used.
"""

from django.db import models

class RegisteredUser(models.Model):
  """A user who has registered through atleast one of the available
  authentication channels.
  """
  user_email = models.EmailField()
  user_first_name = models.CharField(max_length=512)
  user_last_name = models.CharField(max_length=512)
  foursquare_reg_details = models.ForeignKey('FoursquareRegistration')

class RegistrationDetails(models.Model):
  """Registration details associated with a registered user.
  """
  registration_date = models.DateField(auto_now_add=True)

class FoursquareRegistration(RegistrationDetails):
  """Information pertinent to a user who registered via FourSquare.
  """
  access_token = models.CharField(max_length=200)
