class RenderList:

    def __init__(self, type_list: str) -> None:
        self.type_list = "ol" if type_list == "ol" else "ul"

    def __call__(self, lst: list[str], *args, **kwargs) -> str:
        list_items = "</li>\n<li>".join(lst)
        return f"<{self.type_list}>\n<li>{list_items}</li>\n</{self.type_list}>"

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("fefe")
html = render(lst)
print(html)