# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts})
    #print type(post_list)
    #print post_list
    
    return HttpResponse(t.render(c))

class CommentForm(ModelForm):
    class Meta:
	model = Comment
	exclude =['post']

@csrf_exempt
def post_detail(request,id,showComments=False):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
	comment = Comment(post=post)
	form = CommentForm(request.POST, instance=comment)
	if form.is_valid():
	    form.save()
	return HttpResponseRedirect(request.path)
    else:
	form = CommentForm()	

    
    comments = Comment.objects.filter(post=id)
    #response = 'comment : '
    #for b in Comment.objects.all():
	#response+=' '+str(b.body)+' |'
    #post_comment=Comment.objects.get(id=id)
    t = loader.get_template('blog/post_detail.html')
    c = Context({'post':post,'comments':comments, 'form':form})

    return HttpResponse(t.render(c))

    
def post_search(request, term):
    posts =Post.objects.filter(title__contains= term)
    
    t = loader.get_template('blog/post_search.html')
    c = Context({'posts':posts,'term':term})

    return HttpResponse(t.render(c))

def home(request):
    return render_to_response('blog/base.html',{}) 
