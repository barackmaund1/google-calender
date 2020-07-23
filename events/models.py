from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    start_time = models.DateTimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.DateTimeField(u'Final time', help_text=u'Final time')

    @property
    def get_html_url(self):
        url = reverse('events:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    

    