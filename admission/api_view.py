from rest_framework.viewsets import ModelViewSet
from .models import TeachersInfoModel, UserAdmission
from .serializers import AdmissionSerializer, TeachersInfoSerializer


class AdmissionModelViewSet(ModelViewSet):
    queryset = UserAdmission.objects.all()
    serializer_class = AdmissionSerializer


class TeachersInfoModelViewSet(ModelViewSet):
    queryset = TeachersInfoModel.objects.all()
    serializer_class = TeachersInfoSerializer
