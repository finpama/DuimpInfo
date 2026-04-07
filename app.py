import pandas as pd
import os

from modules import *

dir_path = "leitor"

if not os.path.exists(dir_path):
    os.mkdir(dir_path)
else:

    files = os.listdir(dir_path)
    file_paths = [os.path.join(dir_path, file) for file in files if file.lower().endswith('.pdf')]

    df = gerarRelatorio(file_paths)
    print(df)

    # df.to_excel("Relatório.xlsx", index=False)