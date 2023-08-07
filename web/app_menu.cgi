#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>G30 APP</title>')
print('<style>')
print('body { font-family: Arial, sans-serif; }')
print('.button-red{ background-color: red; color: white; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px; }')
print('.button-white { background-color: white; color: black; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px; border: 1px solid black; }')
print('.button-purple{ background-color: purple; color: white; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px; }')
print('.button-green{ background-color: green; color: white; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px; }')
print('table { border-collapse: collapse; width: 100%; }')
print('th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }')
print('th { background-color: #f2f2f2; }')
print('.centered { text-align: center; }')
print('</style>')
print('</head>')
print('<body>')
print('<h1>G30 APP - Sales Management System</h1>')
print('<h1></h1>')

print('<table border="0" cellspacing="5">')
print('<tr>')
print('<td>')
print('<td ><a href="list_products.cgi" class="button-white">Products List</a></td>')
print('</td>')
print('<td>')
print('<td ><a href="list_suppliers.cgi" class="button-white">Suppliers List</a></td>')
print('</td>')
print('<td>')
print('<td ><a href="list_customers.cgi" class="button-white">Customers List</a></td>')
print('</td>')
print('<td>')
print('<td ><a href="list_orders.cgi" class="button-white">Orders List</a></td>')
print('</td>')
print('</tr>')
print('</table>')


print('<h2>Available Operations:</h2>')
print('<h1></h1>')
connection = None
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    print('<table border="0" cellspacing="5">')
    print('<tr>')
    print('<td>')
    print('<td><a href="get_register_products.cgi" class="button-green">Register Product</a></td>')
    print('</td>')
    print('<td>')
    print('<td><a href="get_register_suppliers.cgi" class="button-green">Register Supplier</a></td>')
    print('</td>')
    print('<td>')
    print('<td><a href="get_remove_products.cgi" class="button-red">Remove Product</a></td>')
    print('</td>')
    print('<td>')
    print('<td><a href="get_remove_suppliers.cgi" class="button-red">Remove Supplier</a></td>')
    print('</td>')
    print('</tr>')


    print('<tr style="height: 30px;"></tr>')

    print('<tr>')
    print('<td>')
    print('<td><a href="get_change_product_prices.cgi" class="button-purple">Change Product Price</a></td>')
    print('</td>')
    print('<td>')
    print('<td><a href="get_change_product_descriptions.cgi" class="button-purple">Change Product Description</a></td>')
    print('</td>')
    print('</tr>')


    print('<tr style="height: 30px;"></tr>')


 
    print('<tr>')
    print('<td>')
    print('<td><a href="get_register_customers.cgi" class="button-green">Register Customer</a></td>')
    print('</td>')
    print('<td>')
    print('<td><a href="get_remove_customers.cgi" class="button-red">Remove Customer</a></td>')
    print('</td>')
    print('</tr>')


    print('<tr style="height: 30px;"></tr>')


    print('<tr>')
    print('<td>')
    print('<td><a href="get_place_orders.cgi" class="button-green">Place Order</a></td>')
    print('</td>')
    print('</tr>')


    print('<tr style="height: 30px;"></tr>')


    print('<tr>')
    print('<td>')
    print('<td><a href="get_simulate_payment.cgi" class="button-green">Simulate Order Payment</a></td>')
    print('</td>')
    print('</tr>')

    print('</table>')

    cursor.close()
except Exception as e:

    print('<h2>An error occurred.</h2>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')