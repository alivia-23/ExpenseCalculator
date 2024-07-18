# import for django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense
"""
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # category choice field
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('bills', 'Bills'),
        ('others', 'Others')
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.amount}'
"""
class ExpenseTestCase(APITestCase):
    def setUp(self):
        # create 3 expenses
        Expense.objects.bulk_create([
            Expense(name="Food", amount=100, category="food"),
            Expense(name="Transport", amount=200, category="transport"),
            Expense(name="Bills", amount=300, category="bills"),
        ])
    
    def test_expenses_list(self):
        # test expense list
        response = self.client.get("/api/expenses/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_expenses_detail(self):
        # test expense detail
        response = self.client.get("/api/expenses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Food")
        self.assertEqual(response.json()["amount"], "100.00")
        self.assertEqual(response.json()["category"], "food")
    
    def test_expenses_create(self):
        # test expense create
        response = self.client.post("/api/expenses/", {
            "name": "Others",
            "amount": 400,
            "category": "others"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "Others")
        self.assertEqual(response.json()["amount"], "400.00")
        self.assertEqual(response.json()["category"], "others")
       
    def test_expenses_update(self):
        # test expense update
        response = self.client.put("/api/expenses/1/", {
            "name": "Food",
            "amount": 150,
            "category": "food"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Food")
        self.assertEqual(response.json()["amount"], "150.00")
        self.assertEqual(response.json()["category"], "food")
    
    def test_expenses_delete(self):
        # test expense delete
        response = self.client.delete("/api/expenses/1/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Expense.objects.all()), 2)
        self.assertRaises(Expense.DoesNotExist, Expense.objects.get, id=1)
        response = self.client.get("/api/expenses/2/")
        self.assertEqual(response.status_code, 200)
        

    def tearDown(self):
        # delete all expenses
        Expense.objects.all().delete()


