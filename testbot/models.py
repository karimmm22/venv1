from django.db import models
from datetime import datetime
# Create your models here.

class info_user(models.Model) :
    
    hostname = models.CharField(max_length=170)
    ip = models.CharField(max_length=170)
    user_agent = models.CharField(max_length=170)
    id_user =models.DateTimeField(default = datetime.now )
    
    def __str__(self) :
        return self.user_agent