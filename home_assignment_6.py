# 2. Вам дается файл task2_input.txt, в нем лежит список. Каждый элемент на новой строке, и последняя строка - значение
# искомого элемента el.
# Напишите функцию, которая будет принимать имя этого файла, читать данные из него и создавать файл task2_output.txt,
# куда будет записывать часть списка ДО первого места, где попался el.
# Пример: в функцию передан файл с числами -1, 3, 2, 5, 1, 6, 2 (каждый с новой строки, здесь через запятую
# для краткости). В таком случае значение el - 2 (последняя строка), и ваша функция должна записать в файл
# список -1, 3 (каждый элемент с новой строки).
# Если значение, равное el, стоит на первом месте списка, запишите в файл слово "Empty".
# Если значения, равного el, в списке не нашлось, запишите в файл слово "Error"

#from home_assignment_4.py import get_sublist as qwer

# def get_sublist_ha4(my_list, item):
#
#     for element in my_list:
#         if element == item:
#             index = my_list.index(element)
#             return my_list[:index]
#             break
#
#     return "Error"

from home_assignment_4 import get_sublist as get_sublist_ha4
#import home_assignment_4

def get_sublist(file_name):

    file_input = open(file_name,"r")
    my_list = []
    for line in file_input:
        my_list.append(int(line.strip()))

    file_input.close()

    result_list = get_sublist_ha4(my_list,my_list[-1])
    if result_list == 'Error':
        result_list = ['Error']

    file_otput = open("task2_output.txt","w")
    for element in result_list:
        file_otput.write(str(element) +"\n")

    file_otput.close()

# 3. В функцию передается CSV файл task3_input.csv, c заголовком city,score. Ниже в нем информация в
# виде "название города,кол-во балов" (делимитер - запятая).
# Функция должна вернуть CSV файл task3_output.csv следующего вида:
#     score_sum,avg_score,best_city
#     1,2,3
# где:
# 1 - сумма очков всех городов
# 2 - среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3 - название города, у которого максимальное количество очков

# def city_rating_ha4(cities_dict):
#     count = 0
#     max = 0
#     сity_max = ""
#     sum = 0
#     for key, value in cities_dict.items():
#         count += 1
#         if value > max:
#             max = value
#             сity_max = key
#         sum += value
#
#     average = 0
#     if not count == 0:
#         average = sum / count
#
#     return (sum, average, сity_max)

from home_assignment_4 import city_rating as city_rating_ha4

def city_rating(file_name):
    file_input = open(file_name,"r")

    # skip the header
    file_input.readline()

    cities_dict = {}
    for line in file_input:
        elements = line.strip().split(',')
        cities_dict[elements[0]]=int(elements[1])

    file_input.close()

    result = city_rating_ha4(cities_dict)

    file_output = open('task3_output.csv','w')
    file_output.write('nscore_sum,avg_score,best_city\n')
    file_output.write(f'{result[0]},{result[1]},{result[2]}')

# 4. Вам дается файл task4_input.csv с заголовком name,swimming,chess,guitar и контентом следующего вида:
# имя ребенка и через запятую три значения - 1, если ребенок посещает соответствующий кружок, 0 - если нет.
# Пример:
#     name,swimming,chess,guitar
#     Emma,1,0,0
# У Эммы 1 только в колонке swimming, следовательно, она посещает только плавание.
# На основе этих данных вам нужно вычислить детей, которые не знают никого, кроме одногруппников из своего кружка
# (то есть они не пересекаются с детьми из других кружков).
# Результат запишите в файл task4_output.txt, где каждое имя из вычисленного множества - на новой строке

# def not_busy_children_ha4(groups_dict):
#
#     set_groups = {}
#     for value in groups_dict.values():
#          set_groups = set(value).symmetric_difference(set_groups)
#
#     return set_groups

from home_assignment_4 import not_busy_children as not_busy_children_ha4

def not_busy_children(file_name):
    file_input = open(file_name, "r")

    # skip the header
    file_input.readline()

    swimming = []
    chess = []
    guitar = []

    for line in file_input:
        elements = line.strip().split(',')
        if elements[1] == '1':
            swimming.append(elements[0])
        if elements[2] == '1':
            chess.append(elements[0])
        if elements[3] == '1':
            guitar.append(elements[0])

    file_input.close()

    groups_dict = {'swimming': swimming, 'chess': chess, 'guitar': guitar}

    set_group = not_busy_children_ha4(groups_dict)

    file_otput = open("task4_output.txt", "w")
    for element in set_group:
        file_otput.write(str(element) + "\n")

    file_otput.close()

# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def get_result_list(file_name):
    output = open(file_name)

    result_list = []
    for line in output:
        result_list.append(line.strip())
    return result_list


def get_city_rating_result(file_name):
    output = open(file_name)

    # skip the header
    output.readline()

    result = output.readline().strip().split(",")
    return tuple(result)


def test_get_sublist():
    get_sublist("task2_input.txt")
    result_list = get_result_list("task2_output.txt")
    result_list = [int(item) for item in result_list]

    assert result_list == [1, 5, 3]


def test_city_rating():
    city_rating("task3_input.csv")
    result_list = get_city_rating_result("task3_output.csv")
    result = tuple(result_list)

    assert result == ("366", "61.0", "Munich")


def test_not_busy_children():
    not_busy_children("task4_input.csv")
    result_list = get_result_list("task4_output.txt")
    result = set(result_list)

    assert result == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()
    print("Well done!!!")
