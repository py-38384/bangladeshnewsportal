from .models import Category
def get_category(request):
    category = Category.objects.filter(highlighted=True)[0:5]
    return {'categorys':category}