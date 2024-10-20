import hashlib
import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password: str) -> str:
        """Хэширует пароль с использованием SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password and self.age == other.age
        return False


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration  # в секундах
        self.time_now = 0  # Начальное время просмотра
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}s, adult_mode={self.adult_mode})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False


class UrTube:
    def __init__(self):
        self.users = []       # Список объектов User
        self.videos = []      # Список объектов Video
        self.current_user = None  # Текущий пользователь

    def register(self, nickname: str, password: str, age: int):
        """Регистрирует нового пользователя."""
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Вход выполняется автоматически после регистрации
        print(f"Пользователь {nickname} успешно зарегистрирован и вошёл в систему.")

    def log_in(self, nickname: str, password: str):
        """Авторизует пользователя."""
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошёл в систему.")
                return
        print("Неверный никнейм или пароль.")

    def log_out(self):
        """Выход пользователя из системы."""
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("Нет пользователя, который мог бы выйти.")

    def add(self, *videos: Video):
        """Добавляет видео в платформу, если с таким названием ещё нет."""
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено на платформу.")
            else:
                print(f"Видео '{video.title}' уже существует на платформе.")

    def get_videos(self, search_word: str):
        """Возвращает список названий видео, содержащих поисковое слово (без учёта регистра)."""
        search_word_lower = search_word.lower()
        matched_videos = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return matched_videos

    def watch_video(self, title: str):
        """Воспроизводит видео по названию с учётом условий."""
        # Проверка входа пользователя
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Поиск видео с точным совпадением названия
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            # Нет точного совпадения
            return

        # Проверка возрастного ограничения
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Воспроизведение видео
        print(f"Смотрим видео: {video.title}")
        for second in range(1, video.duration + 1):
            print(second, end=' ')
            time.sleep(0.01)  # Уменьшенная задержка для демонстрации
            video.time_now = second
        print("Конец видео")
        video.time_now = 0  # Сброс времени после просмотра

    def __str__(self):
        return f"UrTube(Users: {len(self.users)}, Videos: {len(self.videos)}, Current User: {self.current_user})"

    def __repr__(self):
        return self.__str__()


# Код для проверки:
if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
    print(ur.get_videos('ПРОГ'))     # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение видео

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Пользователь уже существует
    print(ur.current_user)  # urban_pythonist

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')  # Ничего не происходит

    # Дополнительно: Выход из аккаунта
    ur.log_out()
    ur.watch_video(v1.title)  # Войдите в аккаунт, чтобы смотреть видео
