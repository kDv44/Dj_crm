API Endpoints:

    Check customers list:
    GET http://localhost:8000/api/customers/

    Create a new customer:
    POST http://localhost:8000/api/customers/

    Get a customer by ID:
    GET http://localhost:8000/api/customers/<int:pk>/

    Get a customer by Email:
    GET http://localhost:8000/api/customers/email/<str:email>/

    Update a customer by ID:
    PUT http://localhost:8000/api/customers/<int:pk>/

    Delete a customer by ID:
    DELETE http://localhost:8000/api/customers/<int:pk>/

    Check customers by city:
    GET http://localhost:8000/api/customers/city/<str:city>/