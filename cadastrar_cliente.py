from conexao import conectar

def cadastrar_cliente(nome, endereco, codigo_cliente, cnpj,
                      cidade, estado, email, telefone,
                      data_cadastro):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes (nome, endereco, codigo_cliente, cnpj,
                              cidade, estado, email, telefone,
                              data_cadastro)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (nome, endereco, codigo_cliente, cnpj,
          cidade, estado, email, telefone,
          data_cadastro))

    conn.commit()
    cursor.close()
    conn.close()