
import django_filters
from .models import Paper


class PaperFilter(django_filters.rest_framework.FilterSet):

    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Paper
        fields = ['name']