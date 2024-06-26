# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys
from PyQt6.QtWidgets import QApplication
from bookwindow import BookWindow
import rc_books

if __name__ == "__main__":
    app = QApplication([])

    window = BookWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
