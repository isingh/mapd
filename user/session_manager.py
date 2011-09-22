from bunch import Bunch
from mapd.auth import credentials

class SessionManager(object):
  """Manage and retrieve data from the current session
  """

  @staticmethod
  def GetCredentials(request):
    """Get the credentials from the given request session.

    Args:
      request - Http Request, from whose session we want the credentials.
    """
    return request.session.get('credentials', credentials.MapdCredentials())
