from typing import Callable, Optional


class Handler:

    def __init__(self, methods: tuple = ("GET",)) -> None:
        self.__methods = methods

    def __call__(self, func: Callable) -> Callable:
        def wrapper(request: dict, *args, **kwargs) -> Optional[str]:
            allowed_methods = self.__methods
            method = request.get("method", "GET")
            if method not in allowed_methods:
                return None
            else:
                return self.__getattribute__(method.lower())(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
            return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"

@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)    # GET: Сергей Балакирев
res = contact({"method": "POST", "url": "contact.html"})
print(res)    # None
res = contact({"url": "contact.html"})
print(res)    # GET: Сергей Балакирев