from mapd.auth import credentials
from mapd.config import foursquare_settings
from mapd.util import net_util

import json

_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token?client_id=' \
    '%s&client_secret=%s&grant_type=authorization_code&redirect_uri=%s' \
    '&code=%%s' % (foursquare_settings.CLIENT_ID,
        foursquare_settings.CLIENT_SECRET,
        foursquare_settings.REGISTERED_REDIRECT_URL)

class AuthManager(object):
  """Base Class to manage the authentication of users to various channels.
  """

  def GetAuthorizationURL(self):
    """Unimplemented method to get the URL needed to initiate the
    authorization.
    """
    pass

  def HandleAuthorizationCallback(self, callback_params):
    """Unimplemeted method to handle incoming callbacks to complete
    authorization.
    """
    pass

class FoursquareAuthManager(AuthManager):
  """Handle authorization requests for FourSquare.
  """

  def AuthorizeUser(self, code):
    """Authorize the given user, once they have accepted us on Foursquare.

    Args:
      code - The code that foursquare gave us, during authorizing callback.

    Returns:
      Foursquare credentials of the given user.
    """
    access_token_url = _ACCESS_TOKEN_URL % code
    raw_json = net_util.GenericFetchUrl(access_token_url)
    if not raw_json:
      return None

    response = json.loads(raw_json.read())
    if 'access_token' in response:
      return credentials.FoursquareCredentials(response['access_token'])

    return None

  def GetAuthorizationURL(self):
    """Return the FourSquare URL that the user needs to be redirected to, to
    initiate the authorization process for FourSquare.

    Returns:
      The URL that the user needs to visit to begin their authorization on
      FourSquare.
    """
    return '%s?client_id=%s&response_type=code&redirect_uri=%s' % \
        (foursquare_settings.AUTH_URL, foursquare_settings.CLIENT_ID,
         foursquare_settings.REGISTERED_REDIRECT_URL)
