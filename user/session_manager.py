from bunch import Bunch

from mapd.auth import credentials
from mapd.user.foursquare_user import FoursquareUser

_CREDENTIAL_KEY = 'credentials'
_USER_INFO_KEY = 'user_info'

class SessionManager(object):
  """Manage and retrieve data from the current session
  """
  def __init__(self, session):
    """Initialize a session manager for the given request.

    Args:
      session - The session object.
    """
    self._session = session

  def GetCredentials(self):
    """Get the credentials from the given request session.
    """
    return self._session.get(_CREDENTIAL_KEY, credentials.MapdCredentials())

  def SetCredentials(self, credentials):
    """Set the credentials for the given session.

    Args:
      credentials - The credentials for the given session.
    """
    self._session[_CREDENTIAL_KEY] = credentials
    self._ReCreateUserInfo(credentials)

  def _ReCreateUserInfo(self, cred=None):
    """Load and create the necessary user information.
    """
    if cred is None:
      cred = self.GetCredentials()
    user_info = FoursquareUser(cred.all_credentials.foursquare)
    self.SetUserInformation(user_info)
    return user_info

  def GetUserInformation(self):
    """Returns information pertinent to the current user.
    """
    if _USER_INFO_KEY in self._session:
      return self._session[_USER_INFO_KEY]
    return self._ReCreateUserInfo()

  def SetUserInformation(self, user_info):
    """Set the user information in the session.

    Args:
      user_info - The user information object containing the information
                  related to this user.
    """
    self._session[_USER_INFO_KEY] = user_info

