from django.urls import include, path
from rest_framework import routers
from .views import StudentListViewSet

router = routers.DefaultRouter()
router.register('', StudentListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('image/', PostImageViewSet.as_view()),
    # path('image/<int:pk>/', PostImageViewSet.as_view()),

]