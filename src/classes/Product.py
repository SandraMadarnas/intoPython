# init hace ref a la funcion Product, debe recibir como parametro self
# fregona = Product()

id = 0

products_table = []


def inset_into(item, table): return table.append(item)
# lambda () => {}


class Product:
    def __init__(self, name, description, category, brand):
        global id
        self.id += 1
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand


def create(self):
        insert_into(self, products_table)

    # # DESPUES DE DEFINIR __INIT__ PODEMOS DEFINIR MAS METODOS
    # # Y DESPUES PUEDO USAR ESOS METODOS CON .READ
    # def read(self):
    #     return select(table=PRODUCTS_LIST, where=[("id", self.id)])


fregona = Product(
    brand="Mileda",
    name="Fregona de microfibra",
    description=''' Fregona de microfibra super buena
#     blablabla''',
    category="Productos de limpieza"
)

print(fregona.name)

print("First: ", products_table)

fregona.create()

print("Second: ", products_table)