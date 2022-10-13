from django.urls import path
from . import views

urlpatterns = [
    path('', views.direct_index, name='direct-index'),
    path('<int:pk>', views.direct_chat, name='direct-chat'),
]
