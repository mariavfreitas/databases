#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()


print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Register Customer</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Customer</h2>')


print('<h3>Choose attributes of the new customer:</h3>')

print('<form action="register_customers.cgi" method="post">')

print('<p>Customer Number: <input type="text" name="cust_no"/></p>')
print('<p>Name: <input type="text" name="name"/></p>')
print('<p>Email: <input type="text" name="email"/></p>')
print('<p>Phone number: <input type="text" name="phone"/></p>')
print('<p>Address: <input type="text" name="address"/></p>')
print('<div class="text_center">')
print('<br>')
print('<br>')
print('<br>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('<br>')
print('<br>')

print('<td>')
print('<button type="button" onclick="location.href=\'app_menu.cgi\'" style="font-size: 16px;">Return to App Menu</button>')
print('</td>')
print('</div>')
print('</body>')
print('</html>')