import sys
import os
import ctypes

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

from ui_layout import Ui_MainWindow

import pandas as pd

from modules.Datamodel import PandasModel
from modules.DuimpData import gerarRelatorio

myappid = 'gtf.Relatorio.Duimp.1' 
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)



class MainWindow(QMainWindow):
    pathList:list[str] = []
    dataframe = pd.DataFrame()
    
    def SaveButton_saveAsExcel(self):
        
        if self.dataframe.empty:
            QMessageBox.critical(self, "Erro...", "O relatório ainda não foi gerado.")
            
        else:
            path, filter = QFileDialog.getSaveFileName(self, "Escolha o lugar para salvar a planilha Excel (.xlsx)", filter="Planilha Excel (*.xlsx)")
            if path != "": 
                self.dataframe.to_excel(path)
                QMessageBox.information(self, "Sucesso!", f'Relatório salvo com sucesso em:\n   "{path}"')
    
    def GenerateButton_loadModel(self):
        if self.pathList != []:
            data = gerarRelatorio(self.pathList)
            self.dataframe = data
            self.ui.DataTable.setModel(PandasModel(data))
            
        else: 
            QMessageBox.critical(self, "Erro...", "Nenhuma DUIMP selecionada.")
        
    def FileButton_selectFiles(self):
        files, filters = QFileDialog.getOpenFileNames(self, 'Selecione as DUIMPs...', "", "Arquivos PDF (*.pdf)")
        
        if files == []:
            return

        if self.pathList != []:
            self.ui.FileList.clear()
            self.ui.DataTable.setModel(None)
        
        self.ui.FileList.addItems(files)
        self.pathList = files
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        # Configuração do layout:
        
        self.setMinimumSize(QSize(740, 450))  # cada linha na DataTable tem altura: deltaH = 40
        self.setWindowIcon(QIcon(resource_path('./icone.ico')))
        
        self.ui.GenerateButton.setMinimumSize(QSize(163, 31))
        self.ui.GenerateButton.setMaximumSize(QSize(163, 31))
        # self.ui.DataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        verticalLayout = self.ui.gridLayout_2.findChild(QVBoxLayout, 'verticalLayout')
        verticalLayout2 = self.ui.gridLayout_6.findChild(QVBoxLayout, 'verticalLayout_2')
        
        if verticalLayout != None:
            verticalLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
            verticalLayout.setContentsMargins(0, 20, 0, 0)
        
        if verticalLayout2 != None:
            verticalLayout2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        
        
        
        # Conecção das funcionalizades (Eventos)
        
        self.ui.FileButton.clicked.connect(self.FileButton_selectFiles)
        self.ui.GenerateButton.clicked.connect(self.GenerateButton_loadModel)
        self.ui.SaveButton.clicked.connect(self.SaveButton_saveAsExcel)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
