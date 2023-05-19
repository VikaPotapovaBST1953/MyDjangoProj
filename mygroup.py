groupmates = [
{
	 "name": "Александр",
	 "surname": "Макашов",
	 "exams": ['Социологоия', 'ИТиП', 'БЖ'],
	 "marks": [5, 5, 3]
},
{
	 "name": "Павел",
	 "surname": "Пиляк",
	 "exams": ['БЖ', 'АИС', 'КПТ'],
	 "marks": [4, 4, 5]
},
{
	 "name": "Александр",
	 "surname": "Якимов",
	 "exams": ['Электротехника', 'ИТиП', 'КПТ'],
	 "marks": [4, 3, 3]
}
]

def sortbyavg(avg, studlist):
    for i in studlist:
        if sum(i["marks"])/len(i["marks"]) >= avg:
            print(i["name"], i["surname"])
target = float(input("Введите средний балл: "))
sortbyavg(target, groupmates)
