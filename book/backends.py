from registration.backends.simple.views import RegistrationView
# my new reg view, subclassing RegistrationView from our plugin
class MyRegistrationView(RegistrationView):
# the named URL that we want to redirect to after
# successful registration
	success_url = 'registration_create_thing'