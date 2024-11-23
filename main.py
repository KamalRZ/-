from dict import meme_dict

m = input("Выберите режим:0 - узнать значение слова; 1 - ввести новое слово: ")
while m not in ['0', '1']:
    print("невозможный режим! Попробуйте снова")
    m = input("Выберите режим:0 - узнать значение слова; 1 - ввести новое слово: ")
if m == '0':
    while True:

        word = input('Введите непонятное слово: ').upper()
        print(meme_dict.get(word, "Извините, слово не найдено"))
        if input("Вы хотите узнать значение ещё одного слова? 0 - да; 1 - нет: ") == "1":
            break
else:
    with open("dict.py", "a") as f:
        f.seek(f.tell()-1, 0)
        f.write(f'"{input("Введите слово: ").upper()}":"{input("Введите перевод: ").lower()}"')
print("пока! заходи ещё")
