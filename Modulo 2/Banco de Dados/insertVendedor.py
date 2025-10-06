from coneccao import Session

from bd import Vendedor

with Session() as session:
    # Criar um novo vendedor
    novos_vendedores = Vendedor(nome='vendedores 2',loja_id=2 )
    
    # Adicionar o vendedores  à sessão
    session.add(novos_vendedores)
    
    # Commit para salvar no banco de dados
    session.commit() 

    print(f"vendedores '{novos_vendedores.nome}' criada com sucesso!")



