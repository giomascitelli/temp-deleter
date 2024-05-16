import os
import shutil
import tempfile
import winreg
import logging

# Get user profile directory
user_profile = os.getenv('USERPROFILE')

# Setting up logging configuration to write to a file and overwrite it every time the script runs
logging.basicConfig(filename='temp_deleter.log', filemode='w', level=logging.INFO)

# Windows temp directories
temp_dirs = [
    r"C:\Windows\Temp",
    os.path.join(user_profile, r"AppData\Local\Temp"),
    r"C:\Windows\Panther",
    r"C:\Windows\SoftwareDistribution\Download",
    os.path.join(user_profile, r"AppData\Local\Microsoft\Windows\Explorer")
]

# Get Windows temp directory from registry
def limpar_diretorio(diretorio):
    arquivos_deletados = []

    # Check if directory exists
    for arquivo in os.listdir(diretorio):
        full_path = os.path.join(diretorio, arquivo)
        try:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
            arquivos_deletados.append(full_path)
            logging.info(f"Arquivo deletado: {full_path}")
        except FileNotFoundError:
            pass
        except PermissionError:
            logging.warning(f"Erro ao excluir {full_path}: permissão negada")

    return arquivos_deletados

# Clear temp directories
def limpar_temp():
    arquivos_deletados = []
    for diretorio in temp_dirs:
        arquivos_deletados.extend(limpar_diretorio(diretorio))

    return arquivos_deletados

arquivos_deletados = limpar_temp()

# Print results
if not arquivos_deletados:
    print("\nNenhum arquivo foi deletado.")
else:
    print(f"\n{len(arquivos_deletados)} arquivos foram deletados. Verifique o log para mais informações.")

input("\nPressione Enter para sair...")

