import os
import csv
import random
import string
import uuid

dir_path = os.path.dirname(os.path.realpath(__file__))
data_root = os.path.join(dir_path, '..', 'Data')

# first name options - for creating mechanics and customers
first_name_options = []

with open(os.path.join(dir_path, 'firsts.csv')) as f:
    reader = csv.reader(f)
    first_name_options = list([r[0] for r in reader])

# last name options - for creating mechanics and customers
last_name_options = []

with open(os.path.join(dir_path, 'lasts.csv')) as f:
    reader = csv.reader(f)
    last_name_options = list([r[0] for r in reader])

def generate_name():
    return random.choice(first_name_options), random.choice(last_name_options)

# vtype options - for creating customer vehicles
vtype_id_options = []

with open(os.path.join(data_root, 'fcl.vehicle_types.csv')) as f:
    reader = csv.DictReader(f)
    vtype_id_options = list([vtype['VTYPE_ID'] for vtype in reader])

def pick_vtype_id():
    return random.choice(vtype_id_options)

# for generating vins
vin_template = "{}{}{}{}{}{}{}"
#               1 2 5 1 1 1 6
# 1     - where the vehicle was built
# 2-3   - the manufacturer
# 4-8   - portrait of vehicle brand, engine size and type
# 9     - security code - authorized by the manufacturer
# 10    - model year of card
# 11    - which plant
# 12-17 - serial number

alpha_num_options = string.ascii_uppercase + string.digits

def random_alphanum(size):
    return ''.join(random.choice(alpha_num_options) for _ in range(size))

def generate_vin():
    p1 = random_alphanum(1)
    p2 = random_alphanum(2)
    p3 = random_alphanum(5)
    p4 = random_alphanum(1)
    p5 = random_alphanum(1)
    p6 = random_alphanum(1)
    p7 = random_alphanum(6)
    return vin_template.format(p1,p2,p3,p4,p5,p6,p7)

##

def generate_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))

def generate_uuid():
    return str(uuid.uuid4())

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
    return {
        'V_VIN': generate_vin(),
        'VTYPE_ID': pick_vtype_id(),
    }

def create_mechanics():
    with open(os.path.join(data_root, 'fcl.mechanics.csv'), 'w') as mech_f:
        writer = csv.DictWriter(mech_f, fieldnames=['MECH_ID', 'MECH_FNAME', 'MECH_LNAME'])
        writer.writeheader()
        for i in range(0, 5):
            m = generate_mechanic()
            writer.writerow(m)

def create_customers():
    cust_fn = os.path.join(data_root, 'fcl.customers.csv')
    v_fn = os.path.join(data_root, 'fcl.vehicles.csv')

    with open(cust_fn, 'w') as cust_f, open(v_fn, 'w') as v_f:
        cust_writer = csv.DictWriter(cust_f, fieldnames=['CUST_ID', 'CUST_FNAME', 'CUST_LNAME', 'CUST_PHONE'])
        v_writer = csv.DictWriter(v_f, fieldnames=['V_VIN', 'VTYPE_ID', 'CUST_ID'])

        cust_writer.writeheader()
        v_writer.writeheader()

        for i in range(0, 10):
            c = generate_customer()
            cust_writer.writerow(c)
            for j in range(0, 1):
                v = generate_vehicle()
                v['CUST_ID'] = c['CUST_ID']
                v_writer.writerow(v)

def create_available_parts():
    vend_fn = os.path.join(data_root, 'fcl.vendors.csv')
    part_fn = os.path.join(data_root, 'fcl.parts.csv')
    avail_part_fn = os.path.join(data_root, 'fcl.available_parts.csv')

    with open(vend_fn) as vend_f, open(part_fn) as part_f, open(avail_part_fn, 'w') as avail_part_f:
        vend_reader = csv.DictReader(vend_f)
        part_reader = csv.DictReader(part_f)
        avail_part_writer = csv.DictWriter(avail_part_f, fieldnames=['VEND_ID', 'PART_CODE'])

        avail_part_writer.writeheader()

        part_list = list(part_reader)

        for vend in vend_reader:
            for part in part_list:
                r = {'PART_CODE': part['PART_CODE'], 'VEND_ID': vend['VEND_ID']}
                avail_part_writer.writerow(r)

def create_vehicle_type_services():
    vtype_fn = os.path.join(data_root, 'fcl.vehicle_types.csv')
    part_fn = os.path.join(data_root, 'fcl.parts.csv')
    svc_req_fn = os.path.join(dir_path, 'svc_req.csv')
    vtype_svc_fn = os.path.join(data_root, 'fcl.vehicle_type_services.csv')
    req_part_fn = os.path.join(data_root, 'fcl.required_parts.csv')

    with open(vtype_fn) as vtype_f, open(part_fn) as part_f, open(svc_req_fn) as svc_req_f, open(vtype_svc_fn, 'w') as vtype_svc_f, open(req_part_fn, 'w') as req_part_f:
        vtype_reader = csv.DictReader(vtype_f)
        part_reader = csv.DictReader(part_f)
        svc_req_reader = csv.DictReader(svc_req_f)
        vtype_svc_writer = csv.DictWriter(vtype_svc_f, fieldnames=['SVC_ID', 'VTYPE_ID'])
        req_part_writer = csv.DictWriter(req_part_f, fieldnames=['SVC_ID', 'VTYPE_ID', 'PART_CODE', 'REQ_QTY'])

        all_parts = list(part_reader)

        vtype_svc_writer.writeheader()
        req_part_writer.writeheader()

        svc_req_list = list(svc_req_reader)

        for vtype in vtype_reader:
            for svc_req in svc_req_list:
                vehicle_type_service = {
                    'VTYPE_ID': vtype['VTYPE_ID'],
                    'SVC_ID': svc_req['SVC_ID']
                }

                vtype_svc_writer.writerow(vehicle_type_service)

                if svc_req['REQ_PART_QTY']:
                    part_options = [p for p in all_parts if p['PART_CODE'].startswith(svc_req['REQ_PART_TYPE'])]
                    random_part = random.choice(part_options)
                    required_part = {
                        'VTYPE_ID': vtype['VTYPE_ID'],
                        'SVC_ID': svc_req['SVC_ID'],
                        'PART_CODE': random_part['PART_CODE'],
                        'REQ_QTY': svc_req['REQ_PART_QTY']
                    }

                    req_part_writer.writerow(required_part)

create_mechanics()
create_customers()
create_available_parts()
create_vehicle_type_services()

