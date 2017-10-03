from django.shortcuts import render_to_response

def home(request):
#     return render_to_response('home/home.html')
     return render_to_response('admin/base_site.html')
