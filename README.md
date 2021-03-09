## django-orm-watching-storage

### Описание 
Проект к курсу [Знакомство с Django: ORM ](https://dvmn.org/modules/django-orm/) 1 и 2 уроки
### Установка
1. Склонировать репозиторий
2. Создать виртуальное окружение. Версия Python >= 3.7. В проекте использовался Python 3.9.1. Файл .python-version, если устанавливаете через pyenv
3. Установить все зависимости: `pip install -r requirements.txt`  
4. Чтобы подключить интерфейс к базе данных, создайте файл .env и добавьте в него соотвествующие поля настроек доступа. Файл лежит в `project/`
```shell script
DB_HOST='put_here_your_database_host'
DB_PORT='put_here_your_db_port'
DB_NAME='put_here_db_nam'
DB_USER='put_here_db_user_name'
DB_PASSWORD='put_here_your_password'
SECRET_KEY='put_here_your_secret_key'
DEBUG='put_here_True_or_False'
```
> Для включения режима отладки поместите строку DEBUG=True в файл .env

### Запуск приложения
```python
python manage.py runserver 0.0.0.0:8000
``` 
