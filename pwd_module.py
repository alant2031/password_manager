# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "+", "@", "_", "?", "^"]


def generate():
    qtd_letters = random.randint(4, 6)
    qtd_symbols = random.randint(1, 2)
    qtd_numbers = random.randint(1, 2)

    password_letters = [random.choice(letters) for _ in range(qtd_letters)]
    password_symbols = [random.choice(symbols) for _ in range(qtd_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(qtd_numbers)]

    password_list = (
        password_letters + password_symbols + password_numbers + ["K"]
    )  # noqa

    random.shuffle(password_list)

    password = "".join(password_list)

    return password
