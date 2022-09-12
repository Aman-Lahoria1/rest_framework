from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class CompanyRecord(models.Model):
    company_name=models.TextField(validators=[MinLengthValidator(5)])
    email_id=models.EmailField()
    company_code=models.CharField(max_length=5,unique=True)
    strength=models.PositiveIntegerField(default=0)
    website=models.URLField(max_length=100)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
