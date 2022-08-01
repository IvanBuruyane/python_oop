class AppVK:

    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:

    def __init__(self, memory_max: int) -> None:
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:

    def __init__(self, phone_list: dict) -> None:
        self.name = "Phone"
        self.phone_list = phone_list


class SmartPhone:

    def __init__(self, model: str) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app: [AppVK, AppPhone, AppYouTube]) -> None:
        app_list = list(map(type, self.apps))
        if type(app) not in app_list:
            self.apps.append(app)

    def remove_app(self, app: [AppVK, AppPhone, AppYouTube]) -> None:
        self.apps.remove(app)


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)