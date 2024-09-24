import time


class User:
    """
    Класс для преобразования данных о пользователи
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return (f'{self.nickname}, ({self.age})')

class Video:
    """
    Класс для преобразования данных о видео
    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
class UrTube:
    """
    Класс для преобразования данных о пользователи и списка видео
    """

    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        if nickname in self.users and password in self.users:
            self.current_user = nickname

    def register(self, nickname, password, age):
        if self.log_in(nickname, password):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
            print(f"Пользователь {str(self.users[-1])} успешно зарегистрирован")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(str(video))
        return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18 and any(
                [video.adult_mode for video in self.videos if video.title == video_title]):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for video in self.videos:
                if video.title == video_title:
                    print("Просмотр видео", video_title)
                    print("Время просмотра:", end=" ")
                    for sec in range(video.duration + 1):
                        print(sec, end=" ")
                        time.sleep(0)
                        print("Конец видео")
                    else:
                        print("Видео с таким названием не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

