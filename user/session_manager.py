from bunch import Bunch
from mapd.auth import credentials

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
    return self._session.get('credentials', credentials.MapdCredentials())

  def SetCredentials(self, credentials):
    """Set the credentials for the given session.

    Args:
      credentials - The credentials for the given session.
    """
    self._session['credentials'] = credentials
