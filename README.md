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


## Rest-API

Документацию по API Вы можете прочитать, запустив проект(```
python3 manage.py runserver
```) по ссылке ```/redoc/```

**Пример API-запросов**
Получение постов с 2 по 4

*Request:*
```GET /api/v1/posts/?limit=2&offset=4```

*Respond:*
```
200 OK
{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=6",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "results": [
        {
            "id": 5,
            "author": "Автор поста",
            "text": "Текст поста",
            "pub_date": "2022-10-16T08:55:27.883702Z",
            "image": null,
            "group": null
        },
        {
            "id": 6,
            "author": "Автор поста",
            "text": "Текст поста",
            "pub_date": "2022-10-16T10:51:35.585324Z",
            "image": null,
            "group": null
        }
    ]
}
```

