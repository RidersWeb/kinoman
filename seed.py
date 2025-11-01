from database import SessionLocal, init_db
from models import Movie

movies_data = [
    {
        "title": "Побег из Шоушенка",
        "description": "Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки.",
        "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
        "rating": 9.3
    },
    {
        "title": "Крёстный отец",
        "description": "Криминальная сага о нью-йоркской сицилийской мафиозной семье Корлеоне. Фильм охватывает период 1945-1955 годов.",
        "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
        "rating": 9.2
    },
    {
        "title": "Тёмный рыцарь",
        "description": "Бэтмен поднимает ставки в войне с криминалом. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от преступности.",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "rating": 9.0
    },
    {
        "title": "Список Шиндлера",
        "description": "Фильм рассказывает реальную историю загадочного Оскара Шиндлера, спасшего во время Второй мировой войны более тысячи евреев от гибели.",
        "poster_url": "https://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
        "rating": 9.0
    },
    {
        "title": "Властелин колец: Возвращение короля",
        "description": "Повествование о последней битве за Средиземье. Фродо и Сэм продолжают своё путешествие в Мордор, чтобы уничтожить Кольцо Всевластия.",
        "poster_url": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
        "rating": 8.9
    },
    {
        "title": "Pulp Fiction",
        "description": "Несколько историй из жизни различных персонажей переплетаются в неожиданную картину о преступности, искуплении и судьбе.",
        "poster_url": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
        "rating": 8.9
    },
    {
        "title": "Форрест Гамп",
        "description": "История жизни простого человека с благородным сердцем, чья невероятная судьба оказалась тесно переплетена с важнейшими событиями американской истории XX века.",
        "poster_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/c9k8MkFc9DM1KvfgCE0OCY7Gavp.jpg",
        "rating": 8.8
    },
    {
        "title": "Начало",
        "description": "Талантливый вор, специализирующийся на краже секретов из глубин подсознания во время сна, получает шанс на искупление.",
        "poster_url": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
        "rating": 8.8
    },
    {
        "title": "Матрица",
        "description": "Хакер Нео узнает страшную правду о реальности и своей роли в войне против машин.",
        "poster_url": "https://image.tmdb.org/t/p/w500/hv7o3VgfsairBoQFAawgaQ4cR1m.jpg",
        "rating": 8.7
    },
    {
        "title": "Гладиатор",
        "description": "Генерал римской армии вынужден стать гладиатором, чтобы отомстить за убийство своей семьи.",
        "poster_url": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
        "rating": 8.5
    }
]

def seed_database():
    init_db()
    db = SessionLocal()
    
    for movie_data in movies_data:
        movie = Movie(**movie_data)
        db.add(movie)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_database()