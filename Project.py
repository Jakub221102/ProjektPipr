import json


class AlreadyInThisClassErorr(Exception):
    def __init__(self):
        super().__init__("You are already in this class")


class YouAlreadyHaveTicket(Exception):
    def __init__(self):
        super().__init__("You can only have one seat")


class ThisClassSeatsAreFullError(Exception):
    def __init__(self):
        super().__init__("All seats in this class have been taken.")


class ThisSeatIsOccupiedError(Exception):
    def __init__(self):
        super().__init__("This seat is already occupied.")


class PersonNotinFlighError(Exception):
    def __init__(self):
        super().__init__("There is no such person in this flight")


class MalformedPersonDataError(Exception):
    pass


class InvalidPersonError(Exception):
    def __init__(self, tokens):
        super().__init__("Invalid person data detected")
        self.tokens = tokens


"""
Classa Person. Zawiera atrybuty:
id: numer reprezentujący np pessel osoby
name: imie i nazwisko osoby
fligh_class: tymczasowy argument który pozwala przypisać osobę
do dobrej klasy lotu i ułatwia testowanie
seat: słownik który zawiera "miejsca/siedzenia które osoba kupiła"
postać słownika jest z powodowana tym, że jedna osoba może mieć kika miejsc
w kilku różnych lotach jednocześnie.
"""


class Person:
    def __init__(self, id, name, flight_class=None):
        self._id = id
        self._name = name
        self._flight_class = flight_class
        self._seat = None

    def set_id(self, id):
        if id:
            if not isinstance(id, int):
                raise TypeError
        self._id = id

    def id(self):
        return self._id

    def set_name(self, name):
        if name:
            if not isinstance(name, str):
                raise TypeError
        self._name = name

    def name(self):
        return self._name

    def set_flight_class(self, flight_class):
        self._flight_class = flight_class

    def flight_class(self):
        return self._flight_class

    def set_seat(self, plane, seat):
        self._seat = {plane: seat}

    def add_seat(self, plane, seat):
        if self._seat:
            self._seat[plane] = seat
        else:
            self.set_seat(plane, seat)

    def seat(self):
        return self._seat

    def __str__(self):
        return f"{self._id} {self._name}"


"""
Classa reprezentująca typ samolotu. Zawiera atrybuty takie jak:
plane_type: typ samolotu np "Boing 737" u mnie np są to typy "Fast", "slow" itp
eco: Wymiary obszaru klasy ekonomicznej w jednostkach siedzeń (4, 10) oznacza,
że jest 10 rzędów po 4 siedzenia każdy/
bisnes: analogicznie jak dla eco tylko dla klasy biznesowej
premium: analogicznie jak dla eco tylko dla klasy premium
"""


class PlaneType:
    def __init__(self, plane_type, eco, bisnes, premium):
        self._plane_type = plane_type
        self.set_eco(eco)
        self.set_bisnes(bisnes)
        self.set_premium(premium)

    def set_plane_type(self, plane_type):
        self._plane_type = plane_type

    def plane_type(self):
        return self._plane_type

    def set_eco(self, eco):
        self._eco = eco

    def eco(self):
        return self._eco

    def set_bisnes(self, bisnes):
        self._bisnes = bisnes

    def bisnes(self):
        return self._bisnes

    def set_premium(self, premium):
        self._premium = premium

    def premium(self):
        return self._premium


""" Classa Seat reprezentuje obiekt siedzenia zawiera atrybuty:
passanger: jest to obiekt pasażera, który obecnie zajmuje to miejsce.
Dla różnych lotów nawet jeżeli odbywają się tym samym typem samolotu
obiekty siedzeń są różne, obiekt siedzenia istnieje w momęcie kiedy
istnieje lot number: jest to numer siedzenia np (a1) (b3) itp,
taki sposób numerowania ogranicza nas
do ilości rzędów jaki może mieć samolot ale jeżeli był by to problem i samoloty
miały by więcej rzędów w klasie niż liter w alfabecie można by przenieść się na
sposób numeracj samymimi liczbami np (1:1) odpowiadoało by naszemu (a:1)"""


class Seat:
    def __init__(self, passanger, number):
        self._passanger = passanger
        self._number = number

    def set_passanger(self, passanger):
        if passanger:
            self._passanger = passanger
        else:
            self._passanger = None

    def passanger(self):
        return self._passanger

    def set_number(self, number):
        self._number = number

    def number(self):
        return self._number

    def __str__(self):
        if self._passanger:
            return f"({self._number} X)"
        else:
            return f"({self._number} O)"


"""Classa Pasangers: jest klasą która umożliwia interfejsowi pamiętanie zmian
imituje ona działanie bazy danych poprzez wczytywanie obiektów osób,
które już zakupiły swoje bilety i mają przydzielone siedzenia, miejsca.
Przyjmuje ona jako argumenty:
path: ścierzka do pliku json który imituje działanie bazy danych.
plane: obiekt samolotu, który w tym wypadku można utożsamiać bardziej z
obiekem samolotu w locie niż samego samolotu jak w rzeczywistości
istnieje on po to aby klasa lot nie miała 300 linijek kodu,
roździela jej działanie na dwie klassy."""


class Pasangers:
    def __init__(self, path, plane):
        self.load_form_json(path, plane)

    def load_form_json(self, path, plane):
        with open(path, "r") as file_handle:
            self._passangers = self.read_from_jason(file_handle, plane)

    def lstpassangers(self):
        return self._passangers

    def read_from_jason(self, file_handle, plane):
        passengers = []
        data = json.load(file_handle)
        for item in data:
            try:
                id = item["id"]
                name = item["name"]
                nrseat = item["seat"]
                clasa = item["class"]
                person = Person(id, name, clasa)
                for row in plane.get_class(clasa):
                    for item in row:
                        if item.number() == nrseat:
                            seatobj = item
                person.add_seat(plane, seatobj)
                seatobj.set_passanger(person)
            except KeyError as e:
                raise MalformedPersonDataError("Missing key in file") from e
            except Exception as e:
                raise InvalidPersonError(item) from e
            passengers.append(person)
        return passengers


"""Obiekt samolotu który tworzy tablice 2D obiektów siedzeń
w zależności od typu samolotu jakim jest. Przyjmuje argumenty:
plane_type: Czyli typ samolotu jakim jest z tą zna swoje wymiary,
path: ścierzka do pliku z osobami które już zakupiły bilety i mają
przydzielona miejsca"""


class Plane_Flight:
    def __init__(self, plane_type, path=None):
        self.set_plane_type(plane_type)
        self.set_eco()
        self.set_bisnes()
        self.set_premium()
        self.set_passangers(path)

    def set_plane_type(self, plane_type):
        self._plane_type = plane_type

    def plane_type(self):
        return self._plane_type

    def set_eco(self):
        self._eco = self.form_rows(self._plane_type.eco())

    def eco(self):
        return self._eco

    def set_bisnes(self):
        self._bisnes = self.form_rows(self._plane_type.bisnes())

    def bisnes(self):
        return self._bisnes

    def set_premium(self):
        self._premium = self.form_rows(self._plane_type.premium())

    def premium(self):
        return self._premium

    """Metoda set_passangers przypisuje do listy pasażerów obiekty osób
    z pliku imitującego baze danych z osobami, które już posiadają miejca
    w tym samolocie"""

    def set_passangers(self, path):
        if path:
            obj = Pasangers(path, self)
            self._passangers = obj.lstpassangers()
        else:
            self._passangers = []

    def passangers(self):
        return self._passangers

    def get_class(self, clasa):
        if clasa == "eco":
            return self._eco
        elif clasa == "bisnes":
            return self._bisnes
        elif clasa == "premium":
            return self._premium

    """
    Metoda która tworzy tablice 2D z obiektów siedzeń dla poszczególnych klas
    """

    def form_rows(self, dimentions):
        coding_letters = [chr(i) for i in range(97, 97 + dimentions[1])]
        class_seats = [
            [
                Seat(None, f"{coding_letters[row]}{seat+1}")
                for seat in range(dimentions[0])
            ]
            for row in range(dimentions[1])
        ]
        return class_seats

    """Metoda słóżąca do dodawania nowych osób które zakupiły bilety
    ale nie zdecydowały się na dodatkową opcje zakupu miejca"""

    def add_passangers(self, new_passangers):
        if new_passangers:
            for passenger in new_passangers:
                if not isinstance(passenger, Person):
                    raise TypeError
                self._passangers.append(passenger)
            self.sort_passangers(new_passangers)

    """Metoda, która przydziela miejsce osobom które nie zdecydowały się
    na wybór miejca, wypełnia ona tymi osobami po kolei wolne siedzenia w
    danej klasie siedzeń samolotu"""

    def sort_passangers(self, passangers):
        eco = []
        bisnes = []
        premium = []
        for passenger in passangers:
            if passenger.flight_class() == "eco":
                eco.append(passenger)
            elif passenger.flight_class() == "bisnes":
                bisnes.append(passenger)
            elif passenger.flight_class() == "premium":
                premium.append(passenger)

        if eco:
            for row in self._eco:
                j = 0
                for seat in row:
                    if eco:
                        for eco_passenger in eco:
                            if seat.passanger() is None:
                                seat.set_passanger(eco_passenger)
                                eco_passenger.add_seat(self, seat)
                                eco.remove(eco_passenger)
                                j += 1
        if eco:
            class_is_full(self, "eco")

        if bisnes:
            for row in self._bisnes:
                j = 0
                for seat in row:
                    if bisnes:
                        for bisnes_passenger in bisnes:
                            if seat.passanger() is None:
                                seat.set_passanger(bisnes_passenger)
                                bisnes_passenger.add_seat(self, seat)
                                bisnes.remove(bisnes_passenger)
                                j += 1
        if bisnes:
            class_is_full(self, "bisnes")

        if premium:
            for row in self._premium:
                j = 0
                for seat in row:
                    if premium:
                        for premium_passenger in premium:
                            if seat.passanger() is None:
                                seat.set_passanger(premium_passenger)
                                premium_passenger.add_seat(self, seat)
                                premium.remove(premium_passenger)
                                j += 1
        if premium:
            class_is_full(self, "premium")


""""Classa reprezentująca lot: Przyjmuje argumenty:
number: numer lotu,
plane: obiekt samolotu którym lot się odbędzie,
który zawiera pasażerów tego lotu,
destination: cel podróży,
gate: numer bramiki odlotu,
time_of_departure: godzina odlotu,
prcies: słownik z cenami dla poszczególnych klas"""


class Flight:
    def __init__(
        self,
        number,
        plane,
        destination,
        gate,
        time_of_departure,
        prices,
    ):
        self._number = number
        self._plane = plane
        self._destination = destination
        self._gate = gate
        self._time_of_departure = time_of_departure
        self._prices = prices
        self.set_database()

    def set_number(self, number):
        self._number = number

    def number(self):
        return self._number

    def set_plane(self, plane):
        self._plane = plane

    def plane(self):
        return self._plane

    def set_destination(self, destination):
        self._destination = destination

    def destination(self):
        return self._destination

    def set_gate(self, gate):
        self._gate = gate

    def gate(self):
        return self._gate

    def set_time_of_departure(self, time_of_departure):
        self._time_of_departure = time_of_departure

    def time_of_departure(self):
        return self._time_of_departure

    def set_prices(self, prices):
        self._prices = prices

    def prices(self):
        return self._prices

    """Metoda wywołująca instancje klasy DatabasePlane:
    otrzymujemy w ten sposób słowniki dla poszczególnych klas miejsc
    które jako klucz przyjmują numer siedzenia
    a jako wartość obiekt tego siedzenia,
    dodatkowo zapisujemy wszystkie osoby, które zakupiły bilet
    do pliku, który imituje działanie bazy danych."""

    def set_database(self):
        self._database = DatabasePlane(
            self._plane, f"flight{self._number}.json"
        )

    def database(self):
        return self._database


"""Classa która zajmuje się towrzeniem słowników siedzeń
i zapisywania plików dla classy FLight.
Przyjmuje argumenty:
plane: obiekt samolotu którym odbywa się lot,
path: scieżka do pliku do którego zapisać liste pasażerów"""


class DatabasePlane:
    def __init__(self, plane, path):
        self.set_plane(plane)
        self.set_dict_eco()
        self.set_dict_bisnes()
        self.set_dict_premium()
        self.save_to_file(path)

    def set_plane(self, plane):
        self._plane = plane

    def plane(self):
        return self._plane

    def set_dict_eco(self):
        dict_eco = {}
        self._dict_eco = self.form_dic(self._plane.eco(), dict_eco)

    def dict_eco(self):
        return self._dict_eco

    def set_dict_bisnes(self):
        dict_bisnes = {}
        self._dict_bisnes = self.form_dic(self._plane.bisnes(), dict_bisnes)

    def dict_bisnes(self):
        return self._dict_bisnes

    def set_dict_premium(self):
        dict_premium = {}
        self._dict_premium = self.form_dic(self._plane.premium(), dict_premium)

    def dict_premium(self):
        return self._dict_premium

    def get_dict(self, clasa):
        if clasa == "eco":
            return self._dict_eco
        elif clasa == "bisnes":
            return self._dict_bisnes
        elif clasa == "premium":
            return self._dict_premium

    def form_dic(self, clasa, dictionary):
        for row in clasa:
            for seat in row:
                dictionary[seat.number()] = seat
        return dictionary

    def save_to_file(self, path):
        with open(path, "w", encoding="UTF-8") as self._file_handle:
            self.write_to_json(self._plane.passangers())

    def write_to_json(self, passangers):
        data = []
        for person in passangers:
            id = person.id()
            name = person.name()
            seat = person.seat()[self._plane].number()
            clasa = person.flight_class()
            person_data = {
                "id": id,
                "name": name,
                "seat": seat,
                "class": clasa,
            }
            data.append(person_data)
        json.dump(data, self._file_handle, indent=4, ensure_ascii=False)


"""Metoda buy ticket umożliwia kupowania biletów dla wielu osób, w danej klasie
dodatkowo za opłatą daje nam możlwiość wyboru miejsca dla poszczególnych osób
Przyjmuje argumenty:
people: jest to słownik z kluczmi, którymi są obiekty osoby
a jako wartości numery siedzeń na kótórych dane osoby chcą siedzieć
jezeli wartość nie zostanie podana miejsce zostaje przydzielone
danej osobie losowo za pomocą funkcji add_passangers bez dodatkwej opłaty,
flight: lot na, który bilety chcemy zakupić,
fligh_class: klasa siedzeń do, której chcemy kupić bilety."""


def buy_ticet(people, flight, flight_class):
    i = 0
    price_to_pay = 0
    for person in people.keys():
        if person.seat():
            if flight.plane() in person.seat().keys():
                raise YouAlreadyHaveTicket
        seat = people[person]
        if isinstance(person, Person):
            person.set_flight_class(flight_class)
            if seat:
                seat_obj = flight.database().get_dict(person.flight_class())[
                    seat
                ]
                if seat_obj.passanger():
                    raise ThisSeatIsOccupiedError
                seat_obj.set_passanger(person)
                person.add_seat(flight.plane(), seat_obj)
                price_to_pay += 50
                flight.plane().passangers().append(person)
            else:
                flight.plane().add_passangers([person])
            price_to_pay += flight.prices()[flight_class]
            i += 1
        flight.set_database()
    return price_to_pay


"""Metoda pozwalająca na zmiane obecnej klasy lotu na nową,
Przyjmuje ona argumenty:
person: obiekt osoby dla której chcemy zmienić klase lotu
wystartczy podanie id i name, i jeżeli osoba o podanym id i imieniu
znajduje się w liście pasażerów danego lotu to jej klasa zostanie zmieniona
fligh: lot w którym chcemu zmienic klase,
new_class: nowa klasa na którą chcemy zmienić naszą obecną klase,
new_seat: opcjonalnie za opłatą możma wybrać sobie w nowej klasie miejsce"""


def change_class(person, flight, new_class, new_seat=None):
    person = person_is(person, flight)
    if new_class == person.flight_class():
        raise AlreadyInThisClassErorr
    old_class = person.flight_class()
    class_is_full(flight.plane(), new_class)
    person.set_flight_class(new_class)
    seat_change_fee = 0

    if new_seat:
        seat = flight.database().get_dict(person.flight_class())[new_seat]
        if seat.passanger():
            raise ThisSeatIsOccupiedError
        person.seat()[flight.plane()] = None
        seat.set_passanger(person)
        person.add_seat(flight.plane(), seat)
        seat_change_fee = 50
    else:
        person.seat()[flight.plane()] = None
        flight.plane().add_passangers([person])
    price_to_pay = flight.prices()[new_class] - flight.prices()[old_class]
    flight.set_database()
    if price_to_pay < 0:
        price_to_pay = seat_change_fee
    return price_to_pay


"""Metoda pozwalająca na zmiane miejca w obrębie danej klasy.
Przyjmuje jako argumenty:
person: obiekt osoby dla której zmieniamy miejsce,
flight: lot tej osoby, w którym chcemy zmienić miejsce,
new_seat: numer nowego siedzenia"""


def change_seat(person, flight, new_seat):
    person = person_is(person, flight)
    seat = flight.database().get_dict(person.flight_class())[new_seat]
    if seat.passanger():
        raise ThisSeatIsOccupiedError
    person.seat()[flight.plane()].set_passanger(None)
    seat.set_passanger(person)
    person.add_seat(flight.plane(), seat)
    flight.set_database()
    seat_change_fee = 50
    return seat_change_fee


"""Metoda sprawdzająca czy dana osoba o danym id i name znajduje się
w liscie pasażeów tego lotu i jeżeli tak
pozwala na zmiane np: siedzenia czy klasy tej osoby"""


def person_is(person, flight):
    for obj in flight.plane().passangers():
        if obj.id() == person.id() and obj.name() == person.name():
            person1 = obj
            return person1
    raise PersonNotinFlighError


def class_is_full(plane, clasa):
    all_seats_are_full = True
    seats = plane.get_class(clasa)
    for row in seats:
        for seat in row:
            if seat.passanger() is None:
                all_seats_are_full = False

    if all_seats_are_full is True:
        raise ThisClassSeatsAreFullError
    else:
        pass
