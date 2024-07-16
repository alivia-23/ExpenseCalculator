from django.db import models

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
