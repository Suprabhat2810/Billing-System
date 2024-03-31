from tkinter import *
from tkinter import ttk,messagebox
import random as r
import os,tempfile,smtplib
bill_number = r.randint(100,10000)

def update_combos(event):
    global quantityEntry
    selected_category = catagoryEntry.get()   
    storage_combo.config(values=['Select'])
    storage_combo.current('0')

    if (selected_category in ['Desktop', 'Laptop', 'Tablet']) and (selected_category != 'Accessories'):
                
                if selected_category in ['Tablet']:
                    serviceEntry.config(values=["Assistance","Instalation","Repair"],state='normal')
                    companyEntry.config(values=['Dell', 'Lenovo', 'HP', 'Acer','Samsung'],state='normal')
                    colorEntry.config(values=["White","Grey","Quite Blue","Black","Emerald Green"],state='normal')
                    quantityEntry.config(values=[i for i in range(1,51)],state='normal')
                    processor_combo.config(values= ['Snapdragon 888', 'Intel Core i5', 'AMD Ryzen 7'],state='normal')
                    storage_combo.config(values=['128GB SSD', '256GB SSD','500GB HDD' '1TB HDD'],state='normal')
                else:
                    processor_combo.config(values= ['Intel Core i3', 'Intel Core i5', 'AMD Ryzen 7'],state='normal')
                    companyEntry.config(state='normal')
                    storage_combo.config(values=['128GB SSD', '256GB SSD', '1TB HDD'],state='normal')
                    serviceEntry.config(values=["Assistance","Instalation","Maintainance","Repair"],state='normal')
                    colorEntry.config(values=["White","Grey","Quite Blue","Black","Emerald Green"],state='normal')
                    quantityEntry.config(values=[i for i in range(50)],state='normal')
                    assoEntry.config(values=['Hard Disk', 'Mouse', 'Keyboard', 'Monitor','SSD','Speaker','MicroPhone'],state='disabled')


    elif (selected_category == 'Accessories') and (selected_category not in ['Desktop', 'Laptop', 'Tablet']):
                processor_combo.config(values=[], state='disabled')
                storage_combo.config(values=[], state='disabled')
                colorEntry.config(values=[],state='disabled')
                companyEntry.config(values=[],state='normal')
                quantityEntry.config(values=[i for i in range(50)],state='normal')
                serviceEntry.config(state='disabled')
                assoEntry.config(values=['Hard Disk', 'Mouse', 'Keyboard', 'Monitor','SSD','Speaker','MicroPhone'],state='normal')
                

    elif (selected_category == 'Accessories and System') and (selected_category not in ['Desktop', 'Laptop', 'Tablet']):
            processor_combo.config(values= ['Intel Core i3', 'Intel Core i5', 'AMD Ryzen 7'],state='normal')
            companyEntry.config(state='normal')
            storage_combo.config(values=['128GB SSD', '256GB SSD', '1TB HDD'],state='normal')
            colorEntry.config(values=["White","Grey","Quite Blue","Black","Emerald Green"],state='normal')
            quantityEntry.config(values=[i for i in range(50)],state='normal')
            serviceEntry.config(values=["Assistance","Instalation","Maintainance","Repair"])
            assoEntry.config(values=['Hard Disk', 'Mouse', 'Keyboard', 'Monitor','SSD','Speaker','MicroPhone'],state='normal')


    else:
            processor_combo.config(values=[], state='disabled')
            storage_combo.config(values=[], state='disabled')
            assoEntry.config(values=[], state='disabled')
            colorEntry.config(state='disabled')
            quantityEntry.config(state='disabled')
            serviceEntry.config(state='disabled')
            companyEntry.config(state='disabled')




def total_bill():
    global totalb
    global quantityEntry
    selected_category = catagoryEntry.get()
    company = companyEntry.get()
    selected_processor = processor_combo.get()
    storage = storage_combo.get()
    color = colorEntry.get()
    selected_quantity = int(quantityEntry.get())
    sc = serviceEntry.get()
    selected_accessory = assoEntry.get()

    prices = {
    ('Desktop', 'Dell', 'Intel Core i3', '128GB SSD', 'White') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '128GB SSD', 'Grey') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '128GB SSD', 'Black') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Dell', 'Intel Core i3', '256GB SSD', 'White') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '256GB SSD', 'Grey') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '256GB SSD', 'Black') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Dell', 'Intel Core i3', '1TB HDD', 'White') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '1TB HDD', 'Grey') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '1TB HDD', 'Black') : 45000 ,
    ('Desktop', 'Dell', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Desktop', 'Dell', 'Intel Core i5', '128GB SSD', 'White') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '128GB SSD', 'Grey') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '128GB SSD', 'Black') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '256GB SSD', 'White') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '256GB SSD', 'Grey') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '256GB SSD', 'Black') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '1TB HDD', 'White') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '1TB HDD', 'Grey') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '1TB HDD', 'Black') : 47500 ,
    ('Desktop', 'Dell', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 47500 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'White') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Black') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'White') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Black') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'White') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Black') : 52000 ,
    ('Desktop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'White') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Grey') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Black') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'White') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Grey') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Black') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'White') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Grey') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Black') : 49000 ,
    ('Desktop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'White') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Grey') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Black') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'White') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Grey') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Black') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'White') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Grey') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Black') : 52000 ,
    ('Desktop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 52000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'White') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Black') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'White') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Black') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'White') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Black') : 61000 ,
    ('Desktop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 61000 ,
    ('Desktop', 'HP', 'Intel Core i3', '128GB SSD', 'White') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '128GB SSD', 'Grey') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '128GB SSD', 'Black') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'HP', 'Intel Core i3', '256GB SSD', 'White') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '256GB SSD', 'Grey') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '256GB SSD', 'Black') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'HP', 'Intel Core i3', '1TB HDD', 'White') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '1TB HDD', 'Grey') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '1TB HDD', 'Black') : 43000 ,
    ('Desktop', 'HP', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Desktop', 'HP', 'Intel Core i5', '128GB SSD', 'White') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '128GB SSD', 'Grey') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '128GB SSD', 'Black') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '256GB SSD', 'White') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '256GB SSD', 'Grey') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '256GB SSD', 'Black') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '1TB HDD', 'White') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '1TB HDD', 'Grey') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '1TB HDD', 'Black') : 49000 ,
    ('Desktop', 'HP', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 49000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'White') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Black') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'White') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Black') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'White') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Black') : 57000 ,
    ('Desktop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 57000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '128GB SSD', 'White') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '128GB SSD', 'Grey') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '128GB SSD', 'Black') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Acer', 'Intel Core i3', '256GB SSD', 'White') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '256GB SSD', 'Grey') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '256GB SSD', 'Black') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Desktop', 'Acer', 'Intel Core i3', '1TB HDD', 'White') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '1TB HDD', 'Grey') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '1TB HDD', 'Black') : 46000 ,
    ('Desktop', 'Acer', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Desktop', 'Acer', 'Intel Core i5', '128GB SSD', 'White') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '128GB SSD', 'Grey') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '128GB SSD', 'Black') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '256GB SSD', 'White') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '256GB SSD', 'Grey') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '256GB SSD', 'Black') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '1TB HDD', 'White') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '1TB HDD', 'Grey') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '1TB HDD', 'Black') : 52500 ,
    ('Desktop', 'Acer', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 52500 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'White') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Black') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'White') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Black') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'White') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Black') : 60000 ,
    ('Desktop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 60000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '128GB SSD', 'White') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '128GB SSD', 'Grey') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '128GB SSD', 'Black') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Dell', 'Intel Core i3', '256GB SSD', 'White') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '256GB SSD', 'Grey') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '256GB SSD', 'Black') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Dell', 'Intel Core i3', '1TB HDD', 'White') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '1TB HDD', 'Grey') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '1TB HDD', 'Black') : 50000 ,
    ('Laptop', 'Dell', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Laptop', 'Dell', 'Intel Core i5', '128GB SSD', 'White') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '128GB SSD', 'Grey') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '128GB SSD', 'Black') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '256GB SSD', 'White') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '256GB SSD', 'Grey') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '256GB SSD', 'Black') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '1TB HDD', 'White') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '1TB HDD', 'Grey') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '1TB HDD', 'Black') : 65000 ,
    ('Laptop', 'Dell', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 65000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'White') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Black') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'White') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Black') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'White') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Black') : 67000 ,
    ('Laptop', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'White') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Grey') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Black') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'White') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Grey') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Black') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'White') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Grey') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Black') : 58000 ,
    ('Laptop', 'Lenovo', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'White') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Grey') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Black') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'White') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Grey') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Black') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'White') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Grey') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Black') : 67000 ,
    ('Laptop', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 67000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'White') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Black') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'White') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Black') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'White') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Black') : 69000 ,
    ('Laptop', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 69000 ,
    ('Laptop', 'HP', 'Intel Core i3', '128GB SSD', 'White') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '128GB SSD', 'Grey') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '128GB SSD', 'Black') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'HP', 'Intel Core i3', '256GB SSD', 'White') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '256GB SSD', 'Grey') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '256GB SSD', 'Black') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'HP', 'Intel Core i3', '1TB HDD', 'White') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '1TB HDD', 'Grey') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '1TB HDD', 'Black') : 56000 ,
    ('Laptop', 'HP', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Laptop', 'HP', 'Intel Core i5', '128GB SSD', 'White') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '128GB SSD', 'Grey') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '128GB SSD', 'Black') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '256GB SSD', 'White') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '256GB SSD', 'Grey') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '256GB SSD', 'Black') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '1TB HDD', 'White') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '1TB HDD', 'Grey') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '1TB HDD', 'Black') : 62000 ,
    ('Laptop', 'HP', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 62000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'White') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Black') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'White') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Black') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'White') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Black') : 63000 ,
    ('Laptop', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 63000 ,
    ('Laptop', 'Acer', 'Intel Core i3', '128GB SSD', 'White') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '128GB SSD', 'Grey') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '128GB SSD', 'Quite Blue') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '128GB SSD', 'Black') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '128GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Acer', 'Intel Core i3', '256GB SSD', 'White') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '256GB SSD', 'Grey') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '256GB SSD', 'Quite Blue') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '256GB SSD', 'Black') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '256GB SSD', 'Emerald Green') : 0 ,
    ('Laptop', 'Acer', 'Intel Core i3', '1TB HDD', 'White') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '1TB HDD', 'Grey') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '1TB HDD', 'Quite Blue') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '1TB HDD', 'Black') : 59500 ,
    ('Laptop', 'Acer', 'Intel Core i3', '1TB HDD', 'Emerald Green') : 0 ,
    ('Laptop', 'Acer', 'Intel Core i5', '128GB SSD', 'White') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '128GB SSD', 'Grey') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '128GB SSD', 'Black') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '256GB SSD', 'White') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '256GB SSD', 'Grey') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '256GB SSD', 'Black') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '1TB HDD', 'White') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '1TB HDD', 'Grey') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '1TB HDD', 'Black') : 61000 ,
    ('Laptop', 'Acer', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 61000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'White') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Black') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'White') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Black') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'White') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Black') : 64000 ,
    ('Laptop', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 64000,
    ('Tablet', 'Dell', 'Snapdragon 888', '128GB SSD', 'White') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '128GB SSD', 'Grey') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '128GB SSD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '128GB SSD', 'Black') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '128GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '256GB SSD', 'White') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '256GB SSD', 'Grey') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '256GB SSD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '256GB SSD', 'Black') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '256GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '1TB HDD', 'White') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '1TB HDD', 'Grey') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '1TB HDD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '1TB HDD', 'Black') : 65000 ,
    ('Tablet', 'Dell', 'Snapdragon 888', '1TB HDD', 'Emerald Green') : 0 ,
    ('Tablet', 'Dell', 'Intel Core i5', '128GB SSD', 'White') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '128GB SSD', 'Grey') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '128GB SSD', 'Black') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '256GB SSD', 'White') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '256GB SSD', 'Grey') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '256GB SSD', 'Black') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '1TB HDD', 'White') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '1TB HDD', 'Grey') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '1TB HDD', 'Black') : 72000 ,
    ('Tablet', 'Dell', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 72000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'White') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Black') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'White') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Black') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'White') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Black') : 78000 ,
    ('Tablet', 'Dell', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 78000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '128GB SSD', 'White') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '128GB SSD', 'Grey') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '128GB SSD', 'Quite Blue') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '128GB SSD', 'Black') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '128GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '256GB SSD', 'White') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '256GB SSD', 'Grey') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '256GB SSD', 'Quite Blue') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '256GB SSD', 'Black') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '256GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '1TB HDD', 'White') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '1TB HDD', 'Grey') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '1TB HDD', 'Quite Blue') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '1TB HDD', 'Black') : 60000 ,
    ('Tablet', 'Lenovo', 'Snapdragon 888', '1TB HDD', 'Emerald Green') : 0 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '128GB SSD', 'White') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Grey') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Black') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '256GB SSD', 'White') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Grey') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Black') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '1TB HDD', 'White') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Grey') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Black') : 75000 ,
    ('Tablet', 'Lenovo', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 75000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'White') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Black') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'White') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Black') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'White') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Black') : 80000 ,
    ('Tablet', 'Lenovo', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 80000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '128GB SSD', 'White') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '128GB SSD', 'Grey') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '128GB SSD', 'Quite Blue') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '128GB SSD', 'Black') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '128GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'HP', 'Snapdragon 888', '256GB SSD', 'White') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '256GB SSD', 'Grey') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '256GB SSD', 'Quite Blue') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '256GB SSD', 'Black') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '256GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'HP', 'Snapdragon 888', '1TB HDD', 'White') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '1TB HDD', 'Grey') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '1TB HDD', 'Quite Blue') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '1TB HDD', 'Black') : 67000 ,
    ('Tablet', 'HP', 'Snapdragon 888', '1TB HDD', 'Emerald Green') : 0 ,
    ('Tablet', 'HP', 'Intel Core i5', '128GB SSD', 'White') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '128GB SSD', 'Grey') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '128GB SSD', 'Black') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '256GB SSD', 'White') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '256GB SSD', 'Grey') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '256GB SSD', 'Black') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '1TB HDD', 'White') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '1TB HDD', 'Grey') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '1TB HDD', 'Black') : 78000 ,
    ('Tablet', 'HP', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 78000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '128GB SSD', 'White') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Black') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '256GB SSD', 'White') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Black') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '1TB HDD', 'White') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Black') : 82000 ,
    ('Tablet', 'HP', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 82000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '128GB SSD', 'White') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '128GB SSD', 'Grey') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '128GB SSD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '128GB SSD', 'Black') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '128GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '256GB SSD', 'White') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '256GB SSD', 'Grey') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '256GB SSD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '256GB SSD', 'Black') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '256GB SSD', 'Emerald Green') : 0 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '1TB HDD', 'White') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '1TB HDD', 'Grey') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '1TB HDD', 'Quite Blue') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '1TB HDD', 'Black') : 65000 ,
    ('Tablet', 'Acer', 'Snapdragon 888', '1TB HDD', 'Emerald Green') : 0 ,
    ('Tablet', 'Acer', 'Intel Core i5', '128GB SSD', 'White') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '128GB SSD', 'Grey') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '128GB SSD', 'Quite Blue') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '128GB SSD', 'Black') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '128GB SSD', 'Emerald Green') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '256GB SSD', 'White') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '256GB SSD', 'Grey') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '256GB SSD', 'Quite Blue') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '256GB SSD', 'Black') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '256GB SSD', 'Emerald Green') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '1TB HDD', 'White') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '1TB HDD', 'Grey') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '1TB HDD', 'Quite Blue') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '1TB HDD', 'Black') : 79000 ,
    ('Tablet', 'Acer', 'Intel Core i5', '1TB HDD', 'Emerald Green') : 79000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'White') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Grey') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Quite Blue') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Black') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '128GB SSD', 'Emerald Green') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'White') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Grey') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Quite Blue') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Black') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '256GB SSD', 'Emerald Green') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'White') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Grey') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Quite Blue') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Black') : 83000 ,
    ('Tablet', 'Acer', 'AMD Ryzen 7', '1TB HDD', 'Emerald Green') : 83000 
    }
    
    ser = {'Assistance':2000,'Maintainace':2500,'Repair':2000,'Instalation':2500}

    accessory_prices = {
        'Dell': {
            'Hardisk': {
                '128GB SSD': 5000,
                '256GB SSD': 5500,
                '1TB HDD': 6000
            }
        },
        'Lenovo': {
            'Hardisk': {
                '128GB SSD': 5050,
                '256GB SSD': 6000,
                '1TB HDD': 6050
            }
        },
        'HP': {
            'Hardisk': {
                '128GB SSD': 5050,
                '256GB SSD': 6000,
                '1TB HDD': 6050
            }
        },
        'Acer': {
            'Hardisk': {
                '128GB SSD': 5050,
                '256GB SSD': 6000,
                '1TB HDD': 6050
            }
        },           
        'Mouse': 700,
        'Keyboard': 750,
        'Microphone':600,
        'Monitor':3500,
        'Speaker':2500
        }
    
    


    if not all([selected_category,company, selected_processor, storage, color]):
        messagebox.showwarning("Incomplete Details", "Please fill in all the details.")
    else:
        if selected_category not in 'Accessories':
            if (selected_category, company, selected_processor, storage, color) in prices:
                if (company in ['Dell','Acer','Lenovo','HP']) and (selected_category == 'Laptop'):
                    per_unit = prices[selected_category, company, selected_processor, storage, color]
                    system = (per_unit * selected_quantity) 
                    gst = ((per_unit * selected_quantity) * 0.12)
                    gst_entry.delete(0,END)
                    gst_entry.insert(0, '12 %')
                    system_bill_entry.delete(0,END)
                    system_bill_entry.insert(0, system)

                    totalb = system + gst

                elif (company in ['Dell','Acer','Lenovo','HP']) and (selected_category == 'Desktop'):
                    per_unit = prices[selected_category, company, selected_processor, storage, color]
                    system = (per_unit * selected_quantity)
                    gst = ((per_unit * selected_quantity) * 0.10)
                    gst_entry.delete(0,END)
                    gst_entry.insert(0, '10 %')
                    system_bill_entry.delete(0,END)
                    system_bill_entry.insert(0, system)
                    totalb = system + gst

                elif (company in ['Dell','Acer','Lenovo','HP']) and (selected_category == 'Tablet'):
                        if selected_quantity >= 20 and company == 'Dell':
                            res = messagebox.askretrycancel("Insufficient Stocks","Shortage of Stocks for Dell")
                            if res:
                                quantityEntry = ttk.Spinbox(cumputer_lable,from_=0, to=19,font=('arial',15,),background="Antique White2")
                                per_unit = prices[selected_category, company, selected_processor, storage, color]
                                system = (per_unit * selected_quantity) 
                                gst = ((per_unit * selected_quantity) * 0.08)
                                gst_entry.delete(0,END)
                                gst_entry.insert(0, '8 %')
                                system_bill_entry.delete(0,END)
                                system_bill_entry.insert(0, system)
                                totalb = system + gst
                        else:
                            per_unit = prices[selected_category, company, selected_processor, storage, color]
                            system = (per_unit * selected_quantity)
                            gst = ((per_unit * selected_quantity) * 0.08)
                            gst_entry.delete(0,END)
                            gst_entry.insert(0, '8 %')
                            system_bill_entry.delete(0,END)
                            system_bill_entry.insert(0, system)
                            totalb = system + gst

                           
            else:
                messagebox.showwarning("Imformation Warning","Please Fill Everything!")

        elif selected_category in ["Accessories"]:
            if all([selected_quantity, company, selected_accessory]) in accessory_prices:
                if assoEntry.get() == 'Hardisk':
                    if company in accessory_prices and storage in accessory_prices[company]['Hardisk']:
                        price_per_unit = accessory_prices[company]['Hardisk'][storage]
                        asso = price_per_unit * selected_quantity
                        gst = asso * 0.08  
                        totalb = asso + gst 
                        assoEntry.delete(0, END)
                        assoEntry.insert(0, asso)
                        system_bill_entry.delete(0, END)
                        system_bill_entry.insert(0, total)

                else:
                    # Get price directly from the dictionary for other accessories
                    if selected_accessory in accessory_prices:
                        price_per_unit = accessory_prices[selected_accessory]
                        asso = price_per_unit * selected_quantity
                        gst = asso * 0.08  # Calculate GST
                        totalb = asso + gst  # Calculate total price including GST
                        assoEntry.delete(0, END)
                        assoEntry.insert(0, asso)
                        system_bill_entry.delete(0, END)
                        system_bill_entry.insert(0, asso)
            else:
                messagebox.showwarning("Imformation Warning","Please Fill Everything!")

    if sc in ser:
        print(ser[sc])
        vl = ser[sc] + 200
        service_entry.delete(0,END)
        service_entry.insert(0, vl)

def save_bill():
    global bill_number
    result = messagebox.askyesno("Listen","Do you want to save the bill")
    if result:
         bill_content = textarea.get(1.0,END)
         file = open(f'bills/{bill_number}.txt','w')
         file.write(bill_content)
         file.close()
         messagebox.showinfo("Happy",f"{bill_number} saved successfully")
         bill_number = r.randint(100,10000)




def bill_area1():
    name = nameEntry.get()
    phone = phoneEntry.get()
    if name == '' or phone == '':
        messagebox.showwarning("Unknown","Please Provide The Name and Number")
    elif quantityEntry.get() == '0':
         messagebox.showwarning("Purchase","Please Buy Something To Produce Bill")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,"\t  ** Welcome **\n\n")
        textarea.insert(END,f"Bill Number : {bill_number}\n\n")
        textarea.insert(END,f"Customer Name : {name}\n\n")
        textarea.insert(END,f"Phone Number : {phone}\n\n")
        textarea.insert(END," ==================================== \n")
        textarea.insert(END," Products           QTY         Price \n")
        textarea.insert(END," ==================================== \n")
        if system_bill_entry.get() != '':
            if service_entry.get() !='':
                textarea.insert(END," {}-{}\t\t      {}\t       {} \n".format(catagoryEntry.get(),companyEntry.get(),quantityEntry.get(),system_bill_entry.get()))
                textarea.insert(END," {}-{}\t\t   {}\t       {} \n".format(serviceEntry.get(),catagoryEntry.get(),quantityEntry.get(),int(service_entry.get())*int(quantityEntry.get())))
                textarea.insert(END," ------------------------------------- \n")
                textarea.insert(END,"GST                             {}\n".format(gst_entry.get()))
                textarea.insert(END,"Total                        {}".format(totalb+int(service_entry.get())*int(quantityEntry.get())))
            else:
                textarea.insert(END," {}-{}\t\t      {}\t       {}\n".format(catagoryEntry.get(),companyEntry.get(),quantityEntry.get(),system_bill_entry.get()))
                # textarea.insert(END," {}-{}\t\t   {}\t       {} ".format(serviceEntry.get(),catagoryEntry.get(),quantityEntry.get(),int(service_entry.get())*int(quantityEntry.get())))
                textarea.insert(END," ------------------------------------- \n")
                textarea.insert(END,"GST                             {}\n".format(gst_entry.get()))
                textarea.insert(END,"Total                        {}".format(totalb+int(service_entry.get())*int(quantityEntry.get())))
                 
        
        elif assoseries_bill_entry.get() != '':
            textarea.insert(END," {}-{}\t\t   {}\t       {} \n".format(catagoryEntry.get(),companyEntry.get(),quantityEntry.get(),assoseries_bill_entry.get()))
            textarea.insert(END," ------------------------------------ \n")
            textarea.insert(END,"GST                             {}\n".format(gst_entry.get()))
            textarea.insert(END,"Total                        {}".format(totalb))
        elif (system_bill_entry,assoseries_bill_entry) != '':
            textarea.insert(END," {}-{}\t\t   {}\t       {} \n".format(catagoryEntry.get(),companyEntry.get(),quantityEntry.get(),system_bill_entry.get()))
            textarea.insert(END," {}-{}\t\t   {}\t       {} ".format(catagoryEntry.get(),companyEntry.get(),quantityEntry.get(),assoseries_bill_entry.get()))
            textarea.insert(END," ------------------------------------- \n")
            textarea.insert(END,"GST                             {}\n".format(gst_entry.get()))
            textarea.insert(END,"Total                        {}".format(totalb))

        save_bill()


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billEntry.get():
            f = open(f'bills\{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
        else:
            messagebox.showerror("Invalid","No Match Found")


def print_bill1():
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror("Void","Bill is Empty")
    else:
         file = tempfile.mktemp('.txt')
         open(file,'w').write(textarea.get(1.0,END))
         os.startfile(file,'print')
                  
def clear1():
     textarea.delete(1.0,END)
    #  catagoryEntry.current(0)
    #  companyEntry.current(0)
     nameEntry.delete(0,END)
     phoneEntry.delete(0,END)
    #  storage_combo.current(0)
    #  quantityEntry.config(0)
    #  colorEntry.current(0)
     system_bill_entry.delete(0,END)
     service_entry.delete(0,END)
     assoseries_bill_entry.delete(0,END)
     gst_entry.delete(0,END)

def send_email():
    def send_gmail():
         try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(sender_entry.get(),pasword_entry.get())
            mess = email_text_area.get(1.0,END)
            ob.sendmail(sender_entry.get(),email_entry.get(),mess)
            ob.quit()
            messagebox.showinfo("Success","Email is sent successfully")
            root1.destroy()
         except:
              messagebox.showerror("Listen","Something Went Wrong")

    if textarea.get(1.0,END) == '\n':
          messagebox.showerror("Void","Nothing to send")
    else:
         root1 = Toplevel()
         root1.title("Payment Receipt")
         root1.resizable(False,False)

         senderFrame = LabelFrame(root1,text="Sender",font=('arial',16,'bold'),bd=8,bg='Antique White2')
         senderFrame.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')

         sender_lable = Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='Antique White2')
         sender_lable.grid(row=0,column=0)

         sender_entry = Entry(senderFrame,font=('arial',14),bd=4,width=23,relief='ridge')
         sender_entry.grid(row=0,column=2,padx=10,pady=10)

         pasword_lable = Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='Antique White2')
         pasword_lable.grid(row=1,column=0)

         pasword_entry = Entry(senderFrame,font=('arial',14),bd=4,width=23,relief='ridge',show='*')
         pasword_entry.grid(row=1,column=2,padx=10,pady=10)

         recipentFrame = LabelFrame(root1,text="Recipent's Address",font=('arial',16,'bold'),bd=8,bg='Antique White2')
         recipentFrame.grid(row=1,column=0,padx=10,pady=10)

         Email_add = Label(recipentFrame,text="Email Address",font=('arial',14,'bold'),bg='Antique White2')
         Email_add.grid(row=0,column=0)

         email_entry = Entry(recipentFrame,font=('arial',14),bd=4,width=23,relief='ridge')
         email_entry.grid(row=0,column=1,padx=5,pady=5)

         message_lable = Label(recipentFrame,text="Message",font=('arial',14,'bold'),bd=4,width=23,bg='Antique White2')
         message_lable.grid(row=2,column=0,padx=10,pady=10)

         email_text_area = Text(recipentFrame,font=('arial',14),bd=4,relief='sunken',width=40,height=11)
         email_text_area.grid(row=3,column=0,padx=5,pady=5)
         email_text_area.insert(END,textarea.get(1.0,END))

         send_button = Button(recipentFrame,text='Send',font=('arial',14,'bold'),command=send_gmail)
         send_button.grid(row=4,column=0,padx=10,pady=10)

         root1.mainloop()

def quit_window():
     root.destroy()
#GUI
         
root = Tk()
root.title("Billing System")
root.geometry("1270x685")
root.resizable(False,False)
root.iconbitmap('invoice.ico')

#adding the heading 
heading_lbl = Label(root,text="S.C Private Limited",font=('times new roman',30,'bold'),relief='groove',
                    bg='Antique White2',bd=12)
heading_lbl.pack(fill='x')


#adding the costomer details
c_lable = LabelFrame(root,text="Customer Details",bd=8,bg="Antique White2",relief='groove',font=('times new roman',15,'bold'))
c_lable.pack(fill='x')

name_lable = Label(c_lable,text='Name',font=('times new roman',15,'bold'),bg="Antique White2")
name_lable.grid(row=0,column=0,padx=20,pady=2)

nameEntry = Entry(c_lable,font=("arial",15),bd=6,width=16)
nameEntry.grid(row=0,column=1,padx=8)

phone_lable = Label(c_lable,text="Phone Number",font=('times new roman',15,'bold'),bg="Antique White2")
phone_lable.grid(row=0,column=12,padx=20,pady=2)

phoneEntry = Entry(c_lable,font=("arial",15),bd=6,width=16)
phoneEntry.grid(row=0,column=24,padx=8)

bill_lable = Label(c_lable,text="Bill Number",font=("times new roman",15,'bold'),bd=6,bg='Antique White2')
bill_lable.grid(row=0,column=28,padx=20,pady=2)

billEntry = Entry(c_lable,font=('arial',15,'bold'),bd=6,width=16)
billEntry.grid(row=0,column=30,padx=8)

search = Button(c_lable,text="Search",font=('times new roman',15),relief='groove',bd=6,width=12,command=search_bill)
search.grid(row=0,column=60,padx=50,pady=5)


# Creating item-Frame
i_lable = Frame(root)
i_lable.pack(pady=10)

cumputer_lable = LabelFrame(i_lable,text="Catagory",bd=8,bg="Antique White2",relief='groove',font=('times new roman',15,'bold'))
cumputer_lable.grid(row=0,column=0)


l = ["Select Options","i3-500 GB","i5-500 GB","i9-500"]
c = ["Select Options","Desktop","Laptop","Tablet","Accessories","Accessories and System"]
companies = ["Select Options",'Dell', 'Lenovo', 'HP', 'Acer']
com = StringVar()
combo_var = StringVar()

catagory = Label(cumputer_lable,text='Select Type',font=('times new roman',15,'bold'),bg="Antique White2")
catagory.grid(row=0,column=0,padx=20,pady=2)

catagoryEntry = ttk.Combobox(cumputer_lable,textvariable=combo_var,values=c,font=('arial',15,),background="Antique White2")
catagoryEntry.current('0')
catagoryEntry.grid(row=0,column=1,padx=8)
catagoryEntry.bind('<<ComboboxSelected>>', update_combos)


company = Label(cumputer_lable,text="Select Company",bg="Antique White2",font=('times new roman',15,'bold'))
company.grid(row=0,column=4,padx=20,pady=2)

companyEntry = ttk.Combobox(cumputer_lable,textvariable=com,values=companies,font=('arial',15,),background="Antique White2")
companyEntry.grid(row=0,column=6,padx=10)
companyEntry.current('0')

processor = Label(cumputer_lable,text="Select Processor",bg="Antique White2",font=('times new roman',15,'bold'))
processor.grid(row=4,column=0,padx=20,pady=20)

pv = StringVar()
processor_combo = ttk.Combobox(cumputer_lable,textvariable=pv,font=('arial',15,),background="Antique White2") 
processor_combo.grid(row=4,column=1,padx=20)
processor_combo.insert('0',"Select")
processor_combo.config(state='disable')

storage = Label(cumputer_lable,text="Select Storage",bg="Antique White2",font=('times new roman',15,'bold'))
storage.grid(row=4,column=4,padx=20,pady=0)

sv=StringVar()
storage_combo = ttk.Combobox(cumputer_lable, textvariable=sv, font=('arial', 15), background="Antique White2")
storage_combo.grid(row=4, column=6, padx=10)
storage_combo.config(values=['Select','128GB SSD', '256GB SSD', '1TB HDD'],state='disabled')
storage_combo.current('0')


quantity = Label(cumputer_lable,text="Quantity",bg="Antique White2",font=('times new roman',15,'bold'))
quantity.grid(row=8,column=0,padx=20,pady=0)

# qv =StringVar()
quantityEntry = ttk.Spinbox(cumputer_lable,from_=0, to=1000,font=('arial',15,),background="Antique White2")
quantityEntry.grid(row=8,column=1,padx=10)
quantityEntry.insert(0,0)
quantityEntry.config(state='disable')

color = Label(cumputer_lable,text="Color",bg="Antique White2",font=('times new roman',15,'bold'))
color.grid(row=8,column=4,padx=20,pady=0)

cv = StringVar()
colorEntry = ttk.Combobox(cumputer_lable,textvariable=cv,font=('arial',15,),background="Antique White2")
colorEntry.grid(row=8,column=6,padx=10)
colorEntry.insert('0',"Select")
colorEntry.config(state='disable')

seperator = ttk.Separator(cumputer_lable,orient='horizontal')
seperator.grid(row=16,columnspan=12,sticky='ew',pady=20)

asso = Label(cumputer_lable,text="Assoceries",bg="Antique White2",font=('times new roman',15,'bold'))
asso.grid(row=20,column=0,padx=20,pady=20)

ass = StringVar()
assoEntry = ttk.Combobox(cumputer_lable,textvariable=ass,font=('arial',15,),background="Antique White2")
assoEntry.grid(row=20,column=1,padx=10)
assoEntry.insert('0',"Select")
assoEntry.config(state='disable')


service = Label(cumputer_lable,text="Services",bg="Antique White2",font=('times new roman',15,'bold'))
service.grid(row=20,column=4,padx=20,pady=20)

sv = StringVar()
serviceEntry = ttk.Combobox(cumputer_lable,textvariable=sv,font=('arial',15),background="Antique White2")
serviceEntry.grid(row=20,column=6,padx=10)
serviceEntry.config(values=["Select"],state='disable')
serviceEntry.current('0')

# adding Billing Interface

bill_frame = Frame(i_lable,bd=8,bg="Antique White2",relief='groove')
bill_frame.grid(row=0,column=3,padx=(0,20))

bill_area = Label(bill_frame,text="Bill Area",bd=4,relief='groove',font=('times new roman',15,'bold'))
bill_area.pack(fill='x')

scroll = Scrollbar(bill_frame,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textarea = Text(bill_frame,height=15,width=38,relief='groove',yscrollcommand=scroll.set)
textarea.pack()
scroll.config(command=textarea.yview)


#bill menu frame
bill_menu_frame = LabelFrame(root,text="Bill Menu",bd=8,bg="Antique White2",relief='groove',font=('times new roman',15,'bold'))
bill_menu_frame.pack(fill=X)

system_bill = Label(bill_menu_frame,text="System Bill",font=('arial',15),background="Antique White2")
system_bill.grid(row=0,column=0,padx=20,sticky='w')

system_bill_entry = Entry(bill_menu_frame,font=('arial',15),bd=8,relief='groove')
system_bill_entry.grid(row=0,column=1,sticky='w',pady=10)

assoseries_bill = Label(bill_menu_frame,text="Assoceries Bill",font=('arial',15),background="Antique White2")
assoseries_bill.grid(row=0,column=4,padx=20,sticky='w')

assoseries_bill_entry = Entry(bill_menu_frame,font=('arial',15),bd=8,relief='groove')
assoseries_bill_entry.grid(row=0,column=6,sticky='w',pady=10)

service = Label(bill_menu_frame,text="Service Charges",font=('arial',15),background="Antique White2")
service.grid(row=1,column=0,padx=20,sticky='w')

service_entry = Entry(bill_menu_frame,font=('arial',15),bd=8,relief='groove')
service_entry.grid(row=1,column=1,sticky='w',pady=10)

GST = Label(bill_menu_frame,text="GST %",font=('arial',15),background="Antique White2",width=12)
GST.grid(row=1,column=4,padx=20,sticky='w')

gst_entry = Entry(bill_menu_frame,font=('arial',15),bd=8,relief='groove')
gst_entry.grid(row=1,column=6,pady=10,sticky='w')



#adding buttons
button_frame = Frame(bill_menu_frame,bg="Antique White2")
button_frame.grid(row=0,column=18,rowspan=2)

total = Button(button_frame,text="Total",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=total_bill)
total.grid(row=0,column=0,padx=30,sticky='n')

bill = Button(button_frame,text="Bill",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=bill_area1)
bill.grid(row=0,column=2,padx=20,sticky='n')

send = Button(button_frame,text="Send",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=send_email)
send.grid(row=0,column=4,padx=20,sticky='n')

clear = Button(button_frame,text="Clear",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=clear1)
clear.grid(row=1,column=0,padx=20,sticky='s',pady=10)

print_bill = Button(button_frame,text="Print",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=print_bill1)
print_bill.grid(row=1,column=2,padx=20,pady=10,sticky='s')

quit = Button(button_frame,text="Quit",font=('arial',16,'bold'),bg="Antique White2",bd=8,relief='groove',pady=10,width=5,height=-10,command=quit_window)
quit.grid(row=1,column=4,padx=20,pady=10,sticky='s')

root.mainloop()
