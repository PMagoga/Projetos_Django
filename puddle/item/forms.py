from django import forms

from .models import Item

INPUTED_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ("category", 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUTED_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUTED_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUTED_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUTED_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUTED_CLASSES
            })
        }