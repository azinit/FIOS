"""
UIWidget - mixin for QtWidget
Needed for adding .ui loading functionality
"""


class UIWidget(object):
    def init_ui(self, ui_file):
        from fios.graphics.core.UiLoader import loadUi
        loadUi(ui_file, self)
