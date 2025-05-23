from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Allow logout via GET
class LogoutViewGET(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutViewGET.as_view(next_page='post_list'), name='logout'),
]
