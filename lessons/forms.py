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


class Test2(forms.Form):
    question1 = forms.ChoiceField(choices=((1, "delete <назва вказівника>;"), (2, "int *(назва) = new int;"),
                                           (3, "<назва вказівника> = NULL;")),
                                  widget=forms.RadioSelect,
                                  label="Занулення відбувається командою: ")
    question2 = forms.ChoiceField(choices=((1, "not"), (2, "and"),
                                           (3, "xor"), (4, "or")),
                                  widget=forms.RadioSelect,
                                  label="~ - це побітова:")
    question3 = forms.ChoiceField(choices=((1, "-4"), (2, "4"), (3, "2"), (4, "-2")),
                                  widget=forms.RadioSelect,
                                  label="Якщо у=4, який результат умови:\n"
                                        "If (y >3 && y < 10) x = sqrt(y);\n"
                                        "else x = abs (y);")
    question4 = forms.ChoiceField(choices=((1, "безумовного переходу"), (2, "виходу з команди"), (3, "вибору"), (4, "?")),
                                  widget=forms.RadioSelect,
                                  label="Break – це команда: ")
    required_css_class = "test-form"


class Test3(forms.Form):
    question1 = forms.MultipleChoiceField(choices=((1, "for"), (2, "else"), (3, "do-while"), (4, "while"), (5, "if")),
                                          widget=forms.CheckboxSelectMultiple,
                                          label="Команди циклу у мові С++ (оберіть всі можливі варіанти):")

    question2 = forms.ChoiceField(choices=((1, "6"), (2, "3"),
                                           (3, "5"), (4, "Команда не виконається.")),
                                  widget=forms.RadioSelect,
                                  label="Вкажіть результат виконання коду:\n"
                                        "int х = 6;\n"
                                        "while (х <= 5) { s = х*2/4;}")

    question3 = forms.MultipleChoiceField(choices=((1, "func(1, 2.3)"), (2, "func(8)"), (3, "func()"), (4, "func(‘’ ’’)")),
                                          widget=forms.CheckboxSelectMultiple,
                                          label="Якими способами ми можемо звернутись до функції та змінити її параметри, якщо:\n"
                                        "float func (int k = 5, float r = 3.1);")

    question4 = forms.MultipleChoiceField(choices=((1, "вказує компілятору, що значення змінної слід зберігати у регістрах"),
                                           (2, "застосовується як до локальних, так і до глобальних змінних"),
                                           (3, "для локальних змінних застосовується за замовчуванням"),
                                           (4, "під час повторного виклику функції змінна зберігає своє попереднє значення")),
                                          widget=forms.CheckboxSelectMultiple,
                                          label="Оберіть всі складові компоненту static:")
    question5 = forms.ChoiceField(choices=((1, "template <class Mytype>"), (2, "template class <Mytype>"),
                                           (3, "template <Mytype>"), (4, "template class “Mytype”")),
                                  widget=forms.RadioSelect,
                                  label="Вкажіть правильну сигнатуру шаблону функції:")
    required_css_class = "test-form"


class Test4(forms.Form):
    question1 = forms.ChoiceField(choices=((1, 'char name [5] = "Vlada"'), (2, "char name [5] = {'V', 'l', 'a', 'd', 'a'}"),
                                           (3, "int math[] = {2, 1 0, 5, 7, З};"), (4, "char name [5] = { Vlada }")),
                                  widget=forms.RadioSelect,
                                  label="Який з масивів не буде проініціалізовано: ")
    question2 = forms.ChoiceField(choices=((1, "копіює перших n символів рядка r2 в рядок r1 , команда"),
                                           (2, "команда з'єднання рядків r1, r2 в один рядок, результат присвоює змінній r1"),
                                           (3, "копіює символи з рядка r2 в рядок r1, команда"),
                                           (4, "до змінної r1 додає перших n символів рядка r2, команда")),
                                  widget=forms.RadioSelect,
                                  label="strcpy(r1, r2) – це функція для опрацювання рядків, яка:")
    question3 = forms.MultipleChoiceField(choices=((1, "інформація може складатися з даних різних типів"),
                                           (2, "скінчений набір даних одного типу"),
                                           (3, "опису списку використовують тип даних структура і вказівник"),
                                           (4, "складається з набору полів - даних різних типів")),
                                  widget=forms.CheckboxSelectMultiple,
                                  label="Оберіть правильні визначення, стосовно терміну «список»:")
    required_css_class = "test-form"