import os

def ler_nome_arquivo():
    return input("Digite o nome do arquivo de entrada: ")

def inverter_linhas_arquivo(nome_entrada, nome_saida):
    arquivos_temp = []
    with open(nome_entrada, 'r', encoding='utf-8') as entrada:
        for linha in entrada:
            # Cria um arquivo temporário para cada linha
            temp_name = f'temp_{len(arquivos_temp)}.txt'
            with open(temp_name, 'w', encoding='utf-8') as temp:
                temp.write(linha)
            arquivos_temp.append(temp_name)
    
    with open(nome_saida, 'w', encoding='utf-8') as saida:
        # Lê os arquivos temporários de trás pra frente e escreve no arquivo de saída
        for temp_name in reversed(arquivos_temp):
            with open(temp_name, 'r', encoding='utf-8') as temp:
                saida.write(temp.read())
            os.remove(temp_name)  # Remove o arquivo temporário

def main():
    nome_entrada = ler_nome_arquivo()
    nome_saida = "saida.txt"
    inverter_linhas_arquivo(nome_entrada, nome_saida)
    print(f"Arquivo invertido salvo como {nome_saida}")

if __name__ == "__main__":
    main()
