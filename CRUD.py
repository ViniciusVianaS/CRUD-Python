import mysql.connector

conexao = mysql.connector.connect(
    host='Localhost',
    user='root',
    password='',
    database='formulario'
)
cursor = conexao.cursor()

print("MENU CRUD")
print("Digite [1] para Create")
print("Digite [2] para Read")
print("Digite [3] para Update")
print("Digite [4] para Delete")
opcao = int(input("digite qual você quer: "))

if opcao == 1:
    print("CREATE")
    nome = input("Digite o nome: ") 
    sexo = input("Digite o sexo: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    comando = f'INSERT INTO usuario (nome, sexo, email, telefone) VALUES ("{nome}", "{sexo}", "{email}", "{telefone}")'
    cursor.execute(comando)
    conexao.commit()

elif opcao == 2:
    print("READ")
    comando = 'SELECT * FROM usuario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

elif opcao == 3:
    print("UPDATE")
    idUser = input("Digite o id de quem você quer editar: ")
    nome = input("Digite o novo nome: ") 
    comando = f'UPDATE usuario SET nome = "{nome}" WHERE idUser = "{idUser}"'
    cursor.execute(comando)
    conexao.commit()

elif opcao == 4:
    print("DELETE")
    idUser = input("Digite o id de quem você quer deletar: ")
    comando = f'DELETE FROM usuario WHERE idUser = "{idUser}"'
    cursor.execute(comando)
    conexao.commit()


cursor.close()
conexao.close()