#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()
TIN = form.getvalue('TIN')


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Remove Supplier</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Remove Supplier ({})</h2>'.format(TIN))

connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    
    sql = 'DELETE FROM supplier WHERE TIN = %s;'
    data = (TIN,)
    print('<div class="text_center">')
    print('<h3>{}</h3>'.format(sql % data))
    cursor.execute(sql, data)


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

