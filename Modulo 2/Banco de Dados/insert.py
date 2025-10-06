from coneccao imfport Session

from bd import Loja

with Session() as session:
    # Criar uma nova loja
    nova_loja = Loja(nome='loja 3',endereco='rua matilda',gerente='gerente Paulo')
    
    # Adicionar a loja à sessão
    session.add(nova_loja)
    
    # Commit para salvar no banco de dados
    session.commit()
    
    print(f"Loja '{nova_loja.nome}' criada com sucesso!")

