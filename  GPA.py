# - исходные данные список - оценки, множество - имена:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]         # - list - список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}            # - set - множество
students_list_=list(students)              # - list - преобразовали множество в список, т.к. необходимо его отсортировать
students_list_.sort()    # - отсортировали список в алфавитном порядке
A = sum(grades[0])/len(grades[0])           # вычисляем среднее арифметическое, через ввод новых переменных
B = sum(grades[1])/len(grades[1])
J = sum(grades[2])/len(grades[2])
K = sum(grades[3])/len(grades[3])
S = sum(grades[4])/len(grades[4])
new_grades = [A, B, J, K, S]        # создаём новый список из получившихся данных
new_list_students_grades = [(students_list_[0], A), (students_list_[1], B), (students_list_[2], J),
                     (students_list_[3], K), (students_list_[4], S)]        # - соединяем два списка в список пар кортежей
names_and_ratings = dict(new_list_students_grades)
print(names_and_ratings)
