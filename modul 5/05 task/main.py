import hashlib
import time


class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return

    def register(self, nickname: str, password: str, age: int):
        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует')
            return
        if nickname not in self.users:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        if self.current_user:
            self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        search_word_lower = search_word.lower()
        list_video_title = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return list_video_title

    def watch_video(self, title: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        video = next((i for i in self.videos if i.title == title), None)
        if not video:
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        for second in range(1, video.duration + 1):
            print(second, end=' ')
            time.sleep(0.01)
            video.time_now = second
        print("Конец видео")
        video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')