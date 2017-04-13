from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from officialSite.models import Gallery, Client_showcase

# Create your views here.

def index(request):
    return render(request, 'officialSite/index.html')

def about(request):
    return render(request, 'officialSite/about.html')

def gallery(request):
    photo_list = Gallery.objects.all()
    paginator = Paginator(photo_list, 9)

    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request, 'officialSite/gallery.html', {'photos': photos})

def clientshowcase(request):
    clientshowcase_list = Client_showcase.objects.all()
    paginator = Paginator(clientshowcase_list, 2)

    page = request.GET.get('page')
    try:
        clientshowcases = paginator.page(page)
    except PageNotAnInteger:
        clientshowcases = paginator.page(1)
    except EmptyPage:
        clientshowcases = paginator.page(paginator.num_pages)
    #
    # if request.method == 'POST':
    #     tag = request.POST['tag_id']
    #     number_of_likes = request.POST['Number of likes']
    #     number_of_dislikes = request.POST['Number of dislikes']
    #
    #     current_edit = Client_showcase.objects.get(pk=tag)
    #     current_edit.number_of_likes = number_of_likes + 1
    #     current_edit.number_of_dislikes = number_of_dislikes + 1
    #     current_edit.save()
    #     return render(request, 'officialSite/clientshowcase.html', {'clientshowcase': clientshowcases})

    return render(request, 'officialSite/clientshowcase.html', {'clientshowcase': clientshowcases})

def contacts(request):
    return render(request, 'officialSite/contacts.html')

def carousel(request):
    return render(request, 'officialSite/carousel.html')

def clients(request):
    return render(request, 'officialSite/Clients.html')
