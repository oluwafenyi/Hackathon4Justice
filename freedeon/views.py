
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):
    def get(self, request):
        return Response({
            'users': reverse('users-list', request=request),
            'reports': reverse('reports-list', request=request),
        })
