import csv
import random
from faker import Faker
from faker.providers import phone_number
from datetime import datetime, timedelta

# Set up Faker with Indian locale
fake = Faker('en_IN')
fake.add_provider(phone_number)

# Number of records to generate
num_records = 10000

# Define the date range (10 days)
start_date = datetime(2025, 1, 1)  # Start date: March 1, 2025
end_date = start_date + timedelta(days=9)  # 10 days including start date
filename = f"sales_{start_date.strftime('%Y%m%d')}_to_{end_date.strftime('%Y%m%d')}.csv"

# Define Indian states to include
states = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Maharashtra']

# Define product categories and sample products
products = {
    'Electronics': [
        ('EL001', 'Smartphone', 15000, 30000),
        ('EL002', 'Laptop', 35000, 90000),
        ('EL003', 'Tablet', 10000, 25000),
        ('EL004', 'Headphones', 1500, 5000),
        ('EL005', 'Smart TV', 25000, 75000),
        ('EL006', 'Smartwatch', 2000, 15000),
        ('EL007', 'Bluetooth Speaker', 1500, 7000),
        ('EL008', 'Wireless Earbuds', 2000, 8000),
        ('EL009', 'Gaming Console', 30000, 60000),
        ('EL010', 'External Hard Drive', 4000, 12000),
    ],
    'Clothing': [
        ('CL001', 'T-Shirt', 500, 1500),
        ('CL002', 'Jeans', 1000, 3000),
        ('CL003', 'Formal Shirt', 800, 2500),
        ('CL004', 'Saree', 1500, 10000),
        ('CL005', 'Kurta Set', 1200, 4000),
        ('CL006', 'Hoodie', 1000, 4000),
        ('CL007', 'Jacket', 2000, 8000),
        ('CL008', 'Track Pants', 700, 2500),
        ('CL009', 'Shorts', 500, 2000),
        ('CL010', 'Sweater', 1500, 5000),
    ],
    'Home & Kitchen': [
        ('HK001', 'Pressure Cooker', 800, 3000),
        ('HK002', 'Mixer Grinder', 1500, 5000),
        ('HK003', 'Bedsheet Set', 600, 2000),
        ('HK004', 'Dinner Set', 1000, 4000),
        ('HK005', 'Water Purifier', 8000, 15000),
        ('HK006', 'Microwave Oven', 5000, 20000),
        ('HK007', 'Air Fryer', 4000, 15000),
        ('HK008', 'Vacuum Cleaner', 3000, 12000),
        ('HK009', 'Induction Cooktop', 2000, 7000),
        ('HK010', 'Recliner Chair', 10000, 25000),
    ],
    'Books': [
        ('BK001', 'Fiction Novel', 250, 500),
        ('BK002', 'Self-Help Book', 300, 600),
        ('BK003', 'Cookbook', 400, 800),
        ('BK004', 'Children\'s Book', 200, 450),
        ('BK005', 'Academic Textbook', 500, 1200),
        ('BK006', 'Mystery Novel', 350, 700),
        ('BK007', 'Biography', 400, 900),
        ('BK008', 'Science Fiction', 500, 1000),
        ('BK009', 'Poetry Collection', 300, 800),
        ('BK010', 'Graphic Novel', 600, 1500),
    ],
    'Beauty & Personal Care': [
        ('BP001', 'Face Wash', 200, 600),
        ('BP002', 'Shampoo', 250, 800),
        ('BP003', 'Moisturizer', 300, 1200),
        ('BP004', 'Lipstick', 500, 2000),
        ('BP005', 'Perfume', 1000, 5000),
        ('BP006', 'Hair Straightener', 1500, 5000),
        ('BP007', 'Body Lotion', 250, 900),
        ('BP008', 'Sunscreen', 300, 1000),
        ('BP009', 'Beard Trimmer', 1000, 4000),
        ('BP010', 'Makeup Kit', 1500, 7000),
    ],
    'Sports & Fitness': [
        ('SF001', 'Treadmill', 20000, 70000),
        ('SF002', 'Dumbbell Set', 2000, 10000),
        ('SF003', 'Yoga Mat', 500, 2000),
        ('SF004', 'Cricket Bat', 1500, 5000),
        ('SF005', 'Football', 500, 2500),
        ('SF006', 'Basketball', 600, 2500),
        ('SF007', 'Cycling Helmet', 1000, 4000),
        ('SF008', 'Skipping Rope', 300, 1200),
        ('SF009', 'Resistance Bands', 500, 3000),
        ('SF010', 'Boxing Gloves', 1500, 5000),
    ],
}

# Payment methods
payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash on Delivery', 'EMI']

# Order statuses
order_statuses = ['Delivered', 'Shipped', 'Processing', 'Cancelled', 'Returned']

# Generate a random date within the specified 10-day range
def random_date_in_range():
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates + 1)  # +1 to include end date
    return start_date + timedelta(days=random_number_of_days)

# CSV file creation
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Order ID', 'Order Date', 'Customer Name', 'Email', 'Phone Number', 
                 'Address', 'City', 'State', 'Pincode', 'Product ID', 'Product Name', 
                 'Category', 'Units', 'Price Per Unit', 'Total Amount', 'Payment Method', 'Order Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Generate records
    for i in range(1, num_records + 1):
        # Generate unique order ID
        order_id = f"ORD{fake.unique.random_number(digits=7)}"
        
        # Select random state and generate address
        state = random.choice(states)
        
        # Generate random category and product
        category = random.choice(list(products.keys()))
        product_id, product_name, min_price, max_price = random.choice(products[category])
        price_per_unit = round(random.uniform(min_price, max_price), 2)
        
        # Generate random units between 1 and 5
        units = random.randint(1, 5)
        total_amount = round(price_per_unit * units, 2)
        
        # Generate order date within the specified range
        order_date = random_date_in_range().strftime('%Y-%m-%d')
        
        # Write record to CSV
        writer.writerow({
            'Order ID': order_id,
            'Order Date': order_date,
            'Customer Name': fake.name(),
            'Email': fake.email(),
            'Phone Number': fake.phone_number(),
            'Address': fake.street_address(),
            'City': fake.city(),
            'State': state,
            'Pincode': fake.postcode(),
            'Product ID': product_id,
            'Product Name': product_name,
            'Category': category,
            'Units': units,
            'Price Per Unit': price_per_unit,
            'Total Amount': total_amount,
            'Payment Method': random.choice(payment_methods),
            'Order Status': random.choice(order_statuses)
        })

print(f"Generated {num_records} e-commerce records for Indian states from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
print(f"Data saved to {filename}")