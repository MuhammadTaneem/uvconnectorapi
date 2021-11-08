
from rest_framework import viewsets, permissions, status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import CustomPagination


class StudentListViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_id')
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('full_name','student_id','nick_name','blood_group' )
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny ]
    pagination_class = CustomPagination





