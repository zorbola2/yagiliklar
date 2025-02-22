from django import forms



class RegisterForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Ism kiriting'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Familiyangizni kiriting'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Email kiriting'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Login kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Parol kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password2', 'placeholder': 'Parolni takrorlang'}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Login kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Parol kiriting'}))

