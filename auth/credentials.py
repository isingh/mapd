from bunch import Bunch

class MapdCredentials(object):
  """Credentials to access various functionalities on Mapd
  """
  def __init__(self):
    """Initialize the credentials for this user.
    """
    # Currently we support only Foursquare, but we should be able to store
    # the credentials from various providers.
    self._credentials = Bunch(foursquare=None)

  def AddFoursquareAccess(self, access_token):
    """Add this user's foursquare credentials.
    """
    self._credentials.foursquare = FoursquareCredentials(access_token)

  @property
  def is_authorized(self):
    """Check if the user is logged in, or not.
    """
    if self._credentials.foursquare and \
        hasattr(self._credentials.foursquare, 'access_token'):
      return True
    return False

  @property
  def all_credentials(self):
    """Get all the credentials from all the providers.
    """
    return self._credentials

class FoursquareCredentials(object):
  """Credentials of a logged in user to access foursquare.
  """

  def __init__(self, access_token=None):
    """Constructor to initialize Foursquare details.
    """
    self._access_token = access_token

  @property
  def acces_token(self):
    return self._access_token
