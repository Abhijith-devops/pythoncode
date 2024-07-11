from .models import Category
def menu_links(requested):
    links=Category.objects.all()
    return dict(links=links)
