import sqlite3

# variavel de conexao
try:
    banco = sqlite3.connect('banco_usuario.db')

        # atravez deste curso que iremos digitar dentro do banco de dados
    cursor = banco.cursor()

    # cursor.execute("INSERT INTO clientes VALUES('LUIZ SILVA','7','MARIAdOSaNJOS@15978')")
    # cursor.execute("INSERT INTO clientes VALUES('PEDRO SILVA','50','MARIAdOSaNJOS@15978')")
    # cursor.execute("INSERT INTO clientes VALUES('CARLO SILVA','10','MARIAdOSaNJOS@15978')")
    
    # # cursor.execute("SELECT * FROM clientes")
    # nome = "lucas dias"
    # idade = 23
    # email = "lulu@gakauj1255"                           # Conversao para String para exibir
    # cursor.execute("INSERT INTO clientes VALUES('"+nome+"','"+str(idade)+"','"+email+"')")

    # nome = "MATHEUS "
    # idade = 25
    # email = "lulu@gakauj1255"                           # Conversao para String para exibir
    # cursor.execute("INSERT INTO clientes VALUES('"+nome+"','"+str(idade)+"','"+email+"')")

    # nome = "DIANA"
    # idade = 255
    # email = "lulu@gakauj1255"                           # Conversao para String para exibir
    # cursor.execute("INSERT INTO clientes VALUES('"+nome+"','"+str(idade)+"','"+email+"')")

    # nome = "MARCIO"
    # idade = 23
    # email = "lulu@gakauj1255"                           # Conversao para String para exibir
    # cursor.execute("INSERT INTO clientes VALUES('"+nome+"','"+str(idade)+"','"+email+"')")
    
    # cursor.execute("DELETE from clientes WHERE idade <= 710")
    # print(cursor.fetchall())

    cursor.execute("UPDATE clientes SET nome = ' diogo' WHERE idade <30 ")
    banco.commit()
    print("Operação realizada COM SUCESSO! ")

except sqlite3.Error as erro:
    print("ERRO AO EXCLUIR DADOS ",erro)

