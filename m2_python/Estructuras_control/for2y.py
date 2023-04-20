
lechuga = [3.99, 'verduras']
tomate = [4.99, 'verduras']
papa = [2.55, 'verduras']
zanahoria = [1.55, 'verduras']
queso = [14.55, 'lacteos']
mantequilla = [4.55, 'lacteos']
leche = [2.55, 'lacteos']
SantaTeresa = [16.60, 'espirituoso']
Barcelo = [15.50, 'espirituoso']
DonJulio = [18.00, 'espirituoso']

productos = [lechuga, tomate, papa, zanahoria, queso, mantequilla, leche, SantaTeresa, Barcelo, DonJulio]

for producto in productos:
    if producto[1] == 'espirituoso':
        continue
    producto[0] *= 0.90
   
for producto in productos:
    print(producto)
    
   
   
 
 
