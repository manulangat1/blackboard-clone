from rest_framework.routers import DefaultRouter
from .views import UserAPI,LoginAPI,AssignmentView,RegisterView

from django.conf.urls import url,include
from knox import views as knox_views

router = DefaultRouter()
# router.register(r'register',RegisterView,base_name='register')
router.register(r'ass',AssignmentView)

# 
urlpatterns = [
    url(r'api/auth',include('knox.urls')),
    url(r'^register/',RegisterView.as_view()),
    url(r'^login/',LoginAPI.as_view()),
    url(r'^user/',UserAPI.as_view()),
    url(r'^logout/',knox_views.LogoutView.as_view(),name="logout"),
]
urlpatterns += router.urls