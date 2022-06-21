
from distutils.log import debug
from Data import *
from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from datetime import datetime

class mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        
#As optimized as bureaucracy 
@dataclass
class controller:
    layout: QGridLayout
    allow_alter: bool
    debug: QSpinBox
    catergories: QComboBox
    ComboBox: QComboBox
    item_name: QLabel
    item_price: QLabel
    item_vegan: QLabel
    item_vege: QLabel
    item_sugar: QLabel
    add_order: QPushButton
    orders: QListWidget
    total: QLineEdit
    submit_order: QPushButton
    
    def view_load(self):
        self.debug_mode()
        self.order = []
        self.price_total = 0
        self.set_catergories()
        self.set_combobox()
        self.add_order.clicked.connect(self.add_to_order)
        self.orders.itemDoubleClicked.connect(self.remove_item)
        self.catergories.currentIndexChanged.connect(self.set_combobox)
        self.ComboBox.currentIndexChanged.connect(self.set_layout_labels)
        self.set_layout_labels()
        self.submit_order.clicked.connect(QApplication.instance().quit)

    def debug_mode(self):
        if input("Debug mode Y/N").lower() == "y":
            self.allow_alter = True
            self.layout.addWidget(self.debug)
            self.set_debug()
            self.debug.setValue(1)
            self.debug.valueChanged.connect(self.debug_day_shift)
            self.day_shift = 0
        else:
            self.day_shift = datetime.today().weekday()



    def set_debug(self):
        self.debug.setMaximum(7)
        self.debug.setMinimum(1)

    def debug_day_shift(self):
        self.day_shift = self.debug.value()-1
        print(self.day_shift)
        self.ComboBox.clear()
        self.set_combobox()
        self.set_layout_labels()
        

    def remove_item(self,item):
        find_price = []
        for itm in range(self.orders.count()):
            find_price.append(self.orders.item(itm))
        self.orders.takeItem(find_price.index(item))
        self.order.pop(find_price.index(item))
        self.price_total -= float(item.text().split("$")[1])
        self.total_set()

    def add_to_order(self):
        self.order.append(self.ComboBox.currentText())
        if self.ComboBox.currentText() != "Nothing Avaliable Today":
            for found_class in all_class:
                if found_class._name == self.ComboBox.currentText():
                    break
            self.orders.insertItem(0,f"{self.ComboBox.currentText()}:  ${found_class._price}")
            self.price_total += found_class._price
            self.total_set()
        
    def total_set(self):
        self.total.setText(f"Total = ${self.price_total}")

    
    def set_catergories(self):
        self.catergories.clear()
        self.catergories.addItems(["Sandwiches","Sushi","Drinks","Specials"])
    
    def special_item_days(self,selected_catergory):
        for item in all_class:
            if selected_catergory in str(type(item)):
                if item._days_avaliable[0][0] == days_of_the_week(self.day_shift):
                    self.ComboBox.addItem(item._name)
    
    def norm_items_set(self,selected_catergory):
        for item in all_class:
            if selected_catergory in str(type(item)):
                self.ComboBox.addItem(item._name)

    def set_combobox(self):
        self.ComboBox.clear()
        selected_catergory = self.catergories.currentText()
        if selected_catergory != "Specials":
            self.norm_items_set(selected_catergory)
        else:
            self.special_item_days(selected_catergory)
        if self.ComboBox.currentText() == "":
                self.ComboBox.addItem("Nothing Avaliable Today")

    def set_all(self, current_class):
        print(current_class)
        self.item_name.setText(f"Name: {current_class._name}")
        is_veg = ["Yes" if current_class._is_vegan else "No"][0]
        self.item_vegan.setText(f"Vegan Friendly: {is_veg}")
        is_veg = ["Yes" if current_class._is_vegeterain else "No"][0]
        self.item_vege.setText(f"Vegeterian Friendly: {is_veg}")
        is_sug = ["Yes" if current_class._contains_sugar else "No"][0]
        self.item_sugar.setText(f"Contains Sugar: {is_sug}")
        self.item_price.setText(f"Price: ${current_class._price:.2f}")
        self.total_set()

    def clear_all(self):
        self.item_name.clear()
        self.item_price.clear()
        self.item_vegan.clear()
        self.item_vege.clear()
        self.item_sugar.clear()

    def set_layout_labels(self):
        index = self.ComboBox.currentText()
        catergory = self.catergories.currentText()
        for item in all_class:
            if catergory in str(item):
                if item._name == index:
                    current_class = item
                    break
        try:
            self.set_all(current_class)
        except UnboundLocalError:
            self.clear_all()
        