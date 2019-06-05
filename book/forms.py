from django.forms import ModelForm
from book.models import Profile

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('bio',)