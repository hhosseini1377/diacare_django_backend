from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from account.views import VerifyEmail, CustomObtainTokenPairView
from . import settings

urlpatterns = [
                  path('admin/postgres-metrics/', include('postgres_metrics.urls')),
                  path('admin/', admin.site.urls),
                  path('api/token/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/v1/verify-email/', VerifyEmail.as_view(), name='verify-email'),
                  path('api/v1/account/', include('account.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
