import django_filters
from django_filters import CharFilter, NumericRangeFilter, RangeFilter

from members.models import *



class MemberFilter(django_filters.FilterSet):
    # name = CharFilter(field_name="full_name", lookup_expr="icontains")
    gender = CharFilter(field_name="gender")
    occupation = CharFilter(field_name="occupation", lookup_expr='icontains')
    age = RangeFilter(field_name="age")

    class Meta:
        model = Member
        fields = ['gender', 'age', 'occupation']
        