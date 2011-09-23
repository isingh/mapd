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

    Args:
      access_token - The access token given by Foursquare for this user.
    """
    self._credentials.foursquare = FoursquareCredentials(access_token)

  def SetFoursquareCredentials(self, foursquare_cred):
    """Set the credentials for foursquare in the given credentials.

    Args:
      foursquare_cred - Foursquare credentials.
    """
    self._credentials.foursquare = foursquare_cred

  @property
  def is_authorized(self):
    """Check if the user is logged in, or not.
    """
    if self._credentials.foursquare and \
        self._credentials.foursquare.access_token:
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
  def access_token(self):
    return self._access_token
