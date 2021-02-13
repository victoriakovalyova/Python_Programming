
    #на вход принимается набор строк
    #считать строку циклом
    #создает список
    #посчитать средний балл по предмтам
    #вывести значения среднего балла циклом
    #
    #Петров;85;92;78
    #Сидоров;100;88;94
    #Иванов;58;72;85
    #85.0
     #71.666666667
     #81.0 
#84.0 
#85.666666667
with open("dataset_3363_4.txt", "r") as information, open("output.txt", "w") as output:
    counter, sum_math, sum_physics, sum_russian_language = 0, 0, 0, 0
    for line in information:
        _list = line.strip().split(";")
        average = (int(_list[1]) + int(_list[2]) + int(_list[3])) / 3
        counter += 1
        sum_math += int(_list[1])
        sum_physics += int(_list[2])
        sum_russian_language += int(_list[3])
        output.write(str(average)+"\n")
    output.write(str(sum_math / counter) + " " + str(sum_physics / counter) + " " + str(sum_russian_language / counter))
