products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    np = []
    np.append(name)
    np.append(price)    
    products.append(np)

    # np = [name, price]
    # products.append(np)
    
    #products.append([name, price])
    
print(products)
