from PySide2.QtWidgets import QMainWindow, QApplication
from ui_boarding_pass import Ui_MainWindow

"""Classa która generuje karte pokładową za
pomoca plakietek wypełnionych tekstem"""


class BoardingPass(QMainWindow):
    def __init__(self, person, flight, parent=None):
        super().__init__(parent)
        self.person = person
        self.flight = flight
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.display_info()

    def display_info(self):
        id_name = f"Id: {self.person.id()}, Name: {self.person.name()}"
        self.ui.id_name.setText(id_name)
        flight_number = f"Flight number: {self.flight.number()}"
        self.ui.fligh_nr.setText(flight_number)
        seat_class = f"Seat class: {self.person.flight_class()}"
        self.ui.seat_class.setText(seat_class)
        seat_nr = (
            f"Seat number: {self.person.seat()[self.flight.plane()].number()}"
        )
        self.ui.seat_nr.setText(seat_nr)
        destination = f"Destination: {self.flight.destination()}"
        self.ui.flight_destination.setText(destination)
        gate = f"Gate number: {self.flight.gate()}"
        self.ui.gate.setText(gate)
        time = f"Departure time: {self.flight.time_of_departure()}"
        self.ui.time_of_departue.setText(time)


def guiMain(args, person, flight):
    app = QApplication(args)
    window = BoardingPass(person, flight)
    window.show()
    return app.exec_()
