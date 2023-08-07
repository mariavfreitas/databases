#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()



print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Register Supplier</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Supplier</h2>')


print('<h3>Choose attributes of the new supplier:</h3>')

print('<form action="register_suppliers.cgi" method="post">')

print('<p>TIN: <input type="text" name="TIN"/></p>')
print('<p>Name: <input type="text" name="name"/></p>')
print('<p>Address: <input type="text" name="address"/></p>')
print('<p>SKU: <input type="text" name="SKU"/></p>')
print('<p>Date: <input type="text" name="date"/></p>')
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