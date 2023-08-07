#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Remove Customer</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.button-container { text-align: center; }')
print('.button { padding: 12px 24px; font-size: 18px; margin: 0 10px; border-radius: 4px; cursor: pointer; }')
print('.yes-button { background-color: green; color: white; }')
print('.no-button { background-color: red; color: white; }')
print('</style>')
print('</head>')
print('<body>')

print('<h2>Remove Customer ({})</h2>'.format(cust_no))

print('<div class="button-container">')
print('<form action="remove_customers.cgi" method="post">')
print('<input type="hidden" name="cust_no" value="{}"/>'.format(cust_no))
print('<h2>Are you sure you want to remove customer ({})?</h2>'.format(cust_no))
print('<br>') 
print('<br>') 
print('<button class="button yes-button" type="submit">Yes</button>')
print('</form>')
print('<a href="app_menu.cgi"><button class="button no-button" type="button">No</button></a>')
print('</div>')


print('</body>')
print('</html>')