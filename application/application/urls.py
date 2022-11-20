from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Feed me fast API Doc",  # !
        default_version="v1",  # !
        description="API Doc",
        terms_of_service="http://google.com",
        contact=openapi.Contact(email="admin@fmf.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 权限类
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
