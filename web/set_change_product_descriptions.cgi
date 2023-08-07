#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
SKU = form.getvalue('SKU')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Change Product</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.text_center { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')

print('<h2>Change description of product ({})</h2>'.format(SKU))

print('<form action="change_product_descriptions.cgi" method="post">')
print('<p><input type="hidden" name="SKU" value="{}"/></p>'.format(SKU))
print('<p>New description: <input type="text" name="description"/></p>')
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