# TestingApp
Данное приложение представляет из себя систему для проведения различных тестов. Также в данном приложение доступна регистрация и авторизация пользователя.
## Установка
Наберите в консоли следущее:
```
git clone ulr проекта
cd TestingApp
myvenv\Scripts\activate.bat
cd sitefortesting
pip -r install requirements.txt
python manage.py makemigrations quiz
python manage.py migrate quiz
python manage.py createsuperuser
```
Возможно также потребуется сбросить миграции.

Затем следует зайти в settings.py и заменить хост, юзера и пароль на желаемые. Данная операция требуется для корректной работы модуля регистрации.
```
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '***********@gmail.com'
EMAIL_HOST_PASSWORD = '***************'
EMAIL_PORT = 587
```
Так как приложение пока работает на локалке, то следует разрешить доступ ненадежным приложениям к google(если используется он) на время работы модуля регистрации.
