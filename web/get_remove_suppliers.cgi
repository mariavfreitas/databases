#!/usr/bin/python3
import cgi
import psycopg2
import login
form = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Remove Supplier</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.button { background-color: red; color: white; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px; }')
print('table { border-collapse: collapse; width: 100%; }')
print('th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }')
print('th { background-color: #f2f2f2; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Remove Supplier</h2>')

print('<h3>Choose a Supplier to be removed:</h3>')
connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    sql = 'SELECT  TIN, name, address, SKU, date FROM supplier;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)


    print('<table>')

    print('<tr>')
    print('<th>TIN</th>')
    print('<th>name</th>')
    print('<th>address</th>')
    print('<th>SKU</th>')
    print('<th>date</th>')
    print('</tr>')

    for row in result:
        print('<tr>')
        print('<td>{}</td>'.format(row[0]))
        print('<td>{}</td>'.format(row[1]))
        print('<td>{}</td>'.format(row[2]))
        print('<td>{}</td>'.format(row[3]))
        print('<td>{}</td>'.format(row[4]))
        print('<td><a href="set_remove_suppliers.cgi?TIN={}" class="button">X</a></td>'.format(row[0]))
        print('</tr>')
    print('</table>')



    cursor.close()
except Exception as e:
    print('<h2>An error occurred.</h2>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()

print('<br>') 

print('<td>')
print('<button type="button" onclick="location.href=\'app_menu.cgi\'" style="font-size: 16px;">Return to App Menu</button>')
print('</td>')

print('</body>')
print('</html>')
