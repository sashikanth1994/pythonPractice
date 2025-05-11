import random

def generate_random_number(start, end):
    return random.randint(start, end)

strt = int(input("Enter the lower bound:"))
end = int(input("Enter the upprt bound:"))
print(generate_random_number(strt,end))