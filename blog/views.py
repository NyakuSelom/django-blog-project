# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

def post_detail(request,id,showComments=False):
    post_detail=Post.objects.get(id=id)
    response = 'comment : '
    for b in Comment:
	response+= str(b.title)
    #post_comment=Comment.objects.get(id=id)

    return HttpResponse('<h3>'+str(post_detail)+'</h1>'+'</p>'+response)

    
def post_search(request, term):
    post_search =Post.objects.filter(title__contains= term)

    return HttpResponse(post_search)

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete S3n?') 
