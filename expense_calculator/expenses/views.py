from rest_framework.viewsets import ModelViewSet

from .serializers import ExpenseSerializer
from .models import Expense

class ExpenseViewSet(ModelViewSet):
    '''
    provides CRUD operations for Expense model
    '''
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
