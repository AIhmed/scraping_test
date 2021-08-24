import json 
import pandas as pd
json_file=open('../data.json')
data=json.load(json_file)
prod={'Name':list(),'Price':list()}



for bundle in data["Bundles"]:
    if "Product" in bundle.keys():#check if there is a product to extract the Price and Name 
        print("in product\n\n")
        for product in bundle['Product']:#there can be a list of product 
            if 'Name' in product.keys() and 'Price' in product.keys():#check if there is a Name and Price 
                print(f"you can buy {product['Name']} at our store at {product['Price']}\n\n")
                prod['Name'].append(product['Name'][:29]) 
                if product['Price'] is not None:# the key price can exist but a null value 
                    prod['Price'].append(round(product['Price'],1))
                else:prod['Price'].append(None)
            else:pass
    elif 'Products' in bundle.keys():# when analysing the data i noticed there i are tow keys for product which led to adding this condiction if not 'Product' then 'Products' and the process is the same
        for products in bundle['Products']:
            if 'Name' in products.keys() and 'Price' in products.keys():
                print(f"you can buy {products['Name']} at our store at {products['Price']}\n\n")
                prod['Name'].append(products['Name'][:29])
                if products['Price'] is not None:
                    prod['Price'].append(round(products['Price'],1))
                else:prod['Price'].append(None)
            else:pass
    elif 'Name' in bundle.keys():# if the bundle contains only the Name property
        prod['Name'].append(bundle['Name'][:29])
        prod['Price'].append(None)
    else:pass

df=pd.DataFrame(prod)
df.to_csv('productData.csv',index=False)


