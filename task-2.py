from typing import Callable 
import re

def generator_numbers(text: str):
    pattern = r'(?<=\s)[+-]?(?:\d+\.\d+|\d+|\.\d+)(?=\s)'
    all_numbers = re.findall(pattern, text)
    for number in all_numbers:
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))
   

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


