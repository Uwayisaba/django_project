from django.contrib.auth.models import User
from django.db import models
from team.models import Team

class Lead(models.Model):
    LOW='low'
    MEDIUM ='medium'
    HIGH ='high'
    
    CHOICE_PRIORITY =(
        (LOW,'low'),
        (MEDIUM,'medium'),
        (HIGH,'high')
    )
    NEW ='new'
    CONTACTED ='contacted'
    WON ='won'
    LOST ='lost'
    CHOICES_STATUS=(
        (NEW,'new'),
        (CONTACTED,'contacted'),
        (WON,'won'),
        (LOST,'lost'),   
    )

    team=models.ForeignKey(Team,related_name='leads',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    description =models.TextField(blank=True,null=True)

    priority=models.CharField(max_length=10,choices=CHOICE_PRIORITY,default=MEDIUM)
    status =models.CharField(max_length=10,choices=CHOICES_STATUS,default=NEW)
    converted_to_client =models.BooleanField(default=False)
    
    created_by=models.ForeignKey(User,related_name='leads',on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    image=models.FileField(upload_to="images/",blank=True)

    class Meta:
        ordering=('name',)
        
    def __str__(self):
        return self.name
