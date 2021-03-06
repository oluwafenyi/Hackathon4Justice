
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from freedeon.views import APIRootView
from auth.views import CustomTokenObtainPairView as TokenObtainPairView
from reports.routers import router as reports_router
from accounts.routers import router as accounts_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', APIRootView.as_view(), name='api-root'),
    path('api/', include(reports_router.urls)),
    path('api/', include(accounts_router.urls)),
]
