from django.http import HttpResponse

def auth_handler(request, extra):
  print '1'
  print extra
  return HttpResponse('a')
