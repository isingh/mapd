"""Network related utility functions.
"""
import cStringIO as StringIO
import json
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

def GetJsonFromUrl(url):
  """Retrieves the URL and tries to parse the JSON from the response.

  Args:
    url - The URL that needs to be fetched.

  Returns:
    The JSON dict containing the reply. None if there was an error in parsing
    or the url couldnt be retreived.
  """
  raw_json = GenericFetchUrl(url)
  try:
    if raw_json:
      return json.loads(raw_json.read())
  except:
    logging.error('Error retreiving URL: %s' % url)
  return None

