from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView
import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('send/',accounts.views.send,name='send' ),
    path('get_expense/',accounts.views.get_expenses, name='get_expense'),
    path('delete/',accounts.views.delete,name='delete' ),
    path('sort_by_date/',accounts.views.sort_by_date,name='sort_by_date' ),
    path('sort_by_ammount_ascending/',accounts.views.sort_by_ammount_ascending,name='sort_by_ammount_ascending' ),
    path('sort_by_ammount_descending/',accounts.views.sort_by_ammount_descending,name='sort_by_ammount_descending' ),
    path('back_to_home',accounts.views.back_to_home,name='back_to_home'),
]

