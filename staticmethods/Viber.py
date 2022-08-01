class Message:

    def __init__(self, text: str, fl_like: bool = False) -> None:
        self.text = text
        self.fl_like = fl_like


class Viber:
    MESSAGES = []

    @classmethod
    def add_message(cls, msg: Message) -> None:
        cls.MESSAGES.append(msg)

    @classmethod
    def remove_message(cls, msg: Message) -> None:
        cls.MESSAGES.remove(msg)

    @staticmethod
    def set_like(msg: Message) -> None:
        msg.fl_like = True

    @classmethod
    def show_last_message(cls, n: int) -> None:
        for i in range(n):
            print(cls.MESSAGES[-1 - i])

    @classmethod
    def total_messages(cls) -> int:
        return len(cls.MESSAGES)
