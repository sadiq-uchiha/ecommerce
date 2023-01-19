from rest_framework import viewsets,views,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product,Order,Inventory,Customer
from .serializers import ProductSerializer,InventorySerializer,CustomerSerializer,OrderSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        serializer.save(image=self.request.FILES['image'])
    
class UserproductView(APIView):
    allowed_methods = ('GET',)

    def get(self, request):
        data = Product.objects.all()
        return Response(data)

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerLoginView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        customer = Customer.objects.filter(email=email).first()
        if customer and customer.password == password:
            return Response({'token': customer.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)