
cat_files = {}


class Cat:

    counter = 0

    def __init__(self):
        Cat.counter += 1
        self.id = Cat.counter
        self.path = f'cats/cat_picture_{self.id}.jpg'
