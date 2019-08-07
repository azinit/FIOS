import time
import urllib.request
from fios.io import console
from typing import cast

from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor, QImage, QPixmap
from PySide2.QtWidgets import QFileDialog, QLineEdit, QApplication


# TODO: Rewrite!
class VFX(object):
    def __init__(self, widget):
        self.widget = widget

    # @property
    # def widget(self):
    #     return self.app.widget

    """
    ..............................................................................................................
    ................................................ APPLICATION .................................................
    ..............................................................................................................
    """
    # def set_ui(self, ui_file):
    #     self.widget._init_ui(ui_file)
    #     self.widget.show()
    #     self.redraw()

    def setWidget(self, **kwargs):
        Widget  = kwargs.get("widget",  None)
        show    = kwargs.get("show",    True)

        self.widget.activeWidget = Widget(self.widget)
        self.widget.setCentralWidget(self.widget.activeWidget)
        if show: self.widget.show()
    # def set_step(self, step_name):
    #     self.widget.lbl_step.setText(step_name)
    #
    # def reset_step(self):
    #     self.set_step("Настройка скачивания")
    #
    # def set_style(self, component, style_file):
    #     import fios.io.reader as reader
    #    # init style
    #     style = reader.read(style_file)
    #    # set style
    #     component.setStyleSheet(style)
    #
    def setImage(self, component, image_url, sizes=None, **kwargs):
        """ Set image for component """
        unavailable = kwargs.get("unavailable", "https://pp.userapi.com/c853428/v853428383/aed5e/VSbzlzc886U.jpg")
        image_url   = image_url if image_url else unavailable
        try:
            # init component sizes
            if sizes is None:
                sizes = {"w": component.width(), "h": component.height()}
            # init img data
            img = QImage()
            data = urllib.request.urlopen(image_url).read()
            img.loadFromData(data)
            # img img_view
            imgmap = QPixmap(img).scaled(sizes["w"], sizes["h"], Qt.KeepAspectRatio)
            component.setPixmap(imgmap)
        except:
            try:
                self.setImage(component, unavailable, sizes)
            except:
                reserve_image = "https://i2.wp.com/www.refreshmarketing.co.uk/wp-content/uploads/2014/10/linked-in-profile-anonymous.jpg"
                self.setImage(component, reserve_image, sizes)

    def redraw(self):
        """ Redraw GUI of application """
        QtCore.QCoreApplication.processEvents()

    def notify(self, message, thread=""):
        """ Notify user about status of last operation """
        self.widget.statusBar().showMessage(message)
        if thread:  console.log(message, thread=thread)
        self.redraw()

    """
    ...................................................
    .................... CURSORS  .....................
    ...................................................
    """

    def set_wait_cursor(self):
        """ Set wait cursor in App """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

    def reset_cursor(self):
        """ Reset cursor in App """
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))

    """
    ...................................................
    .................... PROCESSES  ...................
    ...................................................
    """

    def run_wait_process(self, process):
        """ Run process that will require waiting """
        # TODO: Reset cursor for buttons?
        # Set cursor.wait
        self.set_wait_cursor()
        self.redraw()
        # Invoke some_process
        result = process()
        # Reset cursor
        self.reset_cursor()
        return result

    """
    ..............................................................................................................
    ................................................ EFFECTS .....................................................
    ..............................................................................................................
    """

    # TODO: animate effects
    # TODO: loading
    #  effects

    # TODO: rewrite
    # # pl=QUEUE.get_cur_playlist(as_playlist=True)
    # def playlist_focus(pl):
    #     """ Set style for playlist:focus """
    #     LW = main_widget.listWidget
    #     LW.setCurrentItem(pl.item)
    #     highlight_style = "QListWidget::item:selected{background-color: rgb(173, 0, 0); color: #fff;}"
    #     LW.setStyleSheet(highlight_style)
    #
    #
    # def playlist_pressed(pl):
    #     """ Set style for playlist:pressed """
    #     LW = main_widget.listWidget
    #     LW.setCurrentItem(pl.item)
    #     highlight_style = "QListWidget::item:selected{background-color: rgb(173, 0, 0); color: #fff;}"
    #     LW.setStyleSheet(highlight_style)
    #
    #
    # def reset_playlist(pl):
    #     """ Reset playlist style """
    #     LW = main_widget.listWidget
    #     LW.setStyleSheet("")

    """
    ..............................................................................................................
    ................................................ DIALOG WINDOWS ..............................................
    ..............................................................................................................
    """

    # TODO: rewrite
    # Dialog Window Explorer
    def dialog_folder(self, **kwargs):
        """ Open dialog window for select folder """
        # from lib.settings import Settings
        parent          = kwargs.get("parent",          self.widget)
        caption         = kwargs.get("caption",         "Open folder")
        # directory       = kwargs.get("directory",       Settings.__app_dir__)
        directory       = kwargs.get("directory",       None)
        lineEdit        = kwargs.get("lineEdit",        "")

        el              = self.__dialog("folder", parent, caption, directory, "", lineEdit)
        return el

    def dialog_file(self, **kwargs):
        """ Open dialog window for select file """

        parent          = kwargs.get("parent",          self.widget)
        caption         = kwargs.get("caption",         "Select file")
        item            = kwargs.get("item",            "file")
        # directory       = kwargs.get("directory",       Settings.__app_dir__)
        directory       = kwargs.get("directory",       None)
        lineEdit        = kwargs.get("lineEdit",        "")
        filter_         = kwargs.get("filter_",         "All Files (*.*)")

        el              = self.__dialog(item, parent, caption, directory, filter_, lineEdit)
        return el

    def __dialog(self, item, parent, caption, directory, filter_, lineEdit):
        """ Open dialog window for select * """

        fileDialog = QFileDialog()
        # fileDialog.setOption(QFileDialog.DontUseNativeDialog, True)
        # from fios.graphics.core.CustomFileDialog import CustomFileDialog
        # fileDialog = CustomFileDialog()
        # el = fileDialog.getOpenFileNames(parent, caption, directory)
        # el = fileDialog.getExistingDirectory(parent, caption, directory)
        # print("!!!", el, "!!!")
        if   item == "folder":    el = fileDialog.getExistingDirectory(parent, caption, directory)
        elif item == "files" :    el = fileDialog.getOpenFileNames(parent,     caption, directory, filter_)[0]
        elif item == "file"  :    el = fileDialog.getOpenFileName(parent,      caption, directory, filter_)[0]

        count = str(el).count("/")

        # if count > 2:   el = str(el).replace("/", "\\", count)    # TODO: ?
        # if lineEdit:    cast(QLineEdit, lineEdit).setText(el)
        return el

    """
    ..............................................................................................................
    ................................................ PROGRESS BAR ................................................
    ..............................................................................................................
    """

    def update_progress(self, current, limit, process_symbol):
        # update Status
        # TODO: limit progress count?
        self.notify("{process_symbol} {i}/{limit} {progress}".format(
            process_symbol=process_symbol,
            i=current,
            limit=limit,
            progress=" ⬤ " * current + " ◯" * (limit - current),
        ))

    def progress(self, current, limit):
        char = '⟲' if current != limit else '✓'
        message = '\r%s %02d%%' % (char, current * 100 / limit)
        self.notify(message)

    def download_progress(self, percent):
        self.__update_pb(percent, download=True)

    def remove_progress(self, done, total):
        percent_int = int(float(done) / total * 100)
        self.__update_pb(percent_int, reverse=True)

    def backup_progress(self, done, total):
        percent_int = int(float(done) / total * 100)
        self.__update_pb(percent_int, backup=True)

    def reset_progress(self, reverse=False):
        value = 100 if reverse else 0
        self.__update_pb(value, download=True)
        self.redraw()

    def __update_pb(self, value, **kwargs):
        progress_bar = self.widget.progressBar
        if kwargs.get("reverse"):
            value = 100 - value
            color = "rgb(90, 90, 90)"
        elif kwargs.get("backup"):
            color = "rgb(74, 179, 167)"
        else:
            color = "rgb(173, 0, 0)"

        style = "::chunk {background-color: %s;}" % color
        progress_bar.setStyleSheet(style)
        progress_bar.setValue(value)
        self.redraw()

    # """
    # ..............................................................................................................
    # ................................................ VIDEO VIEW ..................................................
    # ..............................................................................................................
    # """
    #
    # def display_video(self, video):
    #     """ Display video in VideoView """
    #     # init components
    #     view_group = main_widget.video_view_group
    #     view_title = main_widget.video_view_title
    #     view_time = main_widget.video_view_time
    #     view_img = main_widget.video_view_img
    #     # :set_group
    #     view_group.setText(video.group_label)
    #     # :set_title
    #     view_title.setText(video.title)
    #     # :set_time
    #     view_time.setText(video.duration)
    #     # :set_image
    #     setImage(view_img, video.pic)
    #     # :redraw
    #     redraw()

    """
    ..............................................................................................................
    ................................................ LAYOUT MANAGE ...............................................
    ..............................................................................................................
    """

    def __each_component(self, layout: list, action):
        """ Action with every component of layout """
        for component in layout:
            if isinstance(component, str):
                element = getattr(self.widget, component)
            else:
                element = component

            action(element)

    def show_layout(self, layout: list):
        """ Show layout """
        self.__each_component(layout, action=lambda x: x.show())

    def hide_layout(self, layout: list):
        """ Hide layout """
        self.__each_component(layout, action=lambda x: x.hide())

    # """
    # ..............................................................................................................
    # ................................................ RESULTS VIEW ................................................
    # ..............................................................................................................
    # """
    #
    # def display_results(self, playlist, results):
    #     from lib.widgets import components
    #     added       = "Добавлено: {}/{}".format(results["added"][0], results["added"][1])
    #     removed     = "Удалено: {}/{}".format(results["removed"][0], results["removed"][1])
    #     text        = "[{title}]\n\n[{added}\n{removed}]".format(title=playlist.title, added=added, removed=removed)
    #     # # show layout
    #     # show_layout(layout)
    #     from PySide2.QtWidgets import QMessageBox
    #     # redraw()
    #     QMessageBox().information(main_widget, "Результаты проверки", text, QMessageBox.Ok)
    #     # view_btn.clicked.connect(handler_next)
    #
    # #
    # # def handler_next():
    # #     main_widget.is_downloading = True
    # #     print("NEXT!")
