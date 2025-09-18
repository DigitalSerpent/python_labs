full_name = input("ФИО: ").strip()
chars = len(full_name.replace(' ', ''))
probely = full_name.count(' ')

words = full_name.split()
initials = ''.join(word[0].upper() for word in words if word)


print(f"Инициалы: {initials}.")
print(f"Длина: {probely + chars}")