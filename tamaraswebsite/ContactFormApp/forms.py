from django.forms import ModelForm
from models import Person, City, Country
from django import forms
from django.forms.models import inlineformset_factory


class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['first_name','last_name','gender','address','zipcode','email','cc_myself','phone','subject','inquiry',]
		
		def clean(self):
			cleaned_data = self.cleaned_data
			
			cc_myself = cleaned_data.get("cc_myself")
			first_name = cleaned_data.get("first_name")
			last_name = cleaned_data.get("last_name")
			gender = cleaned_data.get("gender")
			address = cleaned_data.get("address")
			zipcode = cleaned_data.get("zipcode")
			email =cleaned_data.get("email")
			cc_myself = cleaned_data.get("cc_myself")
			phone = cleaned_data.get("phone")
			subject = cleaned_data.get("subject")
			inquiry = cleaned_data.get("inquiry")

		
		
PersonCountryFormSet = inlineformset_factory(Person, Country, extra=1, can_delete=False)
PersonCityFormSet = inlineformset_factory(Person, City, extra=1, can_delete=False)
