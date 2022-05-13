# !/usr/bin/python
# -*- coding: utf-8
# $Duskers


class GamePlay:
    tytle = r"""
        __   ____  ______       ___   __ __    ___    ___  ____
       /  ] /    ||      |     /   \ |  |  |  /  _]  /  _]|    \
      /  / |  o  ||      |    |     ||  |  | /  [_  /  [_ |  _  |
     /  /  |     ||_|  |_|    |  Q  ||  |  ||    _]|    _]|  |  |
    /   \_ |  _  |  |  |      |     ||  :  ||   [_ |   [_ |  |  |
    \     ||  |  |  |  |      |     ||     ||     ||     ||  |  |
     \____||__|__|  |__|       \__,_| \__,_||_____||_____||__|__|"""
    
    commands = ['play', 'high', 'help', 'exit', 'back', 'yes', 'no', 'menu']
    
    hub = """
    --------------(LOG)-------------------------------(LOG)--------------------------
    |********************************************************************************|
    |--------------------------------------------------------------------------------|
    |------------(ROBOT IMAGES)------------------------------------------------------|
    |--------------------------------------------------------------------------------|
    |--------------------------------------------------------------------------------|
    |--------------------------------------------------------------------------------|
    |--------------------------------------------------------------------------------|
    |--------------------------------------------------------------------------------|
    |================================================================================|
    |                  [Ex]plore                          [Up]grade                  |
    |                  [Save]                             [M]enu                     |
    |********************************************************************************|"""
    
    def __init__(self):
        self.command = ''
    
    def ask_for_command(self):
        print()
        print('Your command:')
        self.command = input()
    
    def start(self):
        print(GamePlay.tytle)
        print('[Play]')
        print('[High] scores')
        print('[Help]')
        print('[Exit]')
        self.ask_for_command()
    
        while True:
            the_question = """Are you ready to begin?\n[Yes] [No] Return to Main[Menu]"""
            if self.command.lower() not in GamePlay.commands:
                print('Invalid input')
                self.ask_for_command()
            elif self.command.lower() == 'menu':
                self.start()
            elif self.command.lower() == 'play':
                print()
                print('Enter your name:')
                player_name = input()
                print()
                print(f'Greetings, player {player_name}!')
                print(the_question)
                self.ask_for_command()
            elif self.command.lower() == 'no':
                print()
                print('How about now.')
                print(the_question)
                self.ask_for_command()
            elif self.command.lower() == 'yes':
                print()
                # print("Great, now let's go code some more ;)")
                print(GamePlay.hub)
                exit()
            elif self.command.lower() == 'high':
                print()
                print('No scores to display.\n    [Back]')
                self.ask_for_command()
            elif self.command.lower() == 'help':
                print()
                print('Coming SOON! Thanks for playing!')
                exit()
            elif self.command.lower() == 'back':
                self.start()
            elif self.command.lower() == 'exit':
                print()
                print('Thanks for playing, bye!')
                exit()


new_game = GamePlay()

if __name__ == '__main__':
    new_game.start()
