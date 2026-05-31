from conexao import conectar

# Criar a tabela de Clientes
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            endereco VARCHAR(200)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela clientes criada com sucesso!")     

# Remover campos na tabela Clientes
def remover_colunas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE clientes
        DROP COLUMN IF EXISTS dt_nasc,
        DROP COLUMN IF EXISTS tp_cliente
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Campos removidos com sucesso!")   

# Alterar e criar campos na tabela Clientes
def alterar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE clientes
        ADD COLUMN IF NOT EXISTS codigo_cliente INTEGER,
        ADD COLUMN IF NOT EXISTS cnpj VARCHAR(18),
        ADD COLUMN IF NOT EXISTS cidade VARCHAR(100),
        ADD COLUMN IF NOT EXISTS estado VARCHAR(2),
        ADD COLUMN IF NOT EXISTS email VARCHAR(100),
        ADD COLUMN IF NOT EXISTS telefone VARCHAR(20),
        ADD COLUMN IF NOT EXISTS data_cadastro DATE
    """)

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_clientes_codigo_cliente
        ON clientes (codigo_cliente)
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela clientes alterada com sucesso!")

# Criar a tabela de Serviços
def criar_tabela_servicos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id SERIAL PRIMARY KEY,
            codigo_cliente INTEGER NOT NULL,
            data_inicial DATE,
            data_final DATE,
            desc_rat VARCHAR(100),
            desc_serv VARCHAR(999),
            sit_serv VARCHAR(30) DEFAULT 'Em Andamento',

            CONSTRAINT fk_servicos_clientes
                FOREIGN KEY (codigo_cliente)
                REFERENCES clientes(codigo_cliente),

            CONSTRAINT chk_servicos_sit_serv
                CHECK (sit_serv IN ('Em Andamento', 'Aguardando Aprovação', 'Aprovado'))
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela servicos criada com sucesso!")

# Alterar e criar campo quantidade de hora na tabela Servicos
def alterar_tabela_servicos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE servicos
        ADD COLUMN IF NOT EXISTS minutos_serv INTEGER DEFAULT 0
    """)

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_servicos_codigo_cliente
        ON servicos (codigo_cliente)
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela serviços alterada com sucesso!")    

criar_tabela()
remover_colunas()
alterar_tabela()
criar_tabela_servicos()
alterar_tabela_servicos()