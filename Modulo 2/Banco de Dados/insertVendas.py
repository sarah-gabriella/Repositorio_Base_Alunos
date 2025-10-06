from coneccao import Session

from bd import Venda

with Session() as session:
    # Criar uma nova Venda
    nova_Venda = Venda(carro='bmw',valor=40.000,comissao=20.00,vendedor_id=1)
    
    # Adicionar a Venda à sessão
    session.add(nova_Venda)
    
    # Commit para salvar no banco de dados
    session.commit()
    
    print(f"Venda '{nova_Venda.nome}' criada com sucesso!")
