from Project import (
    Person,
    PersonNotinFlighError,
    Plane_Flight,
    Flight,
    PlaneType,
    ThisClassSeatsAreFullError,
    ThisSeatIsOccupiedError,
    YouAlreadyHaveTicket,
)
from Project import buy_ticet, change_seat, change_class
import pytest

"""W testach zamiast podawać samolotowi ścierzke z plikiem z pasażerami
podaje liste pasażerów z już wybranymi klasami lotu
do metody add_passangers. Dzięki tem nie tworze dużei ilości
plików z pasażerami a także nie występuje efekt dodawania
pasażerów w nieksończoność do pliku przy każdym wywołaniu testu."""


def test_all_seat_are_full_error():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "wacek", "eco")
    lst = [person1, person2, person3, person4, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    with pytest.raises(ThisClassSeatsAreFullError):
        plane1.add_passangers(lst)


def test_all_seat_are_full_no_error():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person4 = Person(4, "Maciej", "eco")
    lst = [person1, person2, person3, person4]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)


def test_this_seat_is_Occupied_Error():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person4 = Person(4, "Maciej")
    lst = [person1, person2, person3]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisSeatIsOccupiedError):
        buy_ticet({person4: "a2"}, test_flight, "eco")


def test_this_seat_is_Occupied_Error_change_class():
    person1 = Person(1, "Jacek", "premium")
    person2 = Person(2, "Karolina", "premium")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Maciej", "eco")
    lst = [person1, person2, person3, person4]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisSeatIsOccupiedError):
        change_class(person4, test_flight, "premium", "b1")


def test_class_is_full_Error_change_class():
    person1 = Person(1, "Jacek", "premium")
    person2 = Person(2, "Karolina", "premium")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Zosia", "premium")
    person5 = Person(5, "Maciej", "eco")
    lst = [person1, person2, person3, person4, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisClassSeatsAreFullError):
        change_class(person5, test_flight, "premium")


def test_this_person_already_has_a_ticket():
    person1 = Person(1, "Jacek", "premium")
    person2 = Person(2, "Karolina", "premium")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Zosia", "premium")
    person5 = Person(5, "Maciej", "eco")
    lst = [person1, person2, person3, person4, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(YouAlreadyHaveTicket):
        buy_ticet({person5: ""}, test_flight, "bisnes")


def test_all_seats_are_full_buy_ticket():
    person1 = Person(1, "Jacek")
    person2 = Person(2, "Karolina")
    person3 = Person(3, "Jórek")
    person4 = Person(4, "Maciej")
    person5 = Person(5, "wacek")
    lst = {
        person1: "",
        person2: "",
        person3: "",
        person4: "",
        person5: "",
    }
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisClassSeatsAreFullError):
        buy_ticet(lst, test_flight, "eco")


def test_class_is_full_change_class():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "Zenek", "bisnes")
    lst = [person1, person2, person3, person4, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisClassSeatsAreFullError):
        change_class(person5, test_flight, "eco")


def test_change_class_pick_seat_taken():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person5 = Person(5, "Zenek", "bisnes")
    lst = [person1, person2, person3, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(ThisSeatIsOccupiedError):
        change_class(person5, test_flight, "eco", "a1")


def test_person_not_in_flight_Error():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person5 = Person(5, "Zenek", "bisnes")
    person6 = Person(6, "Franek", "eco")
    lst = [person1, person2, person3, person5]
    plane_type = PlaneType("Fast", (2, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(lst)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane1, "Nibylandia", 999, "24:00", prices)
    with pytest.raises(PersonNotinFlighError):
        change_class(person6, test_flight, "eco", "a1")
    with pytest.raises(PersonNotinFlighError):
        change_seat(person6, test_flight, "b2")


def test_init():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person4 = Person(4, "Jacek", "eco")
    person5 = Person(5, "Karolina", "eco")
    person6 = Person(6, "Jórek", "eco")
    person7 = Person(7, "Jórek", "eco")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers([person4, person5])
    elst = [person1, person2, person3]
    plane1.add_passangers(elst)
    assert plane1.eco()[0][0].number() == "a1"
    plane2 = Plane_Flight(plane_type)
    plane2.add_passangers([person5, person6, person7])
    assert plane2.eco()[1][0].number() == "b1"
    assert plane2.eco()[0][0].passanger() == person5


def test_buy_ticket():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person8 = Person(8, "Tomasz")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers([person1, person2, person3])
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    flight = Flight(1, plane1, "Paris", 1, "17:15", prices)
    assert buy_ticet({person8: None}, flight, "premium") == 500
    assert plane1.premium()[0][0].passanger() == person8


def test_change_class_dont_pick_seat():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "eco")
    person8 = Person(8, "Tomasz", "eco")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers([person1, person2, person3, person8])
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    flight = Flight(1, plane1, "Paris", 1, "17:15", prices)
    assert change_class(person8, flight, "premium") == 400
    assert plane1.premium()[0][0].passanger() == person8


def test_buy_ticket_change_seat():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "wacek", "bisnes")
    person6 = Person(6, "Zenek", "bisnes")
    person7 = Person(7, "Błażej", "bisnes")
    person8 = Person(8, "Tomasz")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    passengers = [
        person1,
        person2,
        person3,
        person4,
        person5,
        person6,
        person7,
    ]
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(passengers)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    flight = Flight(1, plane1, "Paris", 1, "17:15", prices)
    assert buy_ticet({person8: None}, flight, "premium") == 500
    assert plane1.premium()[0][1].passanger() == person8
    change_seat(person4, flight, "b1")
    assert plane1.eco()[1][0].passanger() == person4
    change_seat(person5, flight, "e6")
    change_seat(person6, flight, "e5")
    assert plane1.bisnes()[4][5].passanger() == person5
    assert plane1.bisnes()[4][4].passanger() == person6
    assert plane1.bisnes()[0][0].passanger() is None


def test_change_seat_fill_seat():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "wacek", "bisnes")
    person6 = Person(6, "Zenek", "bisnes")
    person7 = Person(7, "Błażej", "bisnes")
    person8 = Person(8, "Tomasz", "bisnes")
    person9 = Person(9, "Weronika", "bisnes")
    person10 = Person(10, "Karol", "bisnes")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    passengers = [
        person1,
        person2,
        person3,
        person4,
        person5,
        person6,
        person7,
    ]
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(passengers)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    flight = Flight(1, plane1, "Paris", 1, "17:15", prices)
    change_seat(person4, flight, "b1")
    assert plane1.eco()[1][0].passanger() == person4
    change_seat(person5, flight, "e6")
    change_seat(person6, flight, "e5")
    assert plane1.bisnes()[4][5].passanger() == person5
    assert plane1.bisnes()[4][4].passanger() == person6
    assert plane1.bisnes()[0][0].passanger() is None
    pasangers_filling = [person8, person9, person10]
    plane1.add_passangers(pasangers_filling)
    assert plane1.bisnes()[0][0].passanger() == person8


def test_change_seat_class_buy_ticket_multiple():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "wacek", "bisnes")
    person6 = Person(6, "Zenek", "bisnes")
    person7 = Person(7, "Błażej", "bisnes")
    person8 = Person(8, "Tomasz", "bisnes")
    person9 = Person(9, "Weronika")
    person10 = Person(10, "Karol")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    passengers = [
        person1,
        person2,
        person3,
        person4,
        person5,
        person6,
        person7,
    ]
    plane1 = Plane_Flight(plane_type)
    plane1.add_passangers(passengers)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    flight = Flight(1, plane1, "Paris", 1, "17:15", prices)
    change_seat(person4, flight, "b1")
    assert plane1.eco()[1][0].passanger() == person4
    change_seat(person5, flight, "e6")
    change_seat(person6, flight, "e5")
    assert plane1.bisnes()[4][5].passanger() == person5
    assert plane1.bisnes()[4][4].passanger() == person6
    assert plane1.bisnes()[0][0].passanger() is None
    pasangers_filling = [person8]
    plane1.add_passangers(pasangers_filling)
    assert plane1.bisnes()[0][0].passanger() == person8
    people = {person9: "c3", person10: "c4"}
    buy_ticet(people, flight, "bisnes")
    assert plane1.bisnes()[2][2].passanger() == person9


def test_database_file():
    person1 = Person(1, "Jacek", "eco")
    person2 = Person(2, "Karolina", "eco")
    person3 = Person(3, "Jórek", "premium")
    person4 = Person(4, "Maciej", "eco")
    person5 = Person(5, "wacek", "bisnes")
    person6 = Person(6, "Zenek", "bisnes")
    person7 = Person(7, "Błażej", "bisnes")
    person8 = Person(8, "Tomasz", "bisnes")
    person9 = Person(9, "Weronika", "premium")
    person10 = Person(10, "Karol", "premium")
    plane_type = PlaneType("Fast", (4, 2), (6, 5), (2, 2))
    plane_type2 = PlaneType("Not that Fast", (6, 10), (6, 5), (4, 2))
    passengers1 = [person1, person2, person3, person4, person5]
    passengers2 = [person6, person7, person8, person9, person10]
    plane1 = Plane_Flight(plane_type)
    plane2 = Plane_Flight(plane_type2)
    plane1.add_passangers(passengers1)
    plane2.add_passangers(passengers2)
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    Flight(1, plane1, "Paris", 1, "17:15", prices)
    Flight(2, plane2, "Berlin", 3, "23:15", prices)


def test_get_passengers_from_test_file():
    plane_type = PlaneType("Fast", (5, 3), (6, 5), (2, 2))
    plane = Plane_Flight(plane_type, "flight_test.json")
    prices = {"eco": 100, "bisnes": 250, "premium": 500}
    test_flight = Flight(999, plane, "Nibylandia", 999, "24:00", prices)
    assert plane.premium()[1][0].passanger().name() == "Karol"
    person1 = Person(11, "Bożena Boska")
    person2 = Person(12, "Naopleon Bonaparte")
    people = {person1: "b1", person2: "b3"}
    buy_ticet(people, test_flight, "bisnes")
    assert plane.bisnes()[1][2].passanger() == person2
    person3 = Person(6, "Zenek", "bisnes")
    change_seat(person3, test_flight, "a5")
