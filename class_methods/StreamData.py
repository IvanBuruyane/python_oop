from typing import List


class StreamData:

    def create(self, fields: List, lst_values: List) -> bool:
        if len(fields) != len(lst_values):
            return False
        [setattr(self, fields[i], lst_values[i]) for i in range(len(fields))]
        return True
