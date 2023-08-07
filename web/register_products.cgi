#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
SKU = form.getvalue('SKU')
name = form.getvalue('name')
description = form.getvalue('description')
price = form.getvalue('price')
ean = form.getvalue('ean')


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Register Product</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Product ({})</h2>'.format(SKU))

try:
   
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()

    check_sku = "SELECT SKU FROM product WHERE SKU = %s;"
    cursor.execute(check_sku, (SKU,))
    result = cursor.fetchall()
    if result:
        raise Exception(f'Product with the same SKU "({SKU})" already exists')

    
    sql = "INSERT INTO product (SKU, name, description, price, ean) VALUES (%s, %s, %s, %s, %s);"
    data = (SKU, name, description, price, ean)
    cursor.execute(sql, data)


    print('<div class="text_center">')
    print('<h3>Product Registred</h3>')

    connection.commit()
    
    cursor.close() 
except Exception as e:

    print('<h2>An error occurred. :(</h2>') 
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close() 


print('<br>')
print('<br>')

print('<td>')
print('<button type="button" onclick="location.href=\'app_menu.cgi\'" style="font-size: 16px;">Return to App Menu</button>')
print('</td>')
print('</div>')
print('</body>')
print('</html>')