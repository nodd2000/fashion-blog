Запуск через docker-compose
```bash
docker-compose build
docker-compose up
```


Создание docker image
```bash
docker image build -t blog .
```

Запуск контейнера в интерактивном режиме
```bash
docker run -it -p 5000:5000 --name blog blog bash
```

Инициализация базы данных (в контейнере)
```bash
flask init-db
```

Добавление данных в БД (в контейнере)
```bash
python main.py
```

Запуск веб-приложения (в контейнере)
```bash
python app.py
```

Веб-приложение работает по адресу `0.0.0.0:5000`

```bash
docker build -t myimage .
```

* `/static/userpics/` - юзерпики пользователей
* `/templates/designed_posts/` - сверстанная часть отдельных постов
* `/templates/posts/post_base.html` - шаблон для страницы отдельного поста
* `/templates/posts/post_list.html` - шаблон для показа выбранных постов (передача через posts)
* `/templates/users/user_detail.html` - шаблон для показа постов отдельного юзера
* `/templates/users/user_list.html` - шаблон для показа всех пользователей
* `/templates/index_base.html` - шаблон для всех страниц сайта, header, footer

При создании пользователя указываются следующие данные:
* username="maksimovv"
* userpic="/static/userpics/maksimovv.png"
* name="Виктор"
* surname="Максимов"

При создании поста указываются следующие данные:
* user_id=user2.id
* title="Кампания Saint Laurent от Юргена Теллера"
* html="designed_posts/ysl-fw21.html"
* main_photo="https://vision-assistant.netlify.app//img/ysl-fw21/saint-laurent-main.jpg"
* theme_id=theme1.id



