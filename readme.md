
### API Documentation
(or use http://127.0.0.1:8000/swagger/# )

#### Customers

    Check/Create customers list:
        GET/POST
        http://localhost:8000/api/customers/

    Get/Update/Delete a customer by ID:
        GET/PUT/DELETE
        http://localhost:8000/api/customers/<int:pk>/

    Filter customers by city:
        GET
        http://localhost:8000/api/customers/?city=<str:city>

    Filter customers by email:
        GET
        http://localhost:8000/api/customers/?email=<str:email>
____________________________________________________________________

#### Devices

    Check/Create devices list:
        GET/POST
        http://localhost:8000/api/device/

    Get/Update/Delete a device by ID:
        GET/PUT/DELETE
        http://localhost:8000/api/device/<int:pk>/

    Filter devices by manufacturer:
        GET
        http://localhost:8000/api/device/?manufacturer=<str:manufacturer>

    Filter devices by model:
        GET
        http://localhost:8000/api/device/?model=<str:model>
____________________________________________________________________
