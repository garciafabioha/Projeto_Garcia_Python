from conexao import conectar

def cadastrar_servico(codigo_cliente, data_inicial,
                      data_final, desc_rat, desc_serv, sit_serv):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO servicos (codigo_cliente, data_inicial,
                              data_final, desc_rat, desc_serv, sit_serv)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (codigo_cliente, data_inicial,
          data_final, desc_rat, desc_serv, sit_serv))

    conn.commit()
    cursor.close()
    conn.close()