"""Network related utility functions.
"""
import cStringIO as StringIO
import logging
import urllib2

def GenericFetchUrl(url):
  """Fetch the given url, and return the raw output as a string.

  Args:
    url - The URL that needs to be retrieved.

  Returns:
    The string representation of the web page retrieved.
  """
  response = None
  try:
    response = urllib2.urlopen(url)
  except urllib2.URLError as e:
    logging.error('Unable to fetch URL: %s because: %s' % (url, e))
  except urllib2.HTTPError as e:
    logging.error('Error while fetching URL: %s, with error code: %s' %
        (url, e))

  if response:
    return StringIO.StringIO(response.read())
  return None
