# !/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Any
from PySide6.QtWidgets import QListWidget
from PySide6.QtGui import QIcon, QDropEvent
from PySide6.QtGui import QDropEvent
from PySide6.QtCore import QUrl
import sys
import os
from pathlib import Path


def only_files(list: list[QUrl]) -> bool:
    return bool(list) and all(url.scheme() == "file" for url in list)


def get_filepaths(list: list[QUrl]) -> list[Path]:
    return [Path(url.path()) for url in list]


class FileEdit(QListWidget):
    filepaths: set[Path] = set()
    
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)
        self.setDragEnabled(True)

    def dragEnterEvent(self, event: QDropEvent):
        data = event.mimeData()
        urls = data.urls()
        if only_files(urls):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if only_files(urls):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if only_files(urls):
            self.filepaths.update(get_filepaths(urls))
            filenames = [file.name for file in self.filepaths]
            self.clear()
            self.addItems(filenames)
