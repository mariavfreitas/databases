#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
SKU = form.getvalue('SKU')
name = form.getvalue('name')
address = form.getvalue('address')
TIN = form.getvalue('TIN')
date = form.getvalue('date')


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Register Supplier</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Supplier ({})</h2>'.format(TIN))

try:
   
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    data = (TIN, name, address, SKU, date)

    check_tin = "SELECT TIN FROM supplier WHERE TIN = %s;"
    cursor.execute(check_tin, (TIN,))
    result = cursor.fetchall()
    if result:
        raise Exception(f'Supplier with the same TIN "({TIN})" already exists')

    
    sql = "INSERT INTO supplier (TIN, name, address, SKU, date) VALUES (%s, %s, %s, %s, %s);"
    data = (TIN, name, address, SKU, date)
    cursor.execute(sql, data)


    print('<div class="text_center">')
    print('<h3>Supplier Registred</h3>')

    connection.commit()
    
    cursor.close() 
except Exception as e:

    print('<h1>An error occurred. :(</h1>') 
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

