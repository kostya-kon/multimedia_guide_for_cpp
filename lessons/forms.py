from django import forms


class Test1(forms.Form):
    question1 = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.RadioSelect, label="chose 1")
    question2 = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.RadioSelect, label="chose 2")
    question3 = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.RadioSelect, label="chose 3")
    required_css_class = "test-form"