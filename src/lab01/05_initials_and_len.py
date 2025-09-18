
full_name = input("ФИО: ")
words = full_name.strip().split()
initials = ''.join(word[0].upper() for word in words if word)
length = len(full_name.strip())
print(f"Инициалы: {initials}.")
print(f"Длина: {length}")