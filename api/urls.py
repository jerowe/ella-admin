from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.http.views import LogoutView, UserViewSet, GenePanelViewSet, UserGroupViewSet, ProfileViewSet, \
    StaffAppLoginView

router = routers.DefaultRouter()

router.register(r'user-groups', UserGroupViewSet, basename='user_groups')
router.register(r'users', UserViewSet, basename='users')
router.register(r'gene-panels', GenePanelViewSet, basename='gene_panels')
router.register(r'', ProfileViewSet, basename='profile')

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('staff-app-login/', StaffAppLoginView.as_view(), name='staff_app_login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^', include(router.urls)),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='user')),
]
