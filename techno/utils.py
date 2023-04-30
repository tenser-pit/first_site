from .models import *

menu = [{'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        {'title': '', 'url_name': ''},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.all()
        # goods = Techno.objects.all()
        # context['cats'] = cats
        # context['goods'] = goods
        return context
