# $Duskers 5/6
"""
Make sure you also add the saving functionality to the save and exit option.
"""
import argparse
import datetime
import logging
import os
import time
from collections import deque
from random import Random

logging.basicConfig(filename='bo.log', level=logging.DEBUG, filemode='a',
                    format='%(levelname)s - %(message)s')


save_file = 'save_file.txt'
high_file = 'high_scores.txt'


class GamePlay:
    global save_file
    n_ph = 0
    commands_stack = deque()

    def __init__(self, _seed, min_durations, max_durations, locations):
        """The initializer of the class."""
        self.min_durations = int(min_durations)
        self.max_durations = int(max_durations)
        self.locations = locations
        self.command = ''
        self.player_name = ''
        self.robot_count = 0
        self.staticmethod_object = 0
        self.search_data = dict()
        self.slots = {1: 'empty', 2: 'empty', 3: 'empty'}
        self.titanium = 0
        self.short_sleep = 0.0001
        self.game_seed = Random()
        self.game_seed.seed(_seed)

        self.animation_seed = Random()
        self.animation_seed.seed(time.time())

    tytle = r"""
     #####                   #####
    #     #   ##   #####    #     # #    # ###### ###### #    #
    #        #  #    #      #     # #    # #      #      ##   #
    #       #    #   #      #     # #    # #####  #####  # #  #
    #       ######   #      #   # # #    # #      #      #  # #
    #     # #    #   #      #    #  #    # #      #      #   ##
     #####  #    #   #       #### #  ####  ###### ###### #    # """

    robots = r"""=================================================================================

       ## ##      ## ##      ## ##
        # #        # #        # #
       #####      #####      #####
       ## ##      ## ##      ## ##
       ## ##      ## ##      ## ##"""

    panel = f"""
 =================================================================================
||                 [Ex]plore                          [Up]grade                  ||
||                 [Save]                             [M]enu                     ||
 ================================================================================="""

    commands = ['new', 'load', 'high', 'help', 'exit', 'back', 'yes', 'no',
                'menu', 'm', 'main', 'save', 'ex', 'up', 's']

    menu = """
    |========================|
    |           MENU         |
    |                        |
    |[Back] to game          |
    |Return to [Main] Menu   |
    |[Save] and exit         |
    |[Exit] game             |
    |========================|"""

    the_question = """Are you ready to begin?\n[Yes] [No] Return to [Main]Menu"""

    def __new__(cls, *args, **kwargs):
        if cls.n_ph == 0:
            cls.n_ph += 1
            return object.__new__(cls)
        return None

    def __repr__(self):
        return f'GamePlay object with:\n' \
               f'self.staticmethod_object: {self.staticmethod_object}\n'

    def __str__(self):
        return self.__repr__()

    # def random_generator(self):
    #     r = random.random()
    #     print(r)
    #     if self.min_durations < int(r * 10) < self.max_durations:
    #         print(int(r * 10))
    #     elif int(r * 10) >= self.max_durations:
    #         return self.max_durations
    #     else:
    #         return self.min_durations

    def ask_for_command(self):
        print()
        print('Your command:')
        self.command = input()
        logging.debug(f'self.command = {self.command}')
        GamePlay.commands_stack.append(self.command)

    def print_hub(self):
        print(GamePlay.robots)
        print(f'  Titanium: {self.titanium}')
        print(GamePlay.panel)

    # def play(self):
    #     print()
    #     # print('Enter your name:')
    #     self.player_name = input('Enter your name: ')
    #     print()
    #     print(f'Greetings, player {self.player_name}!')
    #     print(GamePlay.the_question)
    #     self.command = input()

    def yes(self):
        logging.info('def yes...')
        # print("Great, now let's go code some more ;)")
        GamePlay.print_hub(self)
        self.ask_for_command()

    def no(self):
        logging.debug('def no')
        self.staticmethod_object += 1
        print()
        print('How about now.')
        print(GamePlay.the_question)
        self.command = input()
        GamePlay.commands_stack.append(self.command)

    def high(self):
        logging.info('def high...')
        self.staticmethod_object += 1
        print()
        print('No scores to display.\n    [Back]')
        self.command = input()
        GamePlay.commands_stack.append(self.command)

    def help(self):
        logging.info('def help')
        self.staticmethod_object += 1
        print()
        print('Coming SOON! Thanks for playing!')
        exit()

    def animated_print(self, text, _interval):
        if self.min_durations == 0 and self.max_durations == 0:
            print(text)
        else:
            for t in text:
                print(t, end="")
                time.sleep(_interval)
            print()

    def search(self):
        logging.info('def search')
        # self.slow_print('Searching')
        print("Searching", end="")
        interval = int(self.animation_seed.randint(self.min_durations, self.max_durations))
        self.animated_print(interval * "." + "\n", 1)
        if not self.search_data:
            # random.seed(self.seed)
            # self.search_data[1] = (random.choice(self.locations), random.randint(10, 100))
            self.search_data[1] = (self.game_seed.choice(self.locations), self.game_seed.randint(10, 100))

        else:
            next_search_num = list(self.search_data.keys())[-1] + 1
            # random.seed(self.seed)
            # self.search_data[next_search_num] = (random.choice(self.locations), random.randint(10, 100))
            self.search_data[next_search_num] = (self.game_seed.choice(self.locations), self.game_seed.randint(10, 100))
        for item in self.search_data.items():
            print(f'[{item[0]}] {item[1][0]}')
        print()
        print('[S] to continue searching')
        self.ask_for_command()

    def ex(self):
        logging.info('def ex...')
        # random.seed(self.seed)
        # max_number_of_locations = random.randint(1, 9)
        max_number_of_locations = self.game_seed.randint(1, 9)

        GamePlay.search(self)
        while True:
            if self.command.lower() == 's':
                if list(self.search_data.keys())[-1] == max_number_of_locations:
                    print('Nothing more in sight.\n      [Back]\n')
                    self.command = input('Your command: ')
                else:
                    GamePlay.search(self)
            elif self.command.lower() == 'back':
                self.command = 'yes'
                break
            elif int(self.command) in list(self.search_data.keys()):
                num = int(self.command)
                # self.slow_print('Deploying robots')
                logging.info('Deploying robots')
                print("Deploying robots", end="")
                interval = int(self.animation_seed.randint(self.min_durations, self.max_durations))
                self.animated_print(interval * ".", 1)
                print(f'{self.search_data[num][0]} explored successfully, with no damage taken.')
                acquired_titanium = self.search_data[num][1]
                self.titanium += acquired_titanium
                print(f'Acquired {acquired_titanium} lumps of titanium')
                self.search_data = dict()
                self.command = 'yes'
                GamePlay.commands_stack.append(self.command)
                break

    def up(self):
        logging.info('def up')
        self.staticmethod_object += 1
        print()
        print('Coming SOON! Thanks for playing!')
        exit()

    @staticmethod
    def read_slots():
        logging.info('def read_slots')
        slots = []
        print('    Select save slot:')
        with open(save_file, 'r', encoding='utf-8') as file:
            lines = [line.strip('\n') for line in file.readlines()]
            logging.debug(lines)
            for line in lines:
                if len(line) < 3:
                    print(f'    [{line}] empty')
                    slots.append(line)
                else:
                    _data = line.split(',')
                    slots.append(_data)
                    print(f'    [{_data[0]}] {_data[1]} Titanium: {_data[2]} Robots: {_data[3]} Last save: {_data[4]}')
        return slots

    @staticmethod
    def write_to_file(data0, data1):
        # data0: ['1,ko,0,0,2022-05-27 10:41', '2', '3']
        # data1: ('1', 'ko', '0', '0', '2022-05-27 10:41')
        with open(save_file, 'w', encoding='utf-8') as file:
            for slot in data0:
                if slot[0] == '3' and slot[0] == data1[0]:
                    file.write(','.join(data1))
                elif slot[0] == data1[0]:
                    file.write(','.join(data1) + '\n')
                elif slot[0] == '3':
                    file.write(','.join(slot))
                else:
                    file.write(','.join(slot) + '\n')

    def prepare_gamesave(self, slot_num):
        return (slot_num, self.player_name, self.titanium, self.robot_count,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

    def save(self):
        logging.info('def save')
        memory_saves = self.read_slots()
        print()
        print('Your command:')
        slot_num = input()
        GamePlay.commands_stack.append(slot_num)
        # if slot_num == 'back':
        #     self.yes()
        # else:
        new_data = tuple(map(str, GamePlay.prepare_gamesave(self, slot_num)))
        self.write_to_file(memory_saves, new_data)
        print("""       ==================================
    ||    GAME SAVED SUCCESSFULLY   ||
    ==================================""")
        if GamePlay.commands_stack[-3] == 'm':
            logging.debug('GamePlay.commands_stack[-3] == m:')
            logging.info('save and exit')
            self.command = 'exit'
            GamePlay.commands_stack.append(self.command)
        else:
            self.command = 'yes'
            GamePlay.commands_stack.append(self.command)

    def load(self):
        logging.info('def load...')
        current_saves = self.read_slots()
        logging.debug(current_saves)
        print()
        print('Your command:')
        try:
            slot_num = int(input())
            GamePlay.commands_stack.append(slot_num)
            if len(current_saves[slot_num - 1]) == 1:
                print('Empty slot!')
            else:
                # let's change game params according to loaded data
                logging.debug(current_saves[slot_num - 1])
                _data_ = current_saves[slot_num - 1]
                self.player_name = _data_[1]
                self.titanium = int(_data_[2])
                self.robot_count = int(_data_[3])
                logging.debug(f"player's params: {self.player_name}, {self.titanium}, {self.robot_count}")
                print("""        ==================================
            ||    GAME LOADED SUCCESSFULLY  ||
            ==================================""")
                print(f'Welcome back, commander {self.player_name}!')
                self.command = 'yes'
                GamePlay.commands_stack.append(self.command)
        except ValueError:  # case when user enters 'back'
            self.start()

    # def save(self):
    #     self.staticmethod_object += 1
    #     print()
    #     print('Coming SOON! Thanks for playing!')
    #     exit()

    def new(self):
        logging.debug('def new')
        print()
        # print('Enter your name:')
        self.player_name = input('Enter your name: ')
        print()
        print(f'Greetings, player {self.player_name}!')
        print(GamePlay.the_question)
        self.command = input()
        GamePlay.commands_stack.append(self.command)

    actions = {
        # 'play': play,
        'new': new,
        'load': load,
        'save': save,
        'yes': yes,
        'no': no,
        'up': up,
        'ex': ex,
        'help': help,
        'high': high,
    }

    def start(self):
        logging.info('def start')
        # print(GamePlay.tytle)
        self.animated_print(GamePlay.tytle, self.short_sleep)
        print('[New]  Game')
        print('[Load] Game')
        print('[High] scores')
        print('[Help]')
        print('[Exit]')
        self.ask_for_command()

        while True:
            logging.debug(GamePlay.commands_stack)
            if self.command.lower() not in GamePlay.commands:
                print('Invalid iput')
                self.ask_for_command()
            elif self.command.lower() in GamePlay.actions:
                GamePlay.actions[self.command.lower()](self)
            elif self.command.lower() == 'main':
                self.start()
            elif self.command.lower() == 'm':
                print(GamePlay.menu)
                self.ask_for_command()
            # elif self.command.lower() == 'yes':
            #     print()
            #     # print("Great, now let's go code some more ;)")
            #     GamePlay.print_hub(self)
            #     self.ask_for_command()
            elif self.command.lower() == 'back':
                GamePlay.print_hub(self)
                self.ask_for_command()
            # elif self.command.lower() == 's':
            #     GamePlay.search(self)
            elif self.command.lower() == 'exit':
                print()
                print('Thanks for playing, bye!')
                exit()


def get_args():
    """Get arguments from command line. Return parser object with attributes."""

    parser = argparse.ArgumentParser(description="This program receives 4 arguments")
    parser.add_argument("seed", nargs='?', default='10',
                        help="Type number to set a starting point for randint")
    parser.add_argument("min_durations", type=int, nargs='?', default=0,
                        help="Specify min durations of animation")
    parser.add_argument("max_durations", type=int, nargs='?', default=0,
                        help="Specify max durations of animation")
    parser.add_argument("places", help="Type possible locations", nargs='?',
                        default='High,street/Green,park/Destroyed,Arch')
    return parser.parse_args()


def main():
    logging.info(time.asctime(time.gmtime()))
    # if not os.path.isfile(save_file):
    if not os.path.isfile("save_file.txt"):
        logging.debug('not os.path.isfile("save_file.txt")')
        with open(save_file, 'w', encoding='utf-8') as file:
            file.write('1' + '\n')
            file.write('2' + '\n')
            file.write('3')
    # if not os.path.isfile(high_file):
    if not os.path.isfile('high_scores.txt'):
        logging.debug('not os.path.isfile("high_scores.txt")')
        with open(high_file, 'w', encoding='utf-8') as file:
            file.write('')  # create empty file
    args = get_args()
    seed, min_durations, max_durations = args.seed, args.min_durations, args.max_durations
    places = args.places
    locations = [location.replace(',', ' ') for location in places.split('/')]
    logging.debug(args)
    new_game = GamePlay(seed, min_durations, max_durations, locations)
    new_game.start()


if __name__ == '__main__':
    main()
