# map============================================================================
text = '''
Map__________________________________________'''
print (text)

def square(x):
     return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print('x**2:         ',list(squared_numbers))  # [1,4,9,16,25]

# Сконвертуйте лист градусів у Цельсіях до Фаренгейтів. (Лист [0, 10, 20, 30, 40]). Формула для обчислення: (c * 9/5) + 32
def FC(c):
    return c*9/5 + 32

numbers = [0, 10, 20, 30, 40]
Far = map(FC,numbers)
print('F:            ',list(Far))

#Порахуйте довжину кожної строки (Лист ['apple', 'banana', 'orange', 'kiwi'])
def lengstring (str):
   return len(str)

food = ['apple','banana','orange','kiwi']
strleng = map(lengstring,food)
print('String length:',list(strleng))

#Сконвертуйте лист строк у верхній регістр (Лист ['hello', 'world', 'python', 'programming'])
def HighLetter (x):
    #return x.upper()

    return x.replace(x[0],x[0].upper(),1) #string.replace(oldStr, newStr, count)

    #Вариант 2
    # y = x[0].upper()
    # for i in range(1,len(x)):
    #     y = y + x[i]
    # return y

str = ['hello','world','python','programming']
High = map(HighLetter,str)
print('Upper case:   ',list(High))

#Filter=============================================================================
text = '\nFilter_______________________________________   '
print(text)

def is_even(x):
    return x % 2 == 0

numbers = [1,2,3,4,5]
even_numbers = filter(is_even, numbers)
print('Even number:  ',list(even_numbers)) #[2,4]

#Відфельтруйте слова, довжина яких менша за 5 (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape'])
str = ['apple', 'banana', 'orange', 'kiwi', 'grape']
strleng = filter(lambda x: len(x)<5,str)
print('Short string: ',list(strleng))

#Відфельтруйте пусті строки (Лист ['hello', '', 'world', 'python', '', 'programming'])
def len0(x):
    return len(x)>0

str = ['hello', '', 'world', 'python', '', 'programming']
strleng = filter(len0, str)
print('Full string:  ',list(strleng))

#Відфельтруйте слова, що НЕ починаються з літери ‘a’ (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado'])
def filterA(str):
    if len0(str):
        return str[0] != 'a'
    return True #пустые строки тоже вернем

    #вариант 2
    # return str.find('a') != 0 #метод find() возвращает индекс первого вхождения подстроки в строку find(str, start, end)

str = ['apple', 'banana', 'orange', 'kiwi', 'grape']
#str = ['hello', '', 'world', 'python', '', 'programming']
strA = filter(filterA,str)
print('String ohne A:',list(strA))

#reduce==========================================================================================
print('\nReduce_______________________________________   ')

from functools import  reduce

def multiply(x,y):
    return x*y

numbers = [1,2,3,4,5]
product = reduce(multiply,numbers)
print("Multiply: ",product)#120

#Порахуйте сумму елементів (Лист [1, 2, 3, 4, 5])
product = reduce(lambda x,y: x+y, numbers)
print("Sum:      ",product)

#Знайдіть найбільший елемент (Лист [23, 12, 56, 34, 78, 9, 67])
numbers = [23, 12, 56, 34, 78, 9, 67]
product = reduce(lambda x,y: max(x,y),numbers)
print("Max:      ",product)

#Зробіть одну строку (з пробілами) з листу строк (Лист ['hello', 'world', 'python', 'programming'])
str = ['hello', 'world', 'python', 'programming']
product = reduce(lambda x,y: x+' '+y,str)
print("String:   ",product)

#lambda=========================================================================================
print("\nLambda_______________________________________")

def is_positiv(num):
    return num >=0

numbers = [-1,2,-3,4,-5]
positiv_numbers = filter(is_positiv,numbers)
print('def:   ',list(positiv_numbers)) #[2,4]

numbers = [-1,2,-3,4,-5]
positiv_numbers = filter(lambda num: num >=0 ,numbers)
print('lambda:',list(positiv_numbers)) #[2,4]

#Zip, enumerate, sorted============================================================================
print('\nZip, enumerate, sorted_______________________')

names = ['Alisa','Bob','Charlie','Anna']
ages = [25,30,35]
people = zip(names,ages)
print('zip:   ',list(people))

fruits = ['apple', 'banana','cherry']
print('enumerate:')
for index,fruit in enumerate(fruits):
    print("       ",index,fruit)

numbers = [3,1,4,1,5,9,2,6,5,3,5]
sorted_numbers = sorted(numbers)
print('sorted:',sorted_numbers)
