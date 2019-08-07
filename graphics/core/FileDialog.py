"""
https://www.qtcentre.org/threads/43841-QFileDialog-to-select-files-AND-folders

QFileDialog* _f_dlg = new QFileDialog(this);
  _f_dlg->setFileMode(QFileDialog::Directory);
  _f_dlg->setOption(QFileDialog::DontUseNativeDialog, true);

  // Try to select multiple files and directories at the same time in QFileDialog
  QListView *l = _f_dlg->findChild<QListView*>("listView");
  if (l) {
    l->setSelectionMode(QAbstractItemView::MultiSelection);
   }
  QTreeView *t = _f_dlg->findChild<QTreeView*>();
   if (t) {
     t->setSelectionMode(QAbstractItemView::MultiSelection);
    }

  int nMode = _f_dlg->exec();
  QStringList _fnames = _f_dlg->selectedFiles();
"""

from PySide2 import QtWidgets


class ExtendedFileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)
        btns = self.findChildren(QtWidgets.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QtWidgets.QTreeView)

    def open(self):
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
