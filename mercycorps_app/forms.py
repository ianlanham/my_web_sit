from django import forms


from .models import Person

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ('firstname', 'lastname', 'address', 'nationalid', 'phone', 'email', 'dob',)

    def is_duplicate_record(self):
        
        is_duplicate = False
        
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        dob = self.cleaned_data.get('dob')
        
        found_records =  Person.objects.filter(firstname__contains = firstname)
        
        
        
        return is_duplicate
        
        
        