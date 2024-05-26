"""
URL configuration for musiclab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from testsapp.views import *
from myauth.views import RegistrationView, LogoutView, CustomTokenObtainPairView, CustomUserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/testlist/', TestAPIList.as_view()),
    path('api/v1/test/<int:id>/', TestAPIRetrieve.as_view()),
    path('api/v1/test/<int:test_id>/questions/<int:question_index>/', TestTextQuestionDetailView.as_view(), name='test_question_detail'),
    path('api/v1/question/<int:question_id>/answers/', TestAnswerListView.as_view(), name='question_answers_list'),
    path('api/v1/user_test_answers/', UserTestAnswerCreateView.as_view(), name='user_test_answer_create'),
    path('api/v1/register/', RegistrationView.as_view(), name='register'),
    path('api/v1/logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/users/', CustomUserListView.as_view(), name='user-list'),

    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # type: ignore
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
