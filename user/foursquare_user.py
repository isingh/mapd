from mapd.auth import credentials
from mapd.config import foursquare_settings
from mapd.user.base_user import BaseUser
from mapd.utils import foursquare_utils

import logging

class FoursquareUser(BaseUser):
  """A user with foursquare credentials.
  """

  def __init__(self, credentials):
    """Constructor for a FoursquareUser.

    Args:
      credentials - The credentials that can be used to uniquely idenity this
                    user on foursquare.
    """
    if credentials is None:
      credentials = credentials.FoursqaureCredentials()
    self._credentials = credentials
    self._user = None

  def _LoadUserInformation(self):
    """Load the information of the user from foursquare.
    """
    self._user = None
    if not self.is_authorized:
      return
    user_info_url = foursquare_settings.API_URL + '/users/self'
    user_info_url += ('?oauth_token=%s' % self._credentials.access_token)
    (success, code, response) = foursquare_utils.MakeAPICall(user_info_url)
    if success and code == 200:
      self._user = response['user']

  @property
  def is_authorized(self):
    if self._credentials.access_token:
      return True
    return False

  @property
  def name(self):
    """Return the name of the user.

    This API should go to cache, db and then finally foursquare. However since
    at this time we dont user the first two, we directly query foursquare for
    all the information.
    """
    if self._user is None:
      self._LoadUserInformation()
    return self._user['firstName']

  def GetRecentCheckins(self):
    """Get the recent checkins of this user.

    Returns:
      a list of recent checkins.
    """
    return foursquare_utils.GetLatestCheckins(self._credentials.access_token)
