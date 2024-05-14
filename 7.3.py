class Category:
    categories = []

    @classmethod
    def add(cls, name, is_published=False):
        if any(category['name'] == name for category in cls.categories):
            raise ValueError("Category already exists")
        else:
            category = {'name': name, 'is_published': is_published}
            cls.categories.append(category)
            return cls.categories.index(category)

    @classmethod
    def get(cls, index):
        if index >= len(cls.categories):
            raise IndexError("Index already exists")
        else:
            return cls.categories[index]

    @classmethod
    def delete(cls, index):
        if 0 <= index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, name, is_published=None):
        if 0 <= index < len(cls.categories):
            if any(category['name'] == name for category in cls.categories if cls.categories.index(category) != index):
                raise ValueError("Category name is not unique")
            else:
                category = cls.categories[index]
                category['name'] = name
                if is_published is not None:
                    category['is_published'] = is_published
        elif index == len(cls.categories):
            cls.add(name, is_published)
        else:
            raise IndexError("Index out of range")

    @classmethod
    def get_published(cls, index):
        if 0 <= index < len(cls.categories):
            cls.categories[index]['is_published'] = True
        else:
            raise IndexError("Index out of range")


    @classmethod
    def get_unpublished(cls, index):
        if 0 <= index < len(cls.categories):
            cls.categories[index]['is_published'] = False
        else:
            raise IndexError("Index out of range")


Data = Category()
Data.add('books')
Data.add('movies')
Data.add('action')
Data.add('comedy')
Data.get_published(2)
Data.get_unpublished(2)
print(Category.categories)
