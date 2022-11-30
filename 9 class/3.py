# #3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку
# ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
# нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
# имена категорий уникальны, если новое имя категории нарушает уникальность в списке
# категорий, вызвать исключение ValueError


class Category:
    categories: list[str] = []

    @classmethod
    def add(cls, category: str) -> int:
        category = category.title()
        if category in cls.categories:
            raise ValueError('not unique')
        cls.categories.append(category)
        return len(cls.categories) - 1

    @classmethod
    def get(cls, id: int) -> str:
        if id in range(0, len(cls.categories)):
            return cls.categories[id]
        else:
            raise ValueError('no category')

    @classmethod
    def delete(cls, id: int) -> None:
        try:
            del cls.categories[id]
        except IndexError:
            pass

    @classmethod
    def update(cls, id: int, new_cat: str) -> None:
        new_cat = new_cat.title()
        if new_cat in cls.categories:
            raise ValueError
        try:
            cls.categories[id] = new_cat
        except IndexError:
            cls.add(new_cat)




print(Category.add('food'))
print(Category.add('drink'))
print(Category.add('foods'))
print(Category.get(1))
print(Category.add('drinks'))
print(Category.delete(0))
print(Category.update(2, 'drinks'))
print(Category)