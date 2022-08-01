class Application:

    def __init__(self, name: str, blocked: bool = False) -> None:
        self.name = name
        self.blocked = blocked

class AppStore:

    def __init__(self) -> None:
        self.apps = {}

    def add_application(self, app: Application) -> None:
        self.apps[app.name] = app.blocked

    def remove_application(self, app: Application) -> None:
        self.apps.pop(app.name)

    def block_application(self, app: Application) -> None:
        app.blocked = True

    def total_apps(self) -> int:
        return len(self.apps)


