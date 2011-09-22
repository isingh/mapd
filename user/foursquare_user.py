from mapd.user import BaseUser

class FoursquareUser(BaseUser):
  """A user with foursquare credentials.
  """

  def __init__(self, credentials):
    """Constructor for a FoursquareUser.

    Args:
      credentials - The credentials that can be used to uniquely idenity this
                    user on foursquare.
    """
    self._credentials = credentials

  @property
  def name(self):
    # TODO(inder) - Query user information from Foursquare from either the db
    # or from Foursquare servers.
    return 'not implemented'
