import xadmin

from .models import TableOne,TableTwo


class DataOneAdmin(object):
    list_display = ['project', 'area']
    search_fields = ['project', 'area']
    list_filter = ['project', 'area']


class DataTwoAdmin(object):
    list_display = ['project', 'area']
    search_fields = ['project', 'area']
    list_filter = ['project', 'area']


xadmin.site.register(TableOne,DataOneAdmin)
xadmin.site.register(TableTwo,DataTwoAdmin)