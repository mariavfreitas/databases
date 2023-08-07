#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()
order_no = form.getvalue('order_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Order Payment</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Order ({}) Payment</h2>'.format(order_no))


connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    check_order_no = 'SELECT order_no FROM "order" WHERE order_no = %s;'
    cursor.execute(check_order_no, (order_no,))
    result = cursor.fetchall()
    if not result:
        raise Exception(f'Order with order number ({order_no}) does not exist')


    get_cust_no = 'SELECT cust_no FROM "order" WHERE order_no = %s;'
    cursor.execute(get_cust_no, (order_no,))
    result = cursor.fetchall()

    if not result:
        raise Exception(f'Order "({order_no})" format is incorrect')

    
    cust_no = result[0][0]

    check_if_paid = 'SELECT order_no FROM pay WHERE order_no = %s;'
    cursor.execute(check_if_paid, (order_no,))
    result = cursor.fetchone()  # Use fetchone() instead of fetchall()

    if result is not None:
        raise Exception(f'Order with order number ({order_no}) has already been paid')

    

    sql = "INSERT INTO pay (order_no, cust_no) VALUES (%s, %s);"
    cursor.execute(sql, (order_no, cust_no))

    print('<br>')

    print('<div class="text_center">')
    print('<h3>Payment Completed</h3>')
    

    connection.commit()

 
    cursor.close()

except Exception as e:

    print('<h2>An error occurred.</h2>')
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