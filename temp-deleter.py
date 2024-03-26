import os
import shutil
import tempfile
import winreg

user_profile = os.getenv('USERPROFILE')

# Diretórios temporários do Windows
temp_dirs = [
    r"C:\Windows\Temp",
    os.path.join(user_profile, r"AppData\Local\Temp"),
    r"C:\Windows\Panther",
    r"C:\Windows\SoftwareDistribution\Download",
    os.path.join(user_profile, r"AppData\Local\Microsoft\Windows\Explorer")
]

# # Chaves de registro para arquivos temporários do Internet Explorer
# ie_temp_keys = [
#     r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\History\Current",
#     r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\History\Visited",
# ]

# # Chaves de registro para arquivos temporários do Windows Defender
# wd_temp_keys = [
#     r"HKLM\SOFTWARE\Microsoft\Windows Defender\Settings\IntelligentOfflineScan\History",
#     r"HKLM\SOFTWARE\Microsoft\Windows Defender\Settings\MpEngine\Signatures",
# ]

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
            print(f"Erro ao excluir {full_path}: permissão negada")

    return arquivos_deletados

# def limpar_registro(chave, valor):
#     try:
#         with winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave, 0, winreg.KEY_WRITE) as k:
#             winreg.DeleteValue(k, valor)
#     except PermissionError:
#         print(f"Erro ao excluir {valor} de {chave}: permissão negada")
#     except FileNotFoundError:
#         pass

def limpar_temp():
    arquivos_deletados = []
    for diretorio in temp_dirs:
        arquivos_deletados.extend(limpar_diretorio(diretorio))

    # for chave in ie_temp_keys:
    #     limpar_registro(chave, "Visited")

    # for chave in wd_temp_keys:
    #     limpar_registro(chave, "ScanHistory")

    return arquivos_deletados

arquivos_deletados = limpar_temp()


if not arquivos_deletados:
    print("\nNenhum arquivo foi deletado.")
else:
    print("\nArquivos deletados:")
    for arquivo in arquivos_deletados:
        print(arquivo)

input("\nPressione Enter para sair...")

