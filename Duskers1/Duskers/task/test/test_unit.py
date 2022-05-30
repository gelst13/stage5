from sys import argv
import random

# see interactive_test() for idea how this algorithm should be implemented in
# order to pass tests
# run in command line with same arguments as duskers.py for demo

place_names = ["place1", "place2", "place3"]


class TestData:
    def __init__(self, seed: int, places: str, robot_count: int, strategy: str, start: int):
        self.seed = seed
        self.strategy = strategy
        self.places = places
        self.robot_count = robot_count
        self.start = start


def generate(n):
    result = []
    for _ in range(n):
        place_name = random.choice(place_names)
        place_titanium = random.randint(10, 100)
        encounter_rate = random.random()
        result.append([place_name, place_titanium, encounter_rate])
    return result


def encounter(data):
    encounter_number = random.random()
    for i in range(len(data)):
        if encounter_number < data[i][2]:
            data[i].append(True)
        else:
            data[i].append(False)
    return encounter_number


def interactive_test():
    no_of_places = random.randint(1, 9)
    print("Number of places:", no_of_places)
    no_of_searches = int(input("How many searches: "))
    data = generate(no_of_searches)
    print("Encounter number:", encounter(data))
    print(data)
    print()


def interactive_loop_test(n):
    global_encounters = 0
    global_locations = 0
    for i in range(n):
        no_of_places = random.randint(1, 9)
        global_locations += no_of_places
        data = generate(no_of_places)
        encounter(data)
        print(data)
        encounters = 0
        for item in data:
            if item[3]:
                encounters += 1
        global_encounters += encounters
        print("Encountered:", encounters, "of", no_of_places)
    print("TOTAL ENCOUNTERS:", global_encounters, "of", global_locations)


def third_item(tup):
    return tup[2]


def minimise_maximise(n: int, strategy: int):
    """n - represents amount of lives / robots
    stratgy, 0 means minimising, -1 means maximising"""
    i = 0
    titanium_total = 0
    chosen = []
    total_data = []
    while n > 0:
        i += 1
        no_of_places = random.randint(1, 9)
        data = generate(no_of_places)
        ordered_data = data[:]
        total_data.append(ordered_data)
        encounter(data)
        data.sort(key=third_item)
        chosen.append(ordered_data.index(data[strategy]) + 1)
        if data[strategy][3]:
            n -= 1
        if n > 0:
            titanium_total += data[strategy][1]
    if __name__ == "__main__":
        print(*total_data, sep="\n")
        print("Choices:", chosen)
        print("Game over on round", i)
        print("Gathered:", titanium_total, "titanium")
    return titanium_total, chosen, i, total_data


def init_test(test_case: TestData):
    global place_names
    random.seed(test_case.seed)
    place_names = []
    argv_places = test_case.places.split("/")
    for item in argv_places:
        place = " ".join(item.split(","))
        place_names.append(place)

    if test_case.strategy == "min":
        return minimise_maximise(test_case.robot_count, 0)
    elif test_case.strategy == "max":
        return minimise_maximise(test_case.robot_count, -1)


if __name__ == "__main__":

    if len(argv) == 5:
        random.seed(a=argv[1])
        wait_time_min = int(argv[2])
        wait_time_max = int(argv[3])
        place_names = []
        argv_places = argv[4].split("/")
        for item in argv_places:
            place = " ".join(item.split(","))
            place_names.append(place)
    else:
        print("Incorrect parameters")
        exit()

    while True:
        comm = input("Commands:\nall(n) to loop n times searching all locations\n"
                     "max(n) to search all locations selecting the one with highest encounter"
                     "rate, until all live - n - are used up\nmin(n) same thing but chooses"
                     "lowest available ecnounter rate, both max and min return number of rounds survived\n"
                     "Type 'exit()' to exit or any other character(s) to continue" \
                     " testing interactively: ")
        comm = comm.strip()
        if comm == "exit()":
            break
        if "all(" in comm and ")" in comm:
            interactive_loop_test(int(comm[4:-1]))
        elif "min(" in comm and ")" in comm:
            minimise_maximise(int(comm[4:-1]), 0)
        elif "max(" in comm and ")" in comm:
            minimise_maximise(int(comm[4:-1]), -1)
        else:
            interactive_test()