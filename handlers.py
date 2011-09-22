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
  if code is None:
    return HttpResponse('Got code: %s.' % code)

  auth_mgr = auth_manager.FoursquareAuthManager()
  return HttpResponse('Got value: %s' % auth_mgr.AuthorizeUser(code))

def DefaultHandler(request):
  """Default handler for all pages that do not match any registered handler.
  """
  mapd_credentials = SessionManager.GetCredentials(request)
  if not mapd_credentials.is_authorized:
    return HttpResponseRedirect(auth_manager.FoursquareAuthManager()
        .GetAuthorizationURL())
  context = Context({
    'is_authorized' : mapd_credentials.is_authorized,
  })

  return HttpResponse(loader.get_template('base.html').render(context))

def ViewHandler(request):
  """Handle request to view information.
  """
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

