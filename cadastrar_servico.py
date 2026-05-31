from conexao import conectar

def cadastrar_servico(codigo_cliente, data_inicial,
                      data_final, desc_rat, desc_serv, sit_serv, minutos_serv):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO servicos (codigo_cliente, data_inicial,
                              data_final, desc_rat, desc_serv, sit_serv, minutos_serv)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (int(codigo_cliente), data_inicial,
          data_final, desc_rat, desc_serv, sit_serv, int(minutos_serv)))

    conn.commit()
    cursor.close()
    conn.close()