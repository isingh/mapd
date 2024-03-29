import logging

from bunch import Bunch

from mapd.config import foursquare_settings
from mapd.utils import net_utils

_LATEST_CHECINS_LIMIT = 25

def MakeAPICall(url):
  """Makes a generic API call to Foursquare and verifies the response.

  Args:
    url - The URL that needs to be called.

  Returns:
    Tuple containing (success, code, raw_json)
  """
  raw_json = net_utils.GetJsonFromUrl(url)
  if raw_json is None:
    return (False, None, None)

  code = None
  success  = True
  response = None
  try:
    code = raw_json['meta']['code']
    response = raw_json['response']
  except:
    success = False
  return (success, code, response)

def GetLatestCheckins(token, limit=_LATEST_CHECINS_LIMIT):
  """Get the latest checkins for the user, using the given token.

  Args:
    token - The token to be used for authenticating.
    limit - The number of checkins that need to be fetched.
  Returns:
    A list of all the checkins.
  """
  if token is None:
    return []
  fetch_url = foursquare_settings.API_URL + '/users/self/checkins'
  fetch_url += ('?oauth_token=%s&limit=%s' % (token, limit))
  (success, code, response) = MakeAPICall(fetch_url)
  if not success or code != 200:
    logging.error('Unable to retreive the checkins for the user')
    return []
  all_checkins = {}
  for curr_checkin in response['checkins']['items']:
    try:
      venue_id = curr_checkin['venue']['id']

      # The user has already been to this venue.
      if venue_id in all_checkins.keys():
        all_checkins[venue_id].num_checkins += 1
        continue

      # We are seeing this venue for the first time. Initialize and add.
      checkin = Bunch()
      checkin.num_checkins = 1
      checkin.venue_name = curr_checkin['venue']['name']
      checkin.venue_location = Bunch()
      checkin.venue_location.city = '%s, %s' % \
          (curr_checkin['venue']['location']['city'],
          curr_checkin['venue']['location']['state'])
      checkin.venue_location.lat = curr_checkin['venue']['location']['lat']
      checkin.venue_location.lng = curr_checkin['venue']['location']['lng']
      all_checkins[venue_id] = checkin
    except:
      pass
  return all_checkins.values()

