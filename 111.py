import csv

sl1 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м",
       "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ",
       "ы", "ь", "э", "ю", "я"]


with open('russian.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sl1)
