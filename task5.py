val = int(input("Выручка компании : "))
ubitok = int(input("Издержки компании :"))
if val > ubitok:
    print("Ваша выручка составила : ",val-ubitok)
    print("Рентабельность :", val/ubitok)
    count = int(input("Введите Количество сотрудников фирмы :"))
    print("Прибыль фирмы на каждого сотрудника :", (val-ubitok)/count)
if val<ubitok:
    print("Ваш убыток составил", ubitok-val)
elif val == ubitok:
    print("Ваша выручка равна вашим издержкам")


