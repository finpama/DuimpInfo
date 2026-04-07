import pandas as pd
import pdfplumber
import re
import pyperclip


def gerarLinha(pdf_path:str):
    
    linha = {}
    
    patterns = {
        'Processo': r"REF\. CLIENTE[^\d]*? (.*\d[A-Z])", # Pattern caso tenha letra na referência
        'DI': r"DUIMP[^\d\n]*(.*?-\d)",
        
        'II': r"II:[^\d\n]*(.*,\d\d)",
        'IPI': r"Sem-IPI_ainda",                        # Atualizar padrão quando tivermos uma DUIMP com IPI
        'PIS': r"PIS/PASEP:[^\d\n]*(.*,\d\d)",
        'COFINS': r"COFINS:[^\d\n]*(.*,\d\d)",
        
        'VMLE': r"VMLE[^\d\n]*(\d.*?,\d\d) / (\d.*?,\d\d) / (\d.*\d)",
        'Frete': r"Frete[^\d\n]*(\d.*?,\d\d) / (\d.*?,\d\d) / (\d.*\d)",
        'Seguro': r"Seguro[^\d\n]*(\d.*?,\d\d) / (\d.*?,\d\d) / (\d.*\d)",
        'CIF': r"VMLE\+FRETE\+SEGURO[^\d\n]*(\d.*?,\d\d) / (\d.*?,\d\d) / (\d.*\d)",
        
        'Capatazia': r"Capatazia - [^\d\n]*(\d.*\d)",      # Atualizar padrão quando tivermos uma DUIMP com IPI
        'AFRMM': r"A\.F\.R\.M\.M\.:[^\d\n]*(.*,\d\d)",
        'Siscomex': r"SISCOMEX:[^\d\n]*(.*,\d\d)",
    }
    
    with pdfplumber.open(pdf_path) as di:
        
        for field, pattern in patterns.items():
            
            match field:
                case 'VMLE' | 'Frete' | 'Seguro' | 'CIF':
                    groupIndex = 2
                case _:
                    groupIndex = 1
            
            
            info = ''
            
            for page in di.pages:
                info += page.extract_text() + '\n\n\n\n'
            
            pyperclip.copy(info)
            match = re.search(pattern, info, re.IGNORECASE)
            
            if field == 'Processo' and match == None:
                match = re.search(r"REF\. CLIENTE[^\d]*? (.*\d)", info, re.IGNORECASE)  # Pattern caso NÃO tenha letra na referência
            
            if match != None:
                linha[field] = match.group(groupIndex)
            else:
                linha[field] = 'Não encontrado'
        
    return linha

def gerarRelatorio(pdf_paths:list[str]):
    data = [gerarLinha(pdf_path) for pdf_path in pdf_paths]
    df = pd.DataFrame(data)
    
    return df