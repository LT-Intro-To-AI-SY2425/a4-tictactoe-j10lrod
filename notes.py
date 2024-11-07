# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n, a):
        self.name = n
        self.age = a

       # def __str__(self) -> str:
       #     s = 

# instances of the dog class
logan = Dog("logan", 8)
cookie = Dog("cookie", 8)
maple = Dog("maple", 1)

print(logan)
print(cookie)
print(maple)