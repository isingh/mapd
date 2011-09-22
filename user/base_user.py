

class BaseUser(object):
  """Base class to represent a user.
  """
  @property
  def name(self):
    raise Exception('Not implemented')
