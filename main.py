import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 400)
        self.result = QPushButton('Рисовать', self)
        self.result.move(10, 200)
        self.result.resize(100, 100)
        self.result.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            self.do_paint = False
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        size = randrange(30, 200)
        qp.drawEllipse(200, 100, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())