#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
order_no = form.getvalue('order_no')
cust_no = form.getvalue('cust_no')
date = form.getvalue('date')
SKU = form.getvalue('SKU')
qty = form.getvalue('qty')



print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Place Orders</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Place Orders ({})</h2>'.format(order_no))

try:
   
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()


    check_order_no = f'SELECT order_no FROM "order" WHERE order_no = %s;'
    cursor.execute(check_order_no, (order_no,))
    result = cursor.fetchall()
    if result:
        raise Exception(f'Order with the same order number "{order_no}" already exists')


    check_cust_no = f"SELECT cust_no FROM customer WHERE cust_no = %s;"
    cursor.execute(check_cust_no, (cust_no,))
    result = cursor.fetchall()
    if not result:
        raise Exception(f'Customer with the customer number "{cust_no}" does not exist')


    check_sku = f"SELECT SKU FROM product WHERE SKU = %s;"
    cursor.execute(check_sku, (SKU,))
    result = cursor.fetchall()
    if not result:
        raise Exception(f'Product with SKU "{SKU}" does not exist')


    sql = 'INSERT INTO "order" (order_no, cust_no, date) VALUES (%s, %s, %s);'
    cursor.execute(sql, (order_no, cust_no, date))


    sql = 'INSERT INTO contains (order_no, SKU, qty) VALUES (%s, %s, %s);'
    cursor.execute(sql, (order_no, SKU, qty))

    print('<div class="text_center">')
    print('<h3>Order Placed</h3>')

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
