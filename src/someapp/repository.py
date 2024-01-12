from django.core.paginator import Paginator, EmptyPage

from someapp.models import SomeModel


class SomeModelRepository:
    def get_items(self):
        return SomeModel.objects.all()
