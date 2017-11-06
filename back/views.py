from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Category, Document, PublicDocument, Tag, Note
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType


# Create your views here.

def index(request):
    return render(request, 'back/index.html')
    
def icons(request):
    return render(request, 'back/icons.html')
    
def category_documents(request, category_id):
    if(request.user.has_perm('back.view_private_document')):
        query_results = Document.objects.all().filter(category_id=category_id)
        #children = query_results.all().Tag.objects.get_queryset_ancestors(item.tags.all(), True)
        tmp = []
        # for item in query_results.all():
            # print(item.tags.all(), Tag.objects.get_queryset_ancestors(item.tags.all()))
            # tmp.append(list(Tag.objects.get_queryset_ancestors(item.tags.all(), True)))
        
    else:
        query_results = PublicDocument.objects.all().filter(category_id=category_id)
        tmp = []
        # for item in query_results.all():
            # print(item.tags.all())
            # tmp.append(Tag.objects.get_queryset_ancestors(item.tags.all(), True))
    children = tmp
    # print(children, type(children))
    #output = ', '.join([d for d in query_results]).order_by('-pub_date')
    #query_results = query_results, children
    context = {'category_name' : query_results.all()[0].category.name, 'category_documents' : query_results.all()}
    return render(request, 'back/category_documents.html',context)
    
def connect(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Yes !")
    else:
        return HttpResponse("Nope !")
        
def document_download(request, document_id):
    document = Document.objects.get(id=document_id)
    document.stat += 1
    document.save()
    fsock = document.file.open(mode='r')
    
    response = HttpResponse(fsock, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=%s.pdf" % \
                                     (document.name)
    return response
    
    
def document_notes(request, document_id):
    query_results = Note.objects.all().filter(document_id=document_id)
    print(query_results)
    context = {'document_notes' : query_results}
    return render(request, 'back/document_notes.html',context)