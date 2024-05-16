# invoices-assessment

This API allows you to manage invoices and their details.


## Installation

1. Clone the repository to your local machine.
```bash
git clone https://github.com/snehalkr3030/Django-Assignment.git
```

2. Install the required packages using pip.
```bash
pip install -r requirements.txt
```
3. Run the Django makemigrations.
```bash
python manage.py makemigrations
```

4. Run the Django migrations.
```bash
python manage.py migrate
```


5. Run the Django server.
```bash
python manage.py runserver
```



## Endpoints

### 1. Create Invoice

- URL: `POST /invoices/`
- Create a new invoice with associated details.
- Request Body:
  ```json
  {
      "date": "2024-02-17",
      "customer_name": "Test Customer 1",
      "invoice_details": [
          {
              "description": "Test Description 1",
              "quantity": 1,
              "unit_price": 10,
              "price": 10
          },
          {
              "description": "Test Description 2",
              "quantity": 2,
              "unit_price": 20,
              "price": 40
          }
      ]
  }
  ```

### 2. Get Invoices

- URL: `GET /invoices/`
- Retrieve a list of all invoices.

### 3. Get Invoice Details List

- URL: `GET /invoices/<invoice_id>/details/`
- Retrieve a list of details associated with a specific invoice.

### 4. Update Invoice

- URL: `PUT /invoices/<invoice_id>/`
- Update an existing invoice.
- Request Body:
  ```json
  {
      "date": "2024-02-17",
      "customer_name": "Updated Test Customer"
  }
  ```

### 5. Delete Invoice

- URL: `DELETE /invoices/<invoice_id>/`
- Delete an existing invoice.

### 6. Create Invoice Detail

- URL: `POST /invoices/<invoice_id>/details/`
- Create a new detail associated with a specific invoice.
- Request Body:
  ```json
  {
      "description": "New Test Description",
      "quantity": 3,
      "unit_price": 15,
      "price": 45
  }
  ```

### 7. Update Invoice Detail

- URL: `PUT /invoices/<invoice_id>/details/<detail_id>/`
- Update an existing detail associated with a specific invoice.
- Request Body:
  ```json
  {
      "description": "Updated Test Description",
      "quantity": 2,
      "unit_price": 25,
      "price": 50
  }
  ```

### 8. Delete Invoice Detail

- URL: `DELETE /invoices/<invoice_id>/details/<detail_id>/`
- Delete an existing detail associated with a specific invoice.

## Usage

1. Install [Postman](https://www.postman.com/) or any other API client of your choice. if you haven't any API client installed.
2. Copy the provided request URLs and request bodies into Postman or any other API client.
3. Replace `<invoice_id>` and `<detail_id>` with actual IDs obtained from previous requests.
4. Execute the requests to interact with the API endpoints.
5. Ensure that your Django server is running and accessible at the specified URLs.


