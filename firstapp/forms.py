from django import forms
from .models import Curriculum

class CurriculumForm(forms.ModelForm):
  
  class Meta:
    model = Curriculum
    fields = ['name']
