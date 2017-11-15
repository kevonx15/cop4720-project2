import os
import csv
import random
import string

vin_template = "{}{}{}{}{}{}"
#               1 2 4 1 3 6
# 1     - where the vehicle was built
# 2-3   - the manufacturer
# 4-8   - portrait of vehicle brand, engine size and type
# 9     - security code - authorized by the manufacturer
# 10    - model year of card
# 11    - which plant
# 12-17 - serial number

alpha_num_options = string.ascii_uppercase + string.digits

first_name_options = []
last_name_options = []

hour_options = [1,1.5,2,2.5]

data_root = '.'

with open(os.path.join(data_root, 'firsts.csv')) as f:
    reader = csv.reader(f)
    first_name_options = list(reader)

with open(os.path.join(data_root, 'lasts.csv')) as f:
    reader = csv.reader(f)
    last_name_options = list(reader)

def generate_uuid():
    return ''

def generate_vin():
    p1 = random_alphanum(1)
    p2 = random_alphanum(2)
    p3 = random_alphanum(5)
    p4 = random_alphanum(1)
    p5 = random_alphanum(1)
    p6 = random_alphanum(1)
    p7 = random_alphanum(6)
    return vin_template.format(p1,p2,p3,p4,p5,p6,p7)

def pick_vtype():
    return ''

def random_alphanum(size):
    return ''.join(random.choice(alpha_num_options) for _ in range(size))

def generate_name():
    return random.choice(first_name_options), random.choice(last_name_options)

def generate_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))

def generate_hours():
    return random.choice(hour_options)

def generate_mechanic():
    fn, ln = generate_name()
    return {
        'MECH_ID': generate_uuid(),
        'MECH_FNAME': fn,
        'MECH_LNAME': ln
    }

def generate_customer():
    fn, ln = generate_name()
    ph = generate_phone()
    return {
        'CUST_ID': generate_uuid(),
        'CUST_FNAME': fn,
        'CUST_LNAME': ln,
        'CUST_PHONE': ph
    }

def generate_vehicle():
    vin = generate_vin()
    make = pick_vtype()

for i in range(0, 5):
    m = generate_mechanic()

for i in range(0, 10):
    c = generate_customer()
    for j in range(0, 1):
        v = generate_vehicle()
