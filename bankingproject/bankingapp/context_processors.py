from .models import District, Branch


def menu_links(request):
    links = District.objects.all()
    return dict(links=links)


def branch_links(request):
    br_links = Branch.objects.all()
    return dict(br_links=br_links)
