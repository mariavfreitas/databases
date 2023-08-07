#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Remove Customer</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Remove Customer ({})</h2>'.format(cust_no))

connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    sql = 'DELETE FROM customer WHERE cust_no = %s;'
    data = (cust_no,)
    print('<div class="text_center">')
    print('<h3>{}</h3>'.format(sql % data))
    cursor.execute(sql, data)

    connection.commit()
    cursor.close()

except Exception as e:

    print('<h1>An error occurred.</h1>')
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

