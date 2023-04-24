


def prices_iva(price):
    return price*1.21
prices = [10,20,30,40,50] 
results = list(map(prices_iva,prices))
print(results)


prices = [10,20,30,40,50] 
prices_iva = []
for price in prices:
    prices_iva.append(price * 1.21)
print(prices_iva)

def sumar_iva(price):
    return price * 1.21
sumarIVA1 
