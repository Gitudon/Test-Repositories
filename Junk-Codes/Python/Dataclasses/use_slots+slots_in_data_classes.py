from dataclasses import dataclass


@dataclass
class User:
    __slots__ = ["name", "age"]
    name: str
    age: int


u = User(name="Alice", age=30)
print(u)
