import mysql.connector

class DBManager:
    def __init__(self, host, user, password, database):
        # Initialize database connection
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

        # Create orders table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer VARCHAR(255),
                total DECIMAL(10, 2),
                status VARCHAR(50)
            )
        ''')
        self.connection.commit()

    def execute_query(self, query, values=None):
        # Execute a database query
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_one(self, query, values=None):
        # Fetch one result from the database
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def close_connection(self):
        # Close MySQL connection
        self.cursor.close()
        self.connection.close()

class EShopOrder:
    def __init__(self, db_manager, order_id):
        # Initialize order details based on order ID
        self.order_id = order_id
        self.db_manager = db_manager
        self.order_data = self.get_order_by_id()

    def get_order_by_id(self):
        # Retrieve order details by order ID from the database
        query = 'SELECT * FROM orders WHERE id = %s'
        values = (self.order_id,)
        return self.db_manager.fetch_one(query, values)

    def display_order(self):
        # Display order details
        if self.order_data:
            print(f"Order ID: {self.order_data[0]}, Customer: {self.order_data[1]}, Total: {self.order_data[2]}, Status: {self.order_data[3]}")
        else:
            print("Order not found.")

    def update_order(self, new_data):
        # Update order details in the database
        query = 'UPDATE orders SET customer = %s, total = %s, status = %s WHERE id = %s'
        values = (new_data['customer'], new_data['total'], new_data['status'], self.order_id)
        self.db_manager.execute_query(query, values)

        # Update local order data
        self.order_data = self.get_order_by_id()

    def delete_order(self):
        # Delete order from the database
        query = 'DELETE FROM orders WHERE id = %s'
        values = (self.order_id,)
        self.db_manager.execute_query(query, values)

    def set_order_status(self, new_status):
        # Set order status in the database
        query = 'UPDATE orders SET status = %s WHERE id = %s'
        values = (new_status, self.order_id)
        self.db_manager.execute_query(query, values)

        # Update local order data
        self.order_data = self.get_order_by_id()

# Example usage:

# Initialize DBManager
db_manager = DBManager(host='your_mysql_host', user='your_mysql_user', password='your_mysql_password', database='your_mysql_database')

# Instantiate EShopOrder with order ID
order_system = EShopOrder(db_manager, order_id=1)

# Display order details
order_system.display_order()

# Update order
order_system.update_order({'customer': 'John Updated', 'total': 120.00, 'status': 'Paid'})

# Display updated order details
order_system.display_order()

# Set order status
order_system.set_order_status('Shipped')

# Display order details after status update
order_system.display_order()

# Delete order
order_system.delete_order()

# Display order details after deletion
order_system.display_order()  # This should show "Order not found."

# Close MySQL connection
db_manager.close_connection()
