"""
    Application About Dialog
"""
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
)

import app_info


class AboutDialog(QDialog):
    """
        AboutDialog
    """
    def __init__(self):
        super().__init__()

        q_btn = QDialogButtonBox.Ok  # No cancel
        self.button_box = QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)

        self.setWindowTitle('About')

        layout = QVBoxLayout()

        title = QLabel(app_info.TITLE)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join("icons", "vibrator-256.png")))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version: " + app_info.VERSION))
        layout.addWidget(QLabel(app_info.AUTHOR))
        layout.addWidget(QLabel(app_info.AUTHOR_EMAIL))
        link_label = QLabel('<a href="' + app_info.AUTHOR_WEB + '">' + app_info.AUTHOR_WEB + '</a>')
        link_label.setOpenExternalLinks(True)
        layout.addWidget(link_label)
        layout.addWidget(QLabel(app_info.APP_DATE))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.button_box)

        self.setLayout(layout)
