# 

# prices = {
#         ('Desktop', 'Dell', 'Intel Core i3'): 45000,
#         ('Desktop', 'Dell', 'Intel Core i5'): 50000,
#         ('Laptop', 'Dell', 'Intel Core i3'): 60000,
#         ('Laptop', 'Dell', 'Intel Core i5'): 70000,}
# print(prices)

# import tkinter as tk

# def get_spinbox_value():
#     value = spinbox.get()
#     print("Selected value:", value)

# # Create the main window
# root = tk.Tk()
# root.title("Spinbox Example")

# # Create a Spinbox widget
# spinbox = tk.Spinbox(root, from_=0, to=10, width=5)
# spinbox.pack(padx=20, pady=20)

# # Create a button to get the Spinbox value
# get_value_btn = tk.Button(root, text="Get Value", command=get_spinbox_value)
# get_value_btn.pack()

# # Start the Tkinter event loop
# root.mainloop()


























# import itertools

# # Define the lists of options
# category = ['Tablet']
# company = ['Dell', 'Lenovo', 'HP', 'Acer']
# processors = ['Snapdragon 888', 'Intel Core i5', 'AMD Ryzen 7']
# storage_options = ['128GB SSD', '256GB SSD', '1TB HDD']
# colors = ["White", "Grey", "Quite Blue", "Black", "Emerald Green"]
# assov = ['Hard Disk', 'Mouse', 'Keyboard', 'Monitor','SSD','Speaker','MicroPhone']

# # Generate all possible combinations including company name
# combinations = list(itertools.product(category,company, assov, storage_options))

# # Initialize a dictionary to store prices for each combination
# prices = {}

# # Define price rules based on conditions
# for combo in combinations:
#     catagory_val,company_val, processor_val, storage_val, color_val = combo
#     price = 0  # Default price for each combination
    
    
#     # Store the price in the dictionary using the combination as the key
#     prices[combo] = price

# # Print the prices dictionary
# for combo, price in prices.items():
#     print(combo, ':', price,',')

# ser = {'Assistance':2000,'Maintainace':2500,'Reapir':2000,'Instalation':2500}
# sv = input()
# if sv in ser:
#     print(ser[sv])




# Define the categories, companies, processors, storages, and colors
# categories = ['Desktop', 'Laptop', 'Tablet']
# companies = ['Dell', 'Lenovo', 'HP', 'Acer']
# processors = ['Intel Core i3', 'Intel Core i5', 'AMD Ryzen 7']
# storages = ['128GB SSD', '256GB SSD', '1TB HDD']
# colors = ['White', 'Grey', 'Quite Blue', 'Black', 'Emerald Green']

# # Define the prices for each combination
# prices = {}

# # Iterate over each combination and calculate the price
# for category in categories:
#     for company in companies:
#         for processor in processors:
#             for storage in storages:
#                 for color in colors:
#                     key = (category, company, processor, storage, color)
#                     if category == 'Desktop':
#                         base_price = 45000  # Define your base price here for desktops
#                     elif category == 'Laptop':
#                         base_price = 55000  # Define your base price here for laptops
#                     elif category == 'Tablet':
#                         base_price = 35000  # Define your base price here for tablets
#                     # Calculate final price based on additional factors if needed
#                     # For simplicity, adding base_price as the final price in this example
#                     prices[key] = base_price

# # Print the generated prices dictionary
# print(prices)




prices = {}

categories = ['Desktop', 'Laptop', 'Tablet']
companies = ['Dell', 'Lenovo', 'HP', 'Acer']
processors = ['Intel Core i3', 'Intel Core i5', 'AMD Ryzen 7']
storages = ['128GB SSD', '256GB SSD', '1TB HDD']
colors = ['White', 'Grey', 'Quite Blue', 'Black', 'Emerald Green']

# Initialize the prices dictionary with nested structures
for category in categories:
    prices[category] = {}
    for company in companies:
        prices[category][company] = {}
        for processor in processors:
            prices[category][company][processor] = {}
            for storage in storages:
                prices[category][company][processor][storage] = {}
                for color in colors:
                    # Set default price to 0, you can replace it with actual prices
                    prices[category][company][processor][storage][color] = 0

# Example prices for Desktop - Dell - Intel Core i3 configurations
prices['Desktop']['Dell']['Intel Core i3']['128GB SSD']['White'] = 45000
prices['Desktop']['Dell']['Intel Core i3']['128GB SSD']['Grey'] = 45000
prices['Desktop']['Dell']['Intel Core i3']['256GB SSD']['White'] = 47500
prices['Desktop']['Dell']['Intel Core i3']['256GB SSD']['Grey'] = 47500

# Add prices for other configurations as needed

# Print the prices dictionary to verify the structure and values
print(prices)
