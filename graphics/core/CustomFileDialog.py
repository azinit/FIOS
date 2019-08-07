"""
#include <QtGui>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QFileDialog w;
    w.setFileMode(QFileDialog::DirectoryOnly);
    w.setOption(QFileDialog::DontUseNativeDialog,true);
    QListView *l = w.findChild<QListView*>("listView");
    if (l) {
         l->setSelectionMode(QAbstractItemView::MultiSelection);
     }
    QTreeView *t = w.findChild<QTreeView*>();
     if (t) {
       t->setSelectionMode(QAbstractItemView::MultiSelection);
   }
   return w.exec();
}
"""

from PySide2 import QtWidgets


class CustomFileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setFileMode(self.DirectoryOnly)
        self.setOption(self.DontUseNativeDialog, True)

        l = self.findChild(QtWidgets.QListView, 'listView')
        from PySide2.QtWidgets import QAbstractItemView
        if l:   l.setSelectionMode(QAbstractItemView.MultiSelection)

        t = self.findChild(QtWidgets.QTreeView)
        if t: t.setSelectionMode(QAbstractItemView.MultiSelection)

        # btns = self.findChildren(QtWidgets.QPushButton)
        # self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        # self.openBtn.clicked.disconnect()
        # self.openBtn.clicked.connect(self.open)
        # self.tree = self.findChild(QtWidgets.QTreeView)
    #
    # def open(self):
    #     print("open!!!")
    #     inds = self.tree.selectionModel().selectedIndexes()
    #     files = []
    #     for i in inds:
    #         if i.column() == 0:
    #             directory   = str(self.directory().absolutePath())
    #             el          = str(i.data().toString())
    #             files.append(os.path.join(directory, el))
    #
    #     self.selectedFiles = files
    #     self.hide()
    #
    # def filesSelected(self):
    #     return self.selectedFiles