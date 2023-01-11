from Project import (
    Person,
    PlaneType,
    Plane_Flight,
    Flight,
    AlreadyInThisClassErorr,
    YouAlreadyHaveTicket,
    ThisSeatIsOccupiedError,
    ThisClassSeatsAreFullError,
    PersonNotinFlighError,
    buy_ticet,
    change_class,
    change_seat,
    person_is,
)
from boarding_pass import guiMain
import sys


class IncorectOptionError(Exception):
    def __init__(self):
        super().__init__("You have chosen incorect option")


passengers1 = [
    Person(1, "Jacek", "eco"),
    Person(2, "Karolina", "eco"),
    Person(3, "Jórek", "premium"),
    Person(4, "Maciej", "eco"),
    Person(5, "wacek", "bisnes"),
]

passengers2 = [
    Person(6, "Zenek", "bisnes"),
    Person(7, "Błażej", "bisnes"),
    Person(8, "Tomasz", "bisnes"),
    Person(9, "Weronika", "premium"),
    Person(10, "Karol", "premium"),
]


planetypes = {
    "plane_type1": PlaneType("Fast", (4, 1), (6, 5), (2, 2)),
    "plane_type2": PlaneType("Not that Fast", (6, 5), (6, 5), (4, 2)),
    "plane_type3": PlaneType("Big", (6, 10), (6, 10), (6, 5)),
}
hangar = {
    "plane1": Plane_Flight(planetypes["plane_type1"], "flight997.json"),
    "plane2": Plane_Flight(planetypes["plane_type2"], "flight998.json"),
}

prices = {"eco": 100, "bisnes": 250, "premium": 500}

flights = {
    "Warsaw-Paris": Flight(997, hangar["plane1"], "Paris", 1, "17:15", prices),
    "Warsaw-Berlin": Flight(
        998, hangar["plane2"], "Berlin", 3, "23:15", prices
    ),
}


class StopException(Exception):
    def __init__(self):
        super().__init__("Halt")


"""Classa Interface pozwala na wykonywanie różnych akcji takich jak
kupowanie biletów, zmiana miejsc/klasy, generowanie karty pokładowej itp.
Aby z niej kożystać należy najpierw dodać osobę/ osoby
na których chcemy wykonywać dane akcje. Jeżeli chcemy kupić bilety dla
kilku grup osób po kolei to po zakupie biletów dla pierwszej grupy,
należy albo usunąć obecne osoby i dodać nowe jężeli chcemy kupować
bilety na ten sam lot albo włączyć i wyłączyć interfjes.
Zakładamy że jedna osoba nie może kupić więcej niż 1 miesjca
w danym locie, można zakupić bilet grupowy ale w tedy 1 miejsce jest
przypisane dla jednej osoby.
Aby edytować miejsce/klase osoby która już ma zakupiony bilet
posępujemy analogicznie dajemy tą osobę podające jej id i imie i w tedy
wykonujemy na niej akcjie zamiany miejsca/klasy generacji karty pokładowej"""


class Interface:
    def __init__(self):
        self.people = []

    def print_options(self):
        print(
            "\nSelect one of the following operations:\n"
            " 0) List people\n"
            " 1) Add a person\n"
            " 2) Remove person\n"
            " 3) Buy tickets\n"
            " 4) Change class\n"
            " 5) Change seat\n"
            " 6) Generate boarding pass\n"
            " 9) Exit"
        )

    def get_person_info(self):
        print("Specify id:")
        id = int(input())
        print("Specify name and surname:")
        name = str(input())
        return id, name

    def get_class_info(self):
        print(
            "Select seat class type:\n"
            " 0) eco\n"
            " 1) bisnes\n"
            " 2) premium\n"
        )

    def print_class_seats(self, plane, clasa):
        for row in plane.get_class(clasa):
            X = " ".join(str(obj) for obj in row)
            print(X)
        print("\n")

    def list_people(self):
        for index, person in enumerate(self.people):
            print(f" {index:>3}: {person}")

    def add_person(self):
        try:
            id, name = self.get_person_info()
            self.people.append(Person(id, name))
        except TypeError:
            print("Creation unsuccessful, aborting...")

    def remove_person(self):
        id, name = self.get_person_info()
        try:
            for person in self.people:
                if person.id() == id and person.name() == name:
                    self.people.remove(person)
        except TypeError:
            print("Removal unsuccessful, aborting...")

    def buy_tickets(self):
        print("Chose your flight:\n")
        for index, flight in enumerate(flights.keys()):
            print(f"{index}) {flight}\n")

        try:
            selection = int(input())
            if 0 > selection or (len(flights) - 1) < selection:
                raise ValueError
            lst = list(flights)
            chosen_flight = flights[lst[selection]]

        except IncorectOptionError:
            print("Uncorect flight, aborting...")
            self.tick()

        self.get_class_info()

        try:
            selection = int(input())
            if 0 > selection or 2 < selection:
                raise ValueError

            if selection == 0:
                flight_class = "eco"
            elif selection == 1:
                flight_class = "bisnes"
            elif selection == 2:
                flight_class = "premium"

        except IncorectOptionError:
            print("Uncorect class, aborting...")
            self.tick()

        print(
            "\nYou can choose your seats for a fee of PLN 50\n"
            "per seat. If you choose not to choose a seat,\n"
            "it will be allocated to you automatically\n"
            "without additional payment.\n"
        )

        self.print_class_seats(chosen_flight._plane, flight_class)

        dict_of_people = {}
        for person in self.people:
            print(f"Enter seat number for {person.name()}:")
            seat = str(input())
            dict_of_people[person] = seat
        try:
            a = buy_ticet(dict_of_people, chosen_flight, flight_class)
            print(f"\nTotal price to pay: {a}\n")

        except (
            ThisClassSeatsAreFullError,
            ThisSeatIsOccupiedError,
            YouAlreadyHaveTicket,
        ):
            print("Buying was unsuccesful.")

    def change_class(self):
        id, name = self.get_person_info()
        for person in self.people:
            if id == person.id() and name == person.name():
                you = person

        print("Chose your flight:\n")
        for index, flight in enumerate(flights.keys()):
            print(f"{index}) {flight}\n")

        try:
            selection = int(input())
            if 0 > selection and (len(flights) - 1) < selection:
                raise ValueError
            lst = list(flights)
            chosen_flight = flights[lst[selection]]

        except IncorectOptionError:
            print("Uncorect flight, aborting...")
            self.tick()

        self.get_class_info()

        try:
            selection = int(input())
            if 0 > selection and 2 < selection:
                raise ValueError

            if selection == 0:
                new_class = "eco"
            elif selection == 1:
                new_class = "bisnes"
            elif selection == 2:
                new_class = "premium"

        except IncorectOptionError:
            print("Uncorect class, aborting...")
            self.tick()

        self.print_class_seats(chosen_flight._plane, new_class)

        print(
            "\nYou can choose your new seat for a fee of PLN 50.\n"
            "If you choose not to choose a seat,\n"
            "it will be allocated to you automatically\n"
            "without additional payment."
        )
        new_seat = str(input())
        try:
            a = change_class(you, chosen_flight, new_class, new_seat)
            print(f"price to pay: {a}")
        except (
            ThisClassSeatsAreFullError,
            ThisSeatIsOccupiedError,
            AlreadyInThisClassErorr,
            PersonNotinFlighError,
        ):
            print("Changing class was unsuccessful\n")

    def change_seat(self):
        id, name = self.get_person_info()
        for person in self.people:
            if id == person.id() and name == person.name():
                you = person

        print("Chose your flight:\n")
        for index, flight in enumerate(flights.keys()):
            print(f"{index}) {flight}\n")

        try:
            selection = int(input())
            if 0 > selection and (len(flights) - 1) < selection:
                raise ValueError
            lst = list(flights)
            chosen_flight = flights[lst[selection]]
        except IncorectOptionError:
            print("Uncorect flight, aborting...")
            self.tick()
        try:

            you2 = person_is(you, chosen_flight)

            self.print_class_seats(
                chosen_flight._plane,
                you2._flight_class,
            )
        except PersonNotinFlighError:
            print("Person not in flight\n")
            self.tick()

        print(
            "\nYou can choose your new seat for a fee of PLN 50.\n"
            "If you choose not to choose a seat,\n"
            "it will be allocated to you automatically\n"
            "without additional payment."
        )
        new_seat = str(input())
        try:
            print(f"price to pay: {change_seat(you, chosen_flight, new_seat)}")
        except (ThisClassSeatsAreFullError, ThisSeatIsOccupiedError):
            print("Changing seat was unsuccesful")

    def generate_bording_pass(self):

        id, name = self.get_person_info()

        for person in self.people:
            if id == person.id() and name == person.name():
                person1 = person

        print("Chose your flight:\n")
        for index, flight in enumerate(flights.keys()):
            print(f"{index}) {flight}\n")

        try:
            selection = int(input())
            if 0 > selection or (len(flights) - 1) < selection:
                raise ValueError
            lst = list(flights)
            chosen_flight = flights[lst[selection]]

        except IncorectOptionError:
            print("Uncorect flight, aborting...")
            self.tick()

        try:
            you = person_is(person1, chosen_flight)

            guiMain(sys.argv, you, chosen_flight)

        except PersonNotinFlighError:
            print("No such person in flight\n")
            self.tick()

    def exit(self):
        raise StopException

    def get_input(self):
        while True:
            try:
                data = int(input())
                if data not in [0, 1, 2, 3, 4, 5, 6, 9]:
                    raise ValueError
                return data
            except IncorectOptionError:
                print("Please supply a valid action")

    def tick(self):
        self.print_options()
        selection = self.get_input()

        dict(
            {
                0: self.list_people,
                1: self.add_person,
                2: self.remove_person,
                3: self.buy_tickets,
                4: self.change_class,
                5: self.change_seat,
                6: self.generate_bording_pass,
                9: self.exit,
            }
        ).get(selection, lambda: None)()
