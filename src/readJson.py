import json 
import pandas as pd
json_file=open('../data.json')
data=json.load(json_file)
prod={'Name':list(),'Price':list()}
for bundle in data["Bundles"]:
    if "Product" in bundle.keys():
        print("in product\n\n")
        for product in bundle['Product']:
            if 'Name' in product.keys() and 'Price' in product.keys():
                print(f"you can buy {product['Name']} at our store at {product['Price']}\n\n")
                prod['Name'].append(product['Name'][:29])
                if product['Price'] is not None:
                    prod['Price'].append(round(product['Price'],1))
                else:prod['Price'].append(None)
            else:pass
    elif 'Products' in bundle.keys():
        for products in bundle['Products']:
            if 'Name' in products.keys() and 'Price' in products.keys():
                print(f"you can buy {products['Name']} at our store at {products['Price']}\n\n")
                prod['Name'].append(products['Name'][:29])
                if products['Price'] is not None:
                    prod['Price'].append(round(products['Price'],1))
                else:prod['Price'].append(None)
            else:pass
    elif 'Name' in bundle.keys():
        prod['Name'].append(bundle['Name'][:29])
        prod['Price'].append(None)
    else:pass

df=pd.DataFrame(prod)
df.to_csv('productData.csv',index=False)


