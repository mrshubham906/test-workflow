from rest_framework.views import APIView
from rest_framework.response import Response

from test_app.models import User


# Create your views here.


class CreateUserView(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            User.objects.create(name=name, email=email, password=password)
            return Response({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return Response({'error': 'Invalid request'}, status=400)


    def get(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                'name': user.name,
                'email': user.email
            })
        return Response({'data': data}, status=200)

