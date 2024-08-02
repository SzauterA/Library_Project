from typing import Any
from django.contrib import admin

class PageRangeFilter(admin.SimpleListFilter):
    title = "Page Range"
    parameter_name = "page_range"

    def lookups(self, request, model_admin):
        return [
            ('0-50', '0-50'),
            ('51-100', '51-100'),
            ('101-200', '101-200'),
            ('201-500', '201-500'),
            ('501-1000', '501-1000'),
            ('1001+', '1001+'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '0-50':
            queryset = queryset.filter(pages__lte=50)
        elif self.value() == '51-100':
            queryset = queryset.filter(pages__range=[51, 100])
        elif self.value() == '101-200':
            queryset = queryset.filter(pages__range=[101, 200])
        elif self.value() == '201-500':
            queryset = queryset.filter(pages__range=[201, 500])
        elif self.value() == '501-1000':
            queryset = queryset.filter(pages__range=[501, 1000])
        elif self.value() == '1001+':    
            queryset = queryset.filter(pages__gte=1001)
        
        return queryset