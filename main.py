from decimal import Decimal
from rtd import RTD
import check
import color

# ГОСТ 6651-2009. ТЕРМОПРЕОБРАЗОВАТЕЛИ СОПРОТИВЛЕНИЯ ИЗ ПЛАТИНЫ, МЕДИ И НИКЕЛЯ
# Объявление констант.

temp_coefficient_cu = 0.0042800
a_cu = 0.00428
b_cu = -0.00000062032
c_cu = 0.00000000085154

temp_coefficient_p = 0.00391
a_p = 0.0039690
b_p = -0.0000005841
c_p = -0.000000000004330

temp_coefficient_pt = 0.00385
a_pt = 0.0039083
b_pt = -0.0000005775
c_pt = -0.000000000004183

temp_coefficient_ni = 0.00617
a_ni = 0.0054963
b_ni = 0.0000067556
c_ni = 0.0000000092004

# Объявление переменных.

nominal_tc = 0
material_tc = 0
input_wrong = (f'Внимание!!!\n'
               f'Ошибка ввода.\n'
               f'Введены неверные данные')

# Основной цикл программы

while True:
    print(f'Посчитаем значения термопреобразователей сопротивления\n'
          f'Сократим названия до аббревиатур\n'
          f'"ТС" - Термопреобразователь сопротивления\n'
          f'"ЧЭ" - Чувствительноый элемент\n'
          f'"Номинальные характеристики ТС" - сопротивление ТС в омах при 0⁰C')

    #  Здесь и далее. Вспомогательный цикл для проверок ввода пользователя.

    while True:
        print(f'-------------------------------------')
        nominal_tc = input(
            color.blue(f'Введите номинальные характеристики ТС: '))
        if not check.is_num(nominal_tc):
            print(color.red(input_wrong))
            continue
        elif not check.this_nom(nominal_tc):
            print(color.red(input_wrong))
            continue
        break

    while True:
        print(f'-------------------------------------\n'
              f'Выберите материал чувствительного элемента ТС\n'
              f'"М" - Медь\n'
              f'"П" - Платина (α = {temp_coefficient_p})\n'
              f'"Pt" - Платина (α = {temp_coefficient_pt})\n'
              f'"Н" - Никель')
        material_tc = str.upper(input(color.blue('Введите буквенный код ЧЭ: ')))
        if not check.is_letter(material_tc):
            print(color.red(input_wrong))
            continue
        elif not check.this_mat(material_tc):
            print(color.red(input_wrong))
            continue
        break

    tc = RTD(nominal_tc, material_tc)
    print(color.green(f'Вы выбрали градуировку ТС - {tc.type()}'))

    while True:
        print(f'-------------------------------------\n'
              f'Что нужно пересчитать?\n'
              f'1 - Омы в Температуру\n'
              f'2 - Температуру в Омы')
        ohms_or_temp = input(color.blue(f'Выберите 1 или 2: '))
        if not check.is_num(ohms_or_temp):
            print(color.red(input_wrong))
            continue
        elif not check.this_num(ohms_or_temp):
            print(color.red(input_wrong))
            continue
        break

    if int(ohms_or_temp) == 1:
        print(f'-------------------------------------\n'
              f'Пересчитаем Омы в Температуру')
    elif int(ohms_or_temp) == 2:
        print(f'-------------------------------------\n'
              f'Пересчитаем Температуру в Омы')
    data = input(color.blue(f'Введите данные сюда: '))

    #  Блок формул для расчетов.

    if int(ohms_or_temp) == 1:
        if material_tc == 'М':
            response = ((float(data) / int(nominal_tc)) - 1) / a_cu
            result = Decimal(response)  # Округление до сотых
            result = result.quantize(Decimal("1.00"))
            print(color.yellow((f'Температура для ТС-{tc.type()} при "{data}Ω"'
                                f' равна "{result}⁰C"')))

        elif material_tc == 'П':
            response = ((((a_p ** 2) -
                          (4 * b_p * (1 - (
                                  float(data) / int(nominal_tc))))) ** 0.5) -
                        a_p) / (2 * b_p)
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(color.yellow((f'Температура для ТС-{tc.type()} при "{data}Ω"'
                                f' равна "{result}⁰C"')))

        elif material_tc == 'PT':
            response = ((((a_pt ** 2) -
                          (4 * b_pt * (1 - (
                                  float(data) / int(nominal_tc))))) ** 0.5) -
                        a_pt) / (2 * b_pt)
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(color.yellow((f'Температура для ТС-{tc.type()} при "{data}Ω"'
                                f' равна "{result}⁰C"')))

        elif material_tc == 'Н':
            response = ((((a_ni ** 2) -
                          (4 * b_ni * (1 - (
                                  float(data) / int(nominal_tc))))) ** 0.5) -
                        a_ni) / (2 * b_ni)
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(color.yellow((f'Температура для ТС-{tc.type()} при "{data}Ω"'
                                f' равна "{result}⁰C"')))

    elif int(ohms_or_temp) == 2:
        if material_tc == 'М':
            response = int(nominal_tc) * (1 + (a_cu * float(data)))
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(
                color.yellow((f'Сопротивление для ТС-{tc.type()} при "{data}⁰C"'
                              f' равно "{result}Ω"')))

        elif material_tc == 'П':
            response = int(nominal_tc) * (1 + (a_p * float(data)) +
                                          (b_p * float(data) ** 2))
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(
                color.yellow((f'Сопротивление для ТС-{tc.type()} при "{data}⁰C"'
                              f' равно "{result}Ω"')))

        elif material_tc == 'PT':
            response = int(nominal_tc) * (1 + (a_pt * float(data)) +
                                          (b_pt * float(data) ** 2))
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(
                color.yellow((f'Сопротивление для ТС-{tc.type()} при "{data}⁰C"'
                              f' равно "{result}Ω"')))

        elif material_tc == 'Н':
            response = int(nominal_tc) * (1 + (a_ni * float(data)) +
                                          (b_ni * float(data) ** 2))
            result = Decimal(response)
            result = result.quantize(Decimal("1.00"))
            print(
                color.yellow((f'Сопротивление для ТС-{tc.type()} при "{data}⁰C"'
                              f' равно "{result}Ω"')))

    print(f'-------------------------------------\n'
          f'Хотите ли пересчитать что нибудь еще?')

    #  Завершающий программу цикл с проверкой ввода пользователя
    #  с продолжением либо завершением программы на выбор.

    while True:
        yn = str(input(color.blue(f'Введите "да" или "нет": ')))
        if not check.yes_or_no(yn):
            print(f'-------------------------------------')
            print(color.red(f'Нужно ввести "да" или "нет"!!!'))
            continue
        break
    if yn == 'да':
        continue
    else:
        exit()
