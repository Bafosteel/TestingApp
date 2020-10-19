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
