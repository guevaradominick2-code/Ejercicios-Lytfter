#Cree un diccionario que guarde el total de ventas de cada UPC.

sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

total_sales = {}

for sale in sales:
    for item in sale ["items"]:
        upc = item ["upc"]
        price = item ["unit_price"]

        if upc in total_sales:
            total_sales[upc] = total_sales[upc] + price
        else:
            total_sales[upc] = price

print(total_sales)
print(60*"__")

#-------------------------------------------------------------------------------------------------------------
#Agrupar empleados por departamento

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments_areas = {}

for employee in employees:
    department = employee["department"]
    
    employee_info = {
        "name": employee["name"],
        "email": employee["email"]
    }
    
    if department in departments_areas:
        departments_areas[department].append(employee_info)
    else:
        departments_areas[department] = [employee_info]

print(departments_areas)
print(60*"__")

#-------------------------------------------------------------------------------------------------------------
#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


total_sales2 = {}

for information in products:
    sold_category = information["category"]
    sale = information["price"]

    if sold_category in total_sales2:
        total_sales2[sold_category] = total_sales2[sold_category] + sale
    else:
        total_sales2[sold_category] = sale
    


    
	

    

    
print(f"Resultado de total de ventas por categoria: {total_sales2}")






