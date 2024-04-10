''' 

Arquivos temporarios seguros de deletar no Linux OS (Ubuntu):

`/tmp`;

`/var/tmp`;

`~/.cache`; # user-specific

`var/cache`;

`var/cache/apt/archives`; # debian/ubuntu only

`~/.config`; # browsers?

`/var/log`;

'''

import os
import shutil

temp_dirs = [
    "/tmp",
    "/var/tmp",
    os.path.expanduser("~/.cache"),
    "/var/cache",
    "/var/cache/apt/archives",
    os.path.expanduser("~/.config"),
    "/var/log"
]

def limpar_diretorio(diretorio):
    arquivos_deletados = []

    for arquivo in os.listdir(diretorio):
        full_path = os.path.join(diretorio, arquivo)
        try:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
            arquivos_deletados.append(full_path)
        except FileNotFoundError:
            pass
        except PermissionError:
            print(f"Erro ao excluir {full_path}: PERMISSAO NEGADA")

    return arquivos_deletados

def limpar_temp():
    arquivos_deletados = []
    for diretorio in temp_dirs:
        arquivos_deletados.extend(limpar_diretorio(diretorio))

    return arquivos_deletados

arquivos_deletados = limpar_temp()

if not arquivos_deletados:
    print("\nNenhum arquivo foi deletado.")
else:
    print("\nArquivos deletados:")
    for arquivo in arquivos_deletados:
        print(arquivo)

input("\nPressione Enter para sair...")

