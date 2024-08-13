# if __name__ == '__main__':
#     print('AAAAAAA')


### Задача 1
# Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе,
# и возвращает количество символов (точек и/или тире) в ней. Пример строки азбуки Морзе:
#
# .--- .- ...- .-

def count_morse_characters(str_morse):
    point = str_morse.count('.')
    dash = str_morse.count('-')
    return point + dash


print(count_morse_characters('.--- .- ...- .-'))

### Задача 2
# Вам предоставлен список английских слов и словарь соответствия символов строки коду азбуки Морзе.
# Создайте функцию morse_encode(), которая принимает словарь с азбукой Морзе и слово для кодирования и
# возвращает его представление в азбуке Морзе с использованием пробелов между символами.

morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
         "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
         "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
         "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
         "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
         "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran', 'javascript', 'kotlin', 'swift', 'basic', 'pascal']


def morse_encode(morse, word_to_decode):
    word_in_morse = ''
    for i in word_to_decode:
        word_in_morse += morse[i]
        word_in_morse += ' '
    return word_in_morse.strip()


print(morse_encode(morse, words_to_decode[0]))


### Задача 3
# Вам предоставлен словарь соответствия символов строки коду азбуки Морзе.
# Напишите функцию morse_decode(), которая принимает словарь с азбукой Морзе и строку в виде азбуки Морзе
# и возвращает декодированное слово. Символы в закодированной строке разделены пробелами.
# Пример работы функции:
# print(morse_decode(morse, "--. .- -- ."))
#
# >>> game

morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
             "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
             "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
             "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
             "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran', 'javascript', 'kotlin', 'swift', 'basic', 'pascal']


def morse_encode(morse, code_morse):
    word = ''
    code_morse = code_morse.split()
    print(code_morse)
    for i in code_morse:
        for key, value in morse.items():
            if i == value:
                word += key
    return word


print(morse_encode(morse, "--. .- -- ."))


### Задача 4
# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию calculate_total_cost(), которая принимает список продуктов и возвращает общую
# стоимость всех товаров (цена * количество).
# Если у продукта не указаны цена и/или количество, это не должно приводить к ошибке.

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]


def calculate_total_cost(list_products):
    total_sum = 0
    for product in list_products:
        for i in products:
            try:
                if product["name"] == i["name"]:
                    total_sum += i["price"] * product["quantity"]
            except KeyError:
                total_sum += 0
    return total_sum


# print(calculate_total_cost(["Lettuce", "Cake"]))
print(calculate_total_cost([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
                    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
                    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}]))

### Задача 5
# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию filter_products_by_price(), которая принимает на вход список продуктов и верхний порог
# цены и возвращает список продуктов, цена которых не превышает заданную максимальную цену. Если у продукта не
# указана цена, это не должно приводить к ошибке, при получении значения по ключу,
# если ключа в словаре нет - цена должна равняться 0 (используйте метод get()).

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]


def filter_products_by_price(list_products, max_price):
    new_list_products = []
    for product in list_products:
        if product.get("price", 0) <= max_price:
            new_list_products.append(product)
    return new_list_products

print(filter_products_by_price([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
                    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
                    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}], 1000))

### Задача 6
# Вам предоставлен список словарей, в котором перечислены товары.
# Напишите функцию find_product_by_name(), которая принимает список продуктов и имя для поиска и
# возвращает информацию о продукте по его имени. Если продукт не найден в списке, функция возвращает
# строку «Продукт с таким именем не найден в списке». Если у продукта отсутствует имя, это не должно
# привести к ошибке.


products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

print('---------------')
def find_product_by_name(list_products, product_name):
    for product in list_products:
        try:
            if product_name == product.get("name", None):
                return product
        except AttributeError:
            continue
    return 'Продукт с таким именем не найден в списке'


print(find_product_by_name([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
                    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
                    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}], "Banana"))


### Задача 7
# Вам предоставлен список словарей, в котором перечислены товары.
# Напишите функцию update_product_info(), которая обновляет информацию о продукте по его имени и возвращает
# обновленный список продуктов.
# Функция принимает следующие аргументы: список продуктов, имя продукта, информацию, по которому нужно обновить,
# и словарь с данными, которые требуется обновить. За один вызов функция может обновить только один продукт.
# Если продукт не найден в списке, функция возвращает строку «Продукт с таким именем не найден в списке».
# Если у продукта отсутствует имя, это не должно привести к ошибке.

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

print('----//----//----')


def update_product_info(list_products, product_name, new_info):
    # new_list_products = list_products
    for key, product in enumerate(list_products):
        try:
            if product_name == product.get("name", None):
                product.update(new_info)
                # del new_list_products[key]
                # new_list_products.insert(key, new_info)
                return list_products
        except AttributeError:
            continue
    return 'Продукт с таким именем не найден в списке'


# print(update_product_info([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
#                     {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
#                     {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}], "Apple",
#                           {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True}))

product_to_update = "Apple"
new_info = {"quantity": 10000, "organic": False}
update_result = update_product_info(products[0:0], product_to_update, new_info)
print(update_result)

### Задача 8
# Вам предоставлен список словарей, в котором перечислены товары.
# Напишите функцию sort_products_by_quantity(). Функция должна принимать на вход список продуктов и направление
# сортировки (атрибут должен иметь имя ascending) со значением по умолчанию False (булевое значение) и сортировать
# продукты по количеству в порядке возрастания или убывания.
# Если в функцию не передан аргумент направления сортировки, сортировка должна проходить в порядке возрастания
# количества товаров (от меньшего к большему). Если у продукта не указано количество, это не должно привести к ошибке,
# при получении значения по ключу, если ключа в словаре нет - количество должно равняться 0 (используйте метод get()).


products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

print('------------')


def sort_products_by_quantity(list_products, ascending=False):
    return sorted(list_products, key=lambda x: x.get('quantity', 0), reverse=ascending)


print(sort_products_by_quantity(products))

### Задача 9
# Вам предоставлен список словарей, в котором перечислены товары.
# Напишите функцию average_price_per_category(), которая принимает на вход список продуктов и возвращает новый словарь,
# где ключи — категории, а значения — средняя цена продуктов в каждой категории. Округлите результат вычисления до
# 1 знака после запятой. Если у продукта отсутствует категория, это не должно привести к ошибке.
# Пример вывода:
# {'fruit': 136.7, 'veggie': 166.7}


products1 = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

print('----//----//----')


def average_price_per_category(list_products):
    list_category = {}
    for product in list_products:
        if product.get("category", 0):
            list_category.update({product['category']: []})
    for product in list_products:
        if product.get("category", 0) and product.get('price', 0):
            list_category[product['category']].append(product['price'])
    for key, value in list_category.items():
        list_category[key] = round(sum(value) / len(value), 1)
    return list_category

print(average_price_per_category(products1))


### Задача 10
# Вам предоставлен список словарей в котором перечислены товары.
# Напишите функцию group_products_by_category(products), которая принимает на вход список продуктов и возвращает
# словарь, где ключи — категории, а значения — списки продуктов в каждой категории. Если у продукта отсутствует
# категория, это не должно привести к ошибке. Такой продукт игнорируется программой.

print('---------------')

def group_products_by_category(list_products):
    list_category = {}
    for product in list_products:
        if product.get("category", 0):
            list_category.update({product['category']: []})
    for product in list_products:
        if product.get("category", 0) and product.get('price', 0):
            list_category[product['category']].append(product)
    # for key, value in list_category.items():
    #     list_category[key] = round(sum(value) / len(value), 1)
    return list_category

print(group_products_by_category(products1))