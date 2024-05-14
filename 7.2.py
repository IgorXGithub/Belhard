class Category:
    categories = []

    @classmethod
    def add(cls, name):
        if name in cls.categories:
            raise ValueError("Category already exists")
        else:
            cls.categories.append(name)
            return cls.categories.index(name)

    @classmethod
    def get(cls, index):
        if  index >= len(cls.categories):
            raise IndexError("Index already exists")
        else:
            return cls.categories[index]


    @classmethod
    def delete(cls, index):
        if 0 <= index < len(cls.categories):
            del cls.categories[index]


    @classmethod
    def update(cls, index, name):
        if 0 <= index < len(cls.categories) and not name in cls.categories:
            cls.delete(index)
            cls.categories.insert(index, name)
        elif 0 <= index < len(cls.categories) and name in cls.categories:
            raise ValueError("not unique name")
        elif index > len(cls.categories) and not name in cls.categories:
            cls.add(name)
        else:
            raise ValueError("not unique name")





Category.add("books")
Category.add("movies")
Category.add("games")
Category.add(name="foods")

print(Category.categories)

Category.delete(8)
print(Category.categories)
Category.update(6, 'music')
print(Category.categories)



