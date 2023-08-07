#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Register Product</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h2>Register Product</h2>')


print('<h3>Choose attributes of the new product:</h3>')

print('<form action="register_products.cgi" method="post">')

print('<p>SKU: <input type="text" name="SKU"/></p>')
print('<p>Name: <input type="text" name="name"/></p>')
print('<p>Description: <input type="text" name="description"/></p>')
print('<p>Price: <input type="text" name="price"/></p>')
print('<p>EAN: <input type="text" name="ean"/></p>')
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
