
import random
from logo import vs

data = [
    {
        "area": "アジア",
        "population": 4436
    },
    {
        "area": "アフリカ",
        "population": 1216
    },
    {
        "area": "ヨーロッパ",
        "population": 738
    },
    {
        "area": "北米",
        "population": 579
    },
    {
        "area": "オセアニア",
        "population": 40
    },
]


def random_choice():
    return random.choice(data)


def show(choice):
    name = choice["area"]
    population = choice["population"]
    return f"area: {name}"


def check(guess, a_population, b_population):
    if a_population > b_population:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    Continue = True

    choice_a = random_choice()
    choice_b = random_choice()

    while Continue:
        choice_a = choice_b
        choice_b = random_choice()
        while choice_a == choice_b:
            choice_b = random_choice()

        print(f"比較　A: {show(choice_a)}")
        print(vs)
        print(f"B: {show(choice_b)}")

        guess = input("どの国がより高い人口をもっていますか　A あるいは B:    ").lower()
        a_population = choice_a["population"]
        b_population = choice_b["population"]
        is_True = check(guess, a_population, b_population)

        print("\033[H\033[2J")

        if is_True:
            score += 1
            print(f"正しい！！！　点数： {score}")
        else:
            Continue = False
            print(f"違う！！！　点数: {score}")


game()
