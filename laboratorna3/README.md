# Звіт до роботи
## Тема: Вступні заняття:Основи програмування на Python
### Мета роботи: Навчитись застосовувати основні конструкції мови Python, виконати всі приклади та з використанням AI створити власні приклади які демонструють особливості кодових конструкцій Pyhton


---
### Виконання роботи
* Результати виконання завдання *2*;
    1. Розробили/Створили першу програму на Python
    1. Програма вивела значення: "Всі значення заданого коду"
    1. Отримав наступні результати: Програма працює правильно,код спрацював у всіх методах виклику:<<Terminal,bash,jupyter>> файл з розширенням <<ipynb>> вивів результат.
    1. Навчився налаштуванню середовища роботи VS Code та створювати репозиторії в Github
* вставлені рисунки
 ![alt text]({AF5C94F0-381E-42E2-B7DB-6A090125F865}.png) - Юніт тести(з помилкою)
![alt text]({A15DF0C0-7B0F-4A78-845B-9882375A00A1}.png) - до першого завдання
    ![alt text]({726DD15A-D853-43CA-B296-D24F564E33D1}.png) - pytest
    ![alt text]({A2F6FC08-B685-4793-9966-8EC30E66A9AF}.png) - останнє завдання
    ![alt text]({DDA959DD-4562-4960-91B1-E773743A9FBB}.png) -html

* вставлений код / текстовий або числовий результат / інші результати:
    
class Figure:
    FIGURES = ["square", "rectangle", "triangle"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in self.FIGURES, "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_angles(self):
        if self.type in ["square", "rectangle"]:
            return 4
        if self.type == "triangle":
            return 3


def test_app_triangle():
    fig = "triangle"
    triangle = Figure(fig, 4)
    assert triangle.type == fig


* результати виконання індивідуального завдання (якщо такі є);

---

### Перша програма штучного інтелекту (ChatGPT)

> Запитання:  Запитайте у АІ як би він розписав про основи Python (задайте промпт вказавши що ви вивчаєте Python з використанням Jupyter Notebook). Спробуйте виконати приклади Python коду та вставте їх відповіді у звіт

### Відповідь ChatGPT: Яку першу програму міг би написати ШІ та пояснення до неї

# ChatGPT Response: Basics of Python



---

## 1. Variables and Data Types

Python has different types of variables, including strings, integers, floats, lists, dictionaries, tuples, and sets. Here are some examples:

```python
my_string = "Hello, Python!"
my_int = 10
my_float = 3.14
my_list = [1, 2, 3, "four"]
my_dict = {"name": "Alice", "age": 25}
my_tuple = (1, "two")
my_set = {"apple", "banana", "cherry"}

print(my_string)
print(my_int, my_float)
print(my_list)
print(my_dict)
print(my_tuple)
print(my_set)
```
### Output:Hello, Python!
```
10 3.14
[1, 2, 3, 'four']
{'name': 'Alice', 'age': 25}
(1, 'two')
{'banana', 'apple', 'cherry'}
```
### controll structures:
```
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

for i in range(3):
    print(f"For loop iteration: {i}")

counter = 0
while counter < 3:
    print(f"While loop counter: {counter}")
    counter += 1
    x is positive
For loop iteration: 0
For loop iteration: 1
For loop iteration: 2
While loop counter: 0
While loop counter: 1
While loop counter: 2

```
### Functions and Lambda
```
def greet(name):
    return f"Hello, {name}!"

my_lambda = lambda x: x ** 2

print(greet("Artem"))
print("Square of 5 using lambda:", my_lambda(5))
results:Hello, Artem!
Square of 5 using lambda: 25

```
### Context Managers (with statement)
```
with open("demo.txt", "w") as f:
    f.write("This is a demo file\n")

with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())
results:This is a demo file

```
### Висновок:


---

### 1. Що зроблено в роботі
У ході роботи було вивчено та опрацьовано основи Python, включаючи:  
- змінні та типи даних (str, int, float, list, dict, tuple, set);  
- управління потоком виконання (if-else, for, while);  
- функції та лямбда-функції;  
- обробку виключень (try-except-finally);  
- контекстні менеджери (`with`).  

Всі приклади були виконані у Jupyter Notebook. Додатково я звертався до ChatGPT, щоб отримати приклади коду та пояснення для кожної теми, які потім було реалізовано у власних прикладах.

---

### 2. Чи досягнуто мети роботи
Мета роботи була повністю досягнута. Було не лише виконано усі приклади, а й створено власні приклади за допомогою ChatGPT, що дозволило глибше зрозуміти особливості Python.

---

### 3. Які нові знання отримано
- Ознайомлення з базовими типами даних та їх використанням;  
- Вправи з циклів та умовних конструкцій;  
- Практика створення функцій та лямбда-функцій;  
- Розуміння роботи обробки виключень та контекстних менеджерів;  
- Досвід інтеграції AI (ChatGPT) для отримання підказок і генерації прикладів.

---

### 4. Чи вдалося відповісти на всі питання задані в ході роботи
Так, усі питання щодо основ Python були опрацьовані і перевірені на практиці.

---

### 5. Чи вдалося виконати всі завдання
Так, всі завдання виконані повністю, включаючи запуск кодів, створення власних прикладів та їх оформлення у Jupyter Notebook.

---

### 6. Чи виникли складності у виконанні завдання
Невеликі труднощі виникли при роботі з контекстними менеджерами і встановленням додаткових бібліотек у Jupyter Notebook, але вони були швидко усунені.

---

### 7. Чи подобається такий формат здачі роботи
Так, формат з Jupyter Notebook є зручним і наочним. Він дозволяє поєднувати код, результати виконання та пояснення в одному інтерактивному документі.

---

### 8. Побажання для покращення
Було б корисно додати більше прикладів для складніших конструкцій Python, а також поради щодо оформлення звіту та інтеграції результатів виконання коду у Markdown-комірки для автоматичного відображення результатів.

