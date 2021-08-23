import json 

json_file=open('../data.json')
data=json.load(json_file)
for bundle in data["Bundles"]:
    if "Product" in bundle.keys():
        print("in product\n\n")
        for product in bundle['Product']:
            if ('Name' in bundle['Product'] and 'Price' in bundle['Product']):
                print("Name and Price are in Product")
                print(f"product name is {product['Name']}")
                print(f"product price is {product['Price']}")
            elif "Products" in bundle.keys():
                for products in bundle.keys():
                    if ('Name' in bundle['Products'] and 'Price' in bundle['Products']):
                        print(f"in products the name is {product['Name']}")
                        print(f"in products the price is {product['Price']}")
                    elif 'Name' in bundle.keys():
                        print(bundle['Name'])
                    else:
                        print('no info')

