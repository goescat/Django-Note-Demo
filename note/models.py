# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    ''' Note : model of Note object
            Data:
                content - note content
                owner - note owner
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=100, help_text='Enter your title')
    content = models.TextField(max_length=1000, help_text='Enter your note')
    owner = models.ForeignKey(User, related_name='note_owner', verbose_name='Owner', on_delete=models.CASCADE)
