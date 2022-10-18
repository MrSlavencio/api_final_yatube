# Социальная сеть **YATUBE**


## Описание проекта

Социальная сеть позволяет публиковать посты с группами и без, комментировать их, подписываться на авторов поста.<br/>
Данный код предназначен для взаимодействия с социальной сетью через REST-API.

## Как развернуть проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrSlavencio/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

