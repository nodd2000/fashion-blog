"""Добавляем тестовые данные в БД"""

from models.post import Post
from models.user import User
from models.theme import Theme


def add_some_data(session):
    user1 = User(username="maksimovv",
                 userpic="/static/userpics/maksimovv.png",
                 name="Виктор",
                 surname="Максимов"
                 )

    user2 = User(username="asevanaz",
                 userpic="/static/userpics/asevanaz.png",
                 name="Анна",
                 surname="Филатова"
                 )
    session.add(user1)
    session.add(user2)

    theme1 = Theme(theme_en='fashion', theme_ru='мода')
    theme2 = Theme(theme_en='art', theme_ru='искусство')
    theme3 = Theme(theme_en='photo', theme_ru='фото')
    session.add(theme1)
    session.add(theme2)
    session.add(theme3)

    session.flush()
    session.commit()

    post6 = Post(user_id=user2.id,
                 title="Кампания Saint Laurent от Юргена Теллера",
                 html="designed_posts/ysl-fw21.html",
                 main_photo="https://vision-assistant.netlify.app//img/ysl-fw21/saint-laurent-main.jpg",
                 theme_id=theme1.id)
    post5 = Post(user_id=user1.id,
                 title="Polar Night: Визуальная поэма об арктическом городе",
                 html="designed_posts/polar-night-mark.html",
                 main_photo="https://vision-assistant.netlify.app//img/polar-night-mark/polar-night-main.jpg",
                 theme_id=theme3.id)
    post4 = Post(user_id=user2.id,
                 title="Новая кампания Jil Sander посвящена близости и прикосновениям",
                 html="designed_posts/jil-sander-ss21.html",
                 main_photo="https://vision-assistant.netlify.app//img/jil-sander-ss21/jil-sander-main.jpg",
                 theme_id=theme1.id)
    post3 = Post(user_id=user1.id,
                 title="Самый дорогой художник современности Дэвид Хокни в объективе Mark Mahaney",
                 html="designed_posts/david-hockney.html",
                 main_photo="https://vision-assistant.netlify.app//img/david-hockney/david-hockney-main.jpg",
                 theme_id=theme2.id)
    post2 = Post(user_id=user1.id,
                 title="Stas Kalashnikov для alei journal",
                 html="designed_posts/alei-journal-stas.html",
                 main_photo="https://vision-assistant.netlify.app//img/alei-journal-stas/stas-kalashnikov-main.jpg",
                 theme_id=theme1.id)
    post1 = Post(user_id=user2.id,
                 title="Украинские фотографы Таня и Женя Постернак поучаствовали в проекте Helmut Lang",
                 html="designed_posts/helmut-lang-home-pasternak.html",
                 main_photo="https://vision-assistant.netlify.app//img/helmut-lang-home-pasternak/helmut-lang-main.jpg",
                 theme_id=theme1.id)

    session.add(post1)
    session.add(post2)
    session.add(post3)
    session.add(post4)
    session.add(post5)
    session.add(post6)

    session.flush()
    session.commit()
