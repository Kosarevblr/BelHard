def is_pal(text):
    for i in range(len(text)):
        if text[i]==text[-i-1]:
            return True
        else:
            return False
text=input().lower()
print(is_pal(text))