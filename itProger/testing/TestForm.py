import pytest
# import form
from form import Form


## Вне функций создайте объект на основе класса Form. В объект при создании передавайте 2 параметра: логин и пароль;
tstForm = Form("Admin", "qwerty")
# tstForm2 = Form("BigPig", "qazwsx", "1@1.ru", "1.ru")

## Создайте функцию, что протестирует можем ли мы создать объект на основе класса Form передав в него 2 параметра. Такая функция лишь должна сверять корректно ли
@pytest.mark.form
def test_Form1():
    # tstForm1 = form.Form("Admin", "qwerty")
    assert (tstForm1.login, tstForm1.pwd) == ("Admin", "qwerty")

## Создайте аналогичную функцию, что протестирует можем ли мы создать объект на основе класса Form передав в него 4 параметра;
@pytest.mark.form
def test_Form2():
    tstForm = Form("BigPig", "qazwsx", "1@1.ru", "1.ru")
    assert (tstForm.login, tstForm.pwd, tstForm.email, tstForm.url) == ("BigPig", "qazwsx", "1@1.ru", "1.ru")

# Создайте функцию, что протестирует можно ли установить некорректный URL адрес веб-сайта в переменную url в классе Form.
# Для проверки корректного URL адреса используйте библиотеку requests, которую мы рассматривали ранее в уроке по парсингу веб-сайта.
## добавим возможность проверки по массиву данных
@pytest.mark.parametrize('url, res', [
    ('https://google.com/', True), ### рабочий url
    ('https://google1111111111111.com/', True), ### не рабочий url
    ('https://itproger.com/', True), ### рабочий url
])
@pytest.mark.tstLink
def test_tstLink(url, res):
    assert tstForm.url(url) == res




