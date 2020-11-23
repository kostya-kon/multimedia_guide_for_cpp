from django import forms


class Test1(forms.Form):
    question1 = forms.ChoiceField(choices=((1, "Три змінні цілого типу"), (2, "Одна змінна цілого типу та дві дійсного"),
                                           (3, "Три змінні дійсного типу"), (4, "Одна змінна дійсного типу та дві цілого")),
                                  widget=forms.RadioSelect,
                                  label="int х, у;\n float h;\n У даних строках оголошується:")
    question2 = forms.ChoiceField(choices=((1, "Логічний"), (2, "Символьний"),
                                           (3, "Застосовується до функцій"), (4, "Типована стала")),
                                  widget=forms.RadioSelect,
                                  label="Char – це тип:")
    question3 = forms.ChoiceField(choices=((1, "«І»"), (2, "«АБО»"), (3, "«НЕ»")),
                                  widget=forms.RadioSelect,
                                  label="&&-логічний знак операції:")
    question4 = forms.ChoiceField(choices=((1, "7"), (2, "12"), (3, "81"), (4, "64")),
                                  widget=forms.RadioSelect,
                                  label="Порахуйте функцію pow(3,4):")
    required_css_class = "test-form"