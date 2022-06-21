
from Controller import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
app = QApplication()
# window = QMainWindow()


        
layout = QGridLayout()
window = mainwindow()
window.setWindowTitle("Shop")
window.setCentralWidget(QWidget())
window.centralWidget().setLayout(layout)



allow_alter = False
debug = QSpinBox()


#add widgets
catergories = QComboBox()
ComboBox = QComboBox()
item_name = QLabel()
# item_days_avaliable = QLabel()
item_price = QLabel()
item_vegan = QLabel()
item_vege = QLabel()
item_sugar = QLabel()
add_order = QPushButton("Add")
orders = QListWidget()
total = QLabel()
submit_order = QPushButton("Submit")



layout.addWidget(catergories)
layout.addWidget(ComboBox)
layout.addWidget(item_name)
# layout.addWidget(item_days_avaliable)
layout.addWidget(item_price)
layout.addWidget(item_vegan)
layout.addWidget(item_vege)
layout.addWidget(item_sugar)
layout.addWidget(add_order)
layout.addWidget(orders)
layout.addWidget(total)
layout.addWidget(submit_order)


vc = controller(layout,allow_alter,debug,catergories,ComboBox,item_name,item_price,item_vegan,item_vege,item_sugar,add_order,orders,total,submit_order)
vc.view_load()

window.show()


app.exec()