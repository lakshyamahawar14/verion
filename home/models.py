from django.db import models

# Create your models here.
class Code(models.Model):
    testbench = models.CharField(max_length=120)
    code = models.TextField()

    def __str__(self):
        return self.testbench