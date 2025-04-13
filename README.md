🍨 IglooApi
IglooApi is a RESTful API built using Django Rest Framework (DRF) to manage an ice cream shop's operations. It provides endpoints to handle various aspects of the shop, including products, orders, and customer interactions.

🚀 Features
Product Management: Create, read, update, and delete ice cream products.

Order Processing: Handle customer orders efficiently.

Customer Management: Maintain customer information and preferences.

Authentication: Secure endpoints using DRF's authentication mechanisms.

Admin Interface: Utilize Django's built-in admin panel for backend management.

📂 Project Structure
IglooApi/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── IglooApi/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt





✅Public Access (No Auth Required)
GET /icecream/ — List all ice creams

GET /icecream/{id}/ — Get single ice cream 

GET /favourite/ — List all favourites

POST /favourite/ — Add favourite

GET /favourite/{username}/ — Get user favourites

PUT /favourite/{username}/ — Update favourite

DELETE /favourite/{username}/ — Delete favourite



🔐Admin Only
POST /icecream/ — Create ice cream

PUT /icecream/{id}/ — Update ice cream

DELETE /icecream/{id}/ — Delete ice cream


🔐Authenticated Users
GET /order/ — User: own orders | Admin: all orders

POST /order/ — Create order (user auto-assigned)

GET /order/{username}/ — Get user orders

PUT /order/{username}/ — Update user order

DELETE /order/{username}/ — Delete user order

GET /payment/ — List payments

POST /payment/ — Create payment

GET /payment/{order_id}/ — Get payment by order

PUT /payment/{order_id}/ — Update payment

DELETE /payment/{order_id}/ — Delete payment


