class DateError(Exception):
    """Incorrect date format"""


class DateString:

    def __init__(self, date_string: str) -> None:
        self._date_string = date_string

    def __validate_date(self, date: str) -> None:
        if type(date) is not str:
            raise DateError
        day, month, year = date.split(".")
        self.__validate_part_of_date(day, 1, 31)
        self.__validate_part_of_date(month, 1, 12)
        self.__validate_part_of_date(year, 1, 3000)

    def __setattr__(self, key, value):
        if key == "_date_string":
            self.__validate_date(value)
        super().__setattr__(key, value)

    @staticmethod
    def __validate_part_of_date(part_of_date: str, min: int, max: int) -> None:
        try:
            part_of_date_int = int(part_of_date)
            if not min <= part_of_date_int <= max:
                raise DateError
        except:
            raise DateError

    def __str__(self) -> str:
        date_list = self._date_string.split(".")
        for i in range(2):
            date_list[i] = date_list[i].zfill(2)
        date_list[-1] = date_list[-1].zfill(4)
        return ".".join(date_list)
    #
    # @staticmethod
    # def __validate_month(month: str) -> None:
    #     try:
    #         month = int(month)
    #         if not 1 <= day_int <= 12:
    #             raise DateError
    #     except:
    #         raise DateError

date_string = input()
try:
    print(DateString(date_string))
except:
    print("Неверный формат даты")