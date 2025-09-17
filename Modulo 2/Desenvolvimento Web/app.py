import requests

prato=input ("qual prato vai ser ")
mesa=input("qual mesa vai ser ")
bebida=input("qual bebida vai ser ")

pedido={
    prato:prato,
    mesa:mesa,
    bebida:bebida,
}

r = requests.post("https://68ca9f59430c4476c34a3bb8.mockapi.io/restaurante",)

print(r.json())
