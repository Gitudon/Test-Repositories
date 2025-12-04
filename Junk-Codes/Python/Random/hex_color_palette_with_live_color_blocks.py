import random


def rand_hex():
    hex_digits = "0123456789ABCDEF"
    rand_chars = [random.choice(hex_digits) for _ in range(6)]
    return "#" + "".join(rand_chars)


for _ in range(5):
    h = rand_hex()
    r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    mood = "light" if (r + g + b) // 3 > 128 else "dark"
    print(f"\033[48;2;{r};{g};{b}m \033[0m {h} → {mood}")
