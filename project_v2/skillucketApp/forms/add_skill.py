from django import forms
from ..models.bucket_skill import BucketSkill


class BucketSkillForm(forms.ModelForm):
    class Meta:
        model = BucketSkill
        fields = ['skill', 'target_date', 'notes']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'})
        }

