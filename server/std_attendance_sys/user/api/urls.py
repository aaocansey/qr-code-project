from django.urls import path
from user.views import CreateStudentView, LecturerCreateView, LecturerLoginView, LecturerQRCodeView, ListLecturersView

urlpatterns = [
    path('student', CreateStudentView.as_view(), name='students'),
    path('lecturer/signup', LecturerCreateView.as_view(), name='lecturer'),
    path('lecturer/login', LecturerLoginView.as_view(), name='lecturer-login'),
    path('lecturer/list', ListLecturersView.as_view(), name='lecturer-list'),
    path('lecturer/generate-qr-code', LecturerQRCodeView.as_view(), name='generate-qr-code')
    # path('lecturer/<int:pk>/generate_qr_code/', LecturerQRCodeView.as_view({'get': 'generate_qr_code'}), name='generate-qr-code')
]