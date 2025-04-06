### API_Final_Yatube
API для проекта Yatube, содержащий в себе посты, комментарии к ним, а также возможность подписываться на интересующих вас авторов

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/TheRealestGinger/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

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

### Примеры запросов
'api/v1/posts/' (Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.):

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

'api/v1/posts/{id}/' (Получение публикации по id.):

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

'api/v1/posts/{post_id}/comments/' (Получение всех комментариев к публикации.):

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

'api/v1/posts/{post_id}/comments/{id}/' (Получение комментария к публикации по id.):
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

'api/v1/follow/' (Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.):

```
[
  {
    "user": "string",
    "following": "string"
  }
]
```