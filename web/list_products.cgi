#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>List Products</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('table { border-collapse: collapse; width: 100%; }')
print('th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }')
print('th { background-color: #f2f2f2; }')
print('</style>')
print('</head>')
print('<body>')
print('<h1>List of Products</h1>')
connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    sql = 'SELECT * FROM product;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    print('<table>')

    print('<tr>')
    print('<th>SKU</th>')
    print('<th>name</th>')
    print('<th>description</th>')
    print('<th>price</th>')
    print('<th>ean</th>')
    print('</tr>')

    for row in result:
        print('<tr>')
        print('<td>{}</td>'.format(row[0]))
        print('<td>{}</td>'.format(row[1]))
        print('<td>{}</td>'.format(row[2]))
        print('<td>{}</td>'.format(row[3]))
        print('<td>{}</td>'.format(row[4]))
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
