import xadmin

from .models import TableOne,TableTwo,SystemType,TypeImage


class DataOneAdmin(object):
    list_display = ['project', 'area']
    search_fields = ['project', 'area']
    list_filter = ['project', 'area']


class DataTwoAdmin(object):
    list_display = ['project', 'area']
    search_fields = ['project', 'area']
    list_filter = ['project', 'area']


class SystemTypeAdmin(object):
    list_display = ['types']
    search_fields = ['types']
    list_filter = ['types']


class TypeImageAdmin(object):
    list_display = ['the_type', 'image']
    search_fields = ['the_type', 'image']
    list_filter = ['the_type', 'image']


xadmin.site.register(TableOne,DataOneAdmin)
xadmin.site.register(TableTwo,DataTwoAdmin)
xadmin.site.register(SystemType,SystemTypeAdmin)
xadmin.site.register(TypeImage,TypeImageAdmin)
