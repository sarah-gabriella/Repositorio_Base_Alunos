import requests

print("voce pediu pastel de frango,caldo de cana,na mesa 6 esta certo?")
resposta=input()

if resposta=="sim":
    pedido={
     "prato":"pastel de frango",
       "bebida":"caldo de cana",
       "mesa":"6"

    }
else:
    print("ok irei anotar as suas mudanças de pedido")
    prato=input("digite seu prato")
    bebida=input("digite sua bebida")
    mesa=input("digite sua mesa")
    pedido={
        "prato":prato,
        "bebida":bebida,
        "mesa":mesa,
    }

r =requests.put("https://68ca9f59430c4476c34a3bb8.mockapi.io/restaurante/7",pedido)


print(r.json())


