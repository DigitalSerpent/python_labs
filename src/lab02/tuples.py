def data(chars):
    student_fio = ' '.join(chars[0].split()) 
    student_group = chars[1].strip()
    student_gpa = f"{float(chars[2]):.2f}"
    el_fio = student_fio.split()
    surname = el_fio[0]
    initials = '.'.join(name[0].upper() for name in el_fio[1:]) + '.'
    fio_new = f"{surname} {initials}"
    
    return f"{fio_new}, гр. {student_group}, GPA {student_gpa}"

print(data(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(data(("Петров Пётр", "IKBO-12", 5.0)))
print(data(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(data(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(data('', "IKBO-12", 3.5460))