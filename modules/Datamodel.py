from typing import Union
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QPersistentModelIndex


class PandasModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()):
        # No PyQt6, o argumento 'parent' deve ter um valor padrão
        return self._data.shape[0]

    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()):
        return self._data.shape[1]

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
            
        if role == Qt.ItemDataRole.DisplayRole:
            # Acessa os dados do DataFrame usando iloc
            return str(self._data.iloc[index.row(), index.column()])
            
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
        return None
