# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# ValueError

class category:
    categories: list[dict] = [{'food': False, 'drink': True}, {'alc': False, 'nonalc': True}]

    @classmethod
    def make_published(cls, id: int, is_published: bool) -> None:
        try:
            cls.categories[id]['is_published'] = True
        except IndexError as e:
            raise ValueError(e)


print(category.make_published(0, False))

print(category.make_published(1, True))
print(category.make_published(2, True))
print(category.categories)

