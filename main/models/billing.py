from main.models.base import *


class Billing(BaseModel):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50)
    street_address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    other_notes = models.TextField(null=True, blank=True)
    payment = models.CharField(max_length=100)
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name
