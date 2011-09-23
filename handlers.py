"""Collection of handlers to serve incoming requests coming to the server.
"""

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import loader
from django.template import Template

from mapd.auth import auth_manager
from mapd.user.session_manager import SessionManager

def _GetQueryParam(request, query_param):
  """Get the given query string from the incoming request.

  Args:
    request - The HttpRequest coming in to the server.
    query_param - The query string that needs to be retrieved.

  Returns:
    String containing the value of the query param, else None.
  """
  if query_param in request.GET:
    return request.GET[query_param]
  return None

def AuthHandler(request):
  """Handle the authentication requests coming in.
  """
  code = _GetQueryParam(request, 'code')
  session_manager = SessionManager(request.session)

  if code is None:
    return HttpResponse('Got code: %s.' % code)

  foursquare_cred = auth_manager.FoursquareAuthManager().AuthorizeUser(code)

  mapd_credentials = session_manager.GetCredentials()
  mapd_credentials.SetFoursquareCredentials(foursquare_cred)
  session_manager.SetCredentials(mapd_credentials)

  context = Context({
    'is_authorized' : foursquare_cred,
  })

  return HttpResponse(loader.get_template('base.html').render(context))

def DefaultHandler(request):
  """Default handler for all pages that do not match any registered handler.
  """
  session_manager = SessionManager(request.session)
  mapd_credentials = session_manager.GetCredentials()
  if not mapd_credentials.is_authorized:
    return HttpResponseRedirect(auth_manager.FoursquareAuthManager()
        .GetAuthorizationURL())

  user_info = session_manager.GetUserInformation()
  context = Context({
    'display_name' : user_info.name,
    'recent_checkins' : user_info.GetRecentCheckins(),
  })

  return HttpResponse(loader.get_template('index.html').render(context))

def ViewHandler(request):
  """Handle request to view information.
  """
  request.session.clear()
  return HttpResponse('Move along people, nothing to view here')

def UserRequestHandler(request):
  """Handle requests to add/view user pertinent information.
  """
  user_email = _GetQueryParam(request, 'user_email')
  if user_email:
    # Show user specific details
    return HttpResponse('Under construction')
  # Show the new user registration page
  return HttpResponse('New User Registration')

