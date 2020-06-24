from django import forms

class DistForm(forms.Form):
  dist_name = forms.CharField(label="dist name", max_length=50)