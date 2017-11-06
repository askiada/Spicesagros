from django.shortcuts import render
from .models import Category

def categories(request):
    query_results = Category.objects.all()
    # tmp = []
    # for item in query_results.all():
        # print(item.tags.all())
        # tmp.append(Category.objects.get_queryset_ancestors(item, True))

    context = {'list_categories' : query_results}
    return context