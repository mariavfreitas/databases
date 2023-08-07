#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
order_no = form.getvalue('order_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Order Payment</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.button-container { text-align: center; }')
print('.button { padding: 12px 24px; font-size: 18px; margin: 0 10px; border-radius: 4px; cursor: pointer; }')
print('.yes-button { background-color: green; color: white; }')
print('.no-button { background-color: red; color: white; }')
print('</style>')
print('</head>')
print('<body>')

print('<h2>Order ({}) Payment</h2>'.format(order_no))

print('<div class="button-container">')
print('<form action="simulate_payment.cgi" method="post">')
print('<input type="hidden" name="order_no" value="{}"/>'.format(order_no))
print('<h2>Are you sure you want to complete order ({}) payment?</h2>'.format(order_no))
print('<br>') 
print('<br>') 
print('<button class="button yes-button" type="submit">Yes</button>')
print('</form>')
print('<a href="app_menu.cgi"><button class="button no-button" type="button">No</button></a>')
print('</div>')


print('</body>')
print('</html>')


