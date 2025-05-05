def reverse_readline(file_name, buffer_size=4096):
    """
    Lê um arquivo de forma reversa, gerando suas linhas de baixo para cima.
    O arquivo é lido em blocos (chunks) para usar uma quantidade constante de memória.
    """
    with open(file_name, 'rb') as f:
        # Vai para o final do arquivo
        f.seek(0, 2)
        position = f.tell()
        leftover = b""
        
        # Enquanto não atingirmos o início do arquivo...
        while position > 0:
            # Define o início do bloco (não ultrapassando o começo do arquivo)
            start = max(0, position - buffer_size)
            f.seek(start)
            block = f.read(position - start)
            # Junta com o que sobrou do bloco anterior
            block += leftover
            # Separa pelas quebras de linha
            lines = block.split(b'\n')
            # A primeira parte pode ser uma linha incompleta, que será completada no próximo bloco.
            leftover = lines[0]
            complete_lines = lines[1:]
            
            # Produz as linhas completas em ordem reversa
            for line in reversed(complete_lines):
                yield line.decode('utf-8')
            
            position = start
        
        # Se houver alguma parte remanescente, é a primeira linha do arquivo.
        if leftover:
            yield leftover.decode('utf-8')


def invert_file(input_file, output_file):
    """
    Cria um novo arquivo com as linhas do arquivo de entrada na ordem inversa.
    """
    with open(output_file, 'w', encoding='utf-8') as out:
        for line in reverse_readline(input_file):
            out.write(line + "\n")


def main():
    """
    Função principal que solicita os nomes dos arquivos e gera o arquivo invertido.
    """
    input_file = input("Digite o nome do arquivo de entrada (ex.: entrada.txt): ")
    output_file = input("Digite o nome do arquivo de saída (ex.: saida.txt): ")
    
    invert_file(input_file, output_file)
    print("Arquivo invertido criado com sucesso!")


if __name__ == "__main__":
    main()
