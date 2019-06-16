from django.forms import ModelForm
from .models import Profile
from .models import Book

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'image',)

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'text',)