from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    x: int
    y: int


p = Point(10, 20)
print(p)
