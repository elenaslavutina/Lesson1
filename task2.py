
time = int(input("Введите время в секундах : "))
print('%s %d %s %d %s %d'% ( "Часов:", int(time/3600)," Минут: ", int(time/60) ," секунд: " , time%60 ))

print('Секунды: {2}; Минуты: {1}; Часы: {0}'.format(int(time/3600), int(time/60) , time%60))

