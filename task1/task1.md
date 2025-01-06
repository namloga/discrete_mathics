# Задание №1 по варианту: `Проверка свойств бинарного отношения`
Студент ИТМО,  Нгуен Динь Нам - 415149
## Вариант 1

## Задание 
Написать программу, которая по заданному заранее отношению выводит его свойства (рефлексивность, симметричность, транзитивность)
<br>
- Формат входного файла (input.txt): Первая строка содержит набор S из различных натуральных чисел, разделённых пробелами. Последующие строки - Каждая строка содержит пару чисел (a, b),  представляющую бинарное отношение R между элементами множества S. Числа в каждой строке разделяются пробелами. 
-  Формат выходного файла (output.txt): должны быть перечислены свойства бинарного отношения: Reflexive, Anti-reflexive, Not-reflexive, Symmetric, Asymmetric, Anti-symmetric, Not-symmetric, Transitive, Anti-transitive, Not-transitive. (True/False)  
## Input / Output 

| Input                                                                                                   | Output                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 2 3 <br> 1 1 <br> 2 2 <br> 3 3 <br> 1 2 <br> 2 1 <br> 2 3 <br> 3 2 <br> 1 3 <br> 3 1                  | Reflexive: True <br> Anti-reflexive: False <br> Not-reflexive: False <br> Symmetric: True <br> Asymmetric: False <br> Anti-symmetric: False <br> Not-symmetric: False <br> Transitive: True <br> Anti-transitive: False <br> Not-transitive: False |
| 1 2 3 4 5 <br> 1 2 <br> 2 1 <br> 3 4 <br> 4 5 <br> 5 3                                                  | Reflexive: False <br> Anti-reflexive: True <br> Not-reflexive: False <br> Symmetric: False <br> Asymmetric: False <br> Anti-symmetric: False <br> Not-symmetric: True <br> Transitive: False <br> Anti-transitive: True <br> Not-transitive: False |
| 1 2 3 4 5 6 7 8 9 10 <br> 1 1 <br> 2 2 <br> 3 4 <br> 4 5 <br> 6 7 <br> 7 8 <br> 8 9 <br> 9 10 <br> 10 6 | Reflexive: False <br> Anti-reflexive: False <br> Not-reflexive: True <br> Symmetric: False <br> Asymmetric: True <br> Anti-symmetric: True <br> Not-symmetric: False <br> Transitive: False <br> Anti-transitive: True <br> Not-transitive: False  |

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/namloga/discrete_mathics.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd discrete_mathics
   ```
3. Запустите программу:
   ```bash
   python -m task1.src.main
   ```

4. Запуск тестов:
   ```bash
   python -m unittest discover -s task1/tests -p "test_*.py"
   ```
