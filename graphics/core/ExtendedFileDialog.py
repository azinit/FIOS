import os

from PySide2 import QtWidgets


class ExtendedFileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)
        btns = self.findChildren(QtWidgets.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.open)
        self.tree = self.findChild(QtWidgets.QTreeView)

    def open(self):
        print("open!!!")
        inds = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                directory   = str(self.directory().absolutePath())
                el          = str(i.data().toString())
                files.append(os.path.join(directory, el))

        self.selectedFiles = files
        self.hide()

    def filesSelected(self):
        return self.selectedFiles