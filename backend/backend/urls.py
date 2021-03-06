"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from accounts.urls import router as accounts_router
from event.urls import router as event_router
from program.urls import router as program_router
from schedule.urls import router as schedule_router

from accounts.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(event_router.registry)
router.registry.extend(program_router.registry)
router.registry.extend(schedule_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/", include(router.urls)),
]
