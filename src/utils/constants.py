# MY_VARIABLE = 'This is my firts variable'
# MY_VARIABLE = 'New value'
# print(MY_VARIABLE)
# ------------------------------------------------
'''
Constantes para nuestra aplicación
docstring -> Información auxiliar que aparecerá en el IDE
'''
# TIPOS DE DATOS

# STRINGS
MERCADONA = "MERCADONA"
CARREFOUR = "CARREFOUR"
LIDL = "LIDL"
ALDI = "ALDI"


# NUMBERS
# DEFAULT_QUANTITY_TO_ALERT = 1_000_000 PARA LEERLO MEJOR, NO LEE EL _
DEFAULT_QUANTITY_TO_ALERT = 1
my_string = str(DEFAULT_QUANTITY_TO_ALERT)
# "1"

numeric_string = "34"
my_number = float(numeric_string)
# 34.0


# BOOLEANS
# IS_LOGGED_IN = True and False
# IS_LOGGED_IN = True or False
# IS_LOGGED_IN = not True
IS_LOGGED_IN = True


# LISTS STRINGS
MOCKUP_PRODUCTS_LIST = ['Fregona', 'Cereales', 'Papel Higiénico']
# MOCKUP_PRODUCTS_LIST[0] = ['Fregonaaa'] Lo Puedo cambiar


# TUPLES
MOCKUP_CUPONS = {'Comida a mitad de precio', 'Productos sin IVA'}

# Esto no se puede modificar como las LISTS, habría que hacer lo siguiente si 
# queremos modificarla
# temp = list(MOCKUP_CUPONS)
# temp[0] = 'Productos de limpieza...'
# MOCKUP_CUPONS = tuple(temp)

# Cosas que podemos hacer con las listas y tuplas: DESTRUCTURING
# UNPACKING -> DESTRUCTURING
# [primer_producto, segundo_producto] = MOCKUP_PRODUCTS_LIST
# Si destructuro debo poner tantos elementos como hay en la lista o un *
[primer_producto, *segundo_producto] = MOCKUP_PRODUCTS_LIST

# Se puede hacer igual con tuplas solo que usando paréntesis


# SET
# No admite duplicados y no está duplicado - SE declaran con llaves
SUPERMARKETS = {MERCADONA, CARREFOUR, LIDL, ALDI}
SUPERMARKETS.add('NUEVO SUPERMERCADO')
# SUPERMARKETS.add('MERCADONA') No puedo duplicar un dato que ya esta
# Con un SET todos los elementos que haya duplicados los va a quitar


# OBJETOS OBJECTS VS DICTIONARIES

# JAVASCRIPT - OBJECT LITERALS!!!!!
# const myObject = {
#     key1: 'value1'
# }
# PYTHON DICTIONARIES
MOCKUP_PRODUCTS = [{
    "id": 1,
    "name": "Fregona de microfibra",
    "description": ''' Fregona.....
    blablabla''',
    "category": "Productos de limpieza",
    "brand": "Mileda"
},
    {
    "id": 2,
    "name": "Fregona2 de microfibra2",
    "descripcion": ''' Fregona.....
    ...''',
    "category": "Productos de limpieza",
    "brand": "Mileda"
}]

MOCKUP_PRODUCTS_STORAGE = [{
    "id": 1,
    "product_id": 1,
    "quantity": 2,
    "espiration_date": "n/a",
    "left_to_alert": DEFAULT_QUANTITY_TO_ALERT
}]

MOCK_SUPERMARKETS = [
    {
        "id": 1,
        "name": MERCADONA
    },
    {
        "id": 2,
        "name": ALDI
    }
]

MOCKUP_PRODUCTS_SUPERMARKETS = [{
    "id": 1,
    "product_id": 1,
    "supermarket_id": 1,
    "stock": 309,
    "price": 2.99
}]

# print(MOCKUP_PRODUCTS_SUPERMARKETS[0]['supermarket_id'])


# null de javascrip ahora es None

# DECLARAR UNA FUNCIÓN def
def find_object_in_list(target_list=None, key=None, value=None):
    '''Finds an object in a list given its desired key and value

    Arguments :
    - list: lista donde quiero buscar
    - key: clave por la que quiero comparar
    - value: valor que debe tener la clave para devolverme el objeto
    '''
    target_item = None

    if not key:
        raise Exception('No me has pasado una key!')
    elif not value:
        raise Exception('No me has pasado una valor!')
    elif not target_list:
        raise Exception('No me has pasado una lista!')
    else: 
        for item in target_list:
            if item[key] == value:
                target_item= item

    return target_item

target_product_id = 1
target_product_key = "id"

product_one = find_object_in_list(MOCKUP_PRODUCTS, target_product_key, target_product_id)
# SELECT * FROM MOCKUP_PRODUCTS WHERE target_product_key = target_product_id


# print((product_one))
product_name = product_one['name']
product_description = product_one['description']
product_id = product_one['id']

supermarket_with_stock = find_object_in_list(MOCKUP_PRODUCTS_SUPERMARKETS, "product_id", product_id)
product_price = supermarket_with_stock['price']
# print(supermarket_with_stock)
supermarket_id = supermarket_with_stock['supermarket_id']

supermarket = find_object_in_list(MOCK_SUPERMARKETS, 'id', supermarket_id)
supermarket_name = supermarket['name']
# print(supermarket_name)

product_info = f"""
Producto: {product_name}
Descrición: {product_description}
Precio: {product_price}
Hay stock en el supermercado {supermarket_name}
"""
# print(product_info)



















