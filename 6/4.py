# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

spis = [12, 'dfdf', '33', 12, 'sdaa', 33, 44, 55]

print(list(filter(lambda x: x==str(x), spis)))

