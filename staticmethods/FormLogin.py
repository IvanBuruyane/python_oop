from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        length = len(name)
        if length < 3 or length > 50:
            return False
        for symbol in name:
            if symbol not in cls.CHARS_CORRECT:
                return False
        return True

    def __init__(self, name, size=10):
        self.name = ""
        self.size = size
        if not self.check_name(name):
            raise ValueError('некорректное имя поля')
        else:
            self.name = name

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(TextInput):

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)