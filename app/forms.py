from django import forms
from .models import Details

#Create your forms here.

class detailsForm(forms.ModelForm):

    #specify model used.
    class Meta:
        model= Details
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['productName'].widget.attrs.update({'class':'product-name','readonly':True})
        self.fields['quantity'].widget.attrs.update({'class':'quantity'})
        self.fields['price'].widget.attrs.update({'class':'total','readonly':True})