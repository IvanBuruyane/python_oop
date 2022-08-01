from typing import Optional


class Ellipse:

    def __init__(self, x1: Optional[float] = None, y1: Optional[float] = None, x2: Optional[float] = None, y2: Optional[float] = None) -> None:
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

    def __bool__(self) -> bool:
        return hasattr(self, "x1") and hasattr(self, "y1") and hasattr(self, "x2") and hasattr(self, "y2")

    def get_coords(self) -> tuple:
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom: list = [Ellipse(), Ellipse(), Ellipse(1, 2, 4, 8), Ellipse(3, 5, 234, 32)]
[ellips.get_coords() for ellips in lst_geom if ellips]