#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')
name = form.getvalue('name')
address = form.getvalue('address')
phone = form.getvalue('phone')
email = form.getvalue('email')


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Register Customer</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Customer ({})</h2>'.format(cust_no))

try:
   
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    data = (cust_no, name, email, phone, address)

    check_cust_no = "SELECT * FROM customer WHERE cust_no = %s;"
    cursor.execute(check_cust_no, (cust_no,))
    result = cursor.fetchall()
    if result:
        raise Exception(f'Customer with the same cust_no "({cust_no})" already exists')

    
    check_email = "SELECT email FROM customer WHERE email = %s;"
    cursor.execute(check_email, (email,))
    resulte = cursor.fetchall()
    if resulte:
        raise Exception(f'Customer with the same email "({email})" already exists')

    
    sql = "INSERT INTO customer (cust_no, name, email, phone, address) VALUES (%s, %s, %s, %s, %s);"
    data = (cust_no, name, email, phone, address)
    cursor.execute(sql, data)


    print('<div class="text_center">')
    print('<h3>Customer Registred</h3>')

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



