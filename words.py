import random

words = [
    "python","variable","function","loop","condition","string","integer","boolean","compiler","debugging",
    "algorithm","database","network","security","encryption","software","hardware","keyboard","monitor",
    "processor","memory","storage","binary","decimal","operator","syntax","exception","iteration","recursion",
    "inheritance","polymorphism","abstraction","encapsulation","framework","library","package","module"
]

def get_word():
    return random.choice(words)