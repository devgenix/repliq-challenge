# Swagger docs
from Repliq.schema_generator import CustomSchemaGenerator
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Django imports
from django.contrib import admin
from django.urls import path, include

# Own Imports

# Swagger docs
schema_view = get_schema_view(
    openapi.Info(
        title="Repliq Challenge API",
        default_version="1.0",
        description="Django app to track corporate assets such as phones, tablets, laptops and other gears handed out to employees",
        contact=openapi.Contact(email="challenge@repliq.com"),
    ),
    public=True,
    generator_class=CustomSchemaGenerator,
)

urlpatterns = [
    path('restricted/admin/', admin.site.urls, name='root_admin'),
    path('api/', include('Assets.urls')),
    path('api/auth/', include('users.urls')),

    # Documentation by swagger
    path(
        "api/auth/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="api_docs",
    ),

    # Documentation by redoc to be rendered on home page
    path(
        "",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="api_redocs",
    ),
]
