l_nominal = [50, 100, 500]
l_material = ['М', 'П', 'PT', 'Н']
l_num = [1, 2]
l_yn = ['да', 'нет']


def is_num(string):
    """Ошибка ввода если введены буквы"""
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_letter(num):
    """Ошибка ввода если введены цифры или символы"""
    if num.isalpha():
        return True
    else:
        return False


def this_nom(num):
    """Проверка правильности ввода номинала"""
    if int(num) in l_nominal:
        return True
    else:
        return False


def this_mat(string):
    """Проверка правильности ввода материала"""
    if string in l_material:
        return True
    else:
        return False


def this_num(num):
    """Проверка правильности выбора цифр ввода"""
    if int(num) in l_num:
        return True
    else:
        return False


def yes_or_no(string):
    """Проверка правильности выбора"""
    if string in l_yn:
        return True
    else:
        return False
