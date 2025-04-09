from django import forms
from .models import AnalyzedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = AnalyzedImage
        fields = ['image']