# $Duskers


class GamePlay:
    tytle = r"""
     #####                   #####
    #     #   ##   #####    #     # #    # ###### ###### #    #
    #        #  #    #      #     # #    # #      #      ##   #
    #       #    #   #      #     # #    # #####  #####  # #  #
    #       ######   #      #   # # #    # #      #      #  # #
    #     # #    #   #      #    #  #    # #      #      #   ##
     #####  #    #   #       #### #  ####  ###### ###### #    # """
    
    commands = ['play', 'high', 'help', 'exit', 'back', 'yes', 'no',
                'menu', 'm', 'main', 'save', 'ex', 'up']
    
    menu = """
    |========================|
    |           MENU         |
    |                        |
    |[Back] to game          |
    | Return to [Main] Menu  |
    |[Save] and exit         |
    |[Exit] game             |
    |========================|"""
    
    def __init__(self):
        self.command = ''
    
    def ask_for_command(self):
        print()
        print('Your command:')
        self.command = input()
    
    @staticmethod
    def print_hub():
        print("""║════════════════════════════════════════════════════════════════════════════════║

  ╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬
  ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬
      ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬
     ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬
     ╬       ╬           ╬       ╬           ╬       ╬

║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║""")
    
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
            elif self.command.lower() == 'main':
                self.start()
            elif self.command.lower() == 'm':
                print(GamePlay.menu)
                self.ask_for_command()
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
                self.print_hub()
                self.ask_for_command()
            elif self.command.lower() == 'high':
                print()
                print('No scores to display.\n    [Back]')
                self.ask_for_command()
            elif self.command.lower() == 'help':
                print()
                print('Coming SOON! Thanks for playing!')
                exit()
            elif self.command.lower() == 'ex':
                print()
                print('Coming SOON! Thanks for playing!')
                exit()
            elif self.command.lower() == 'up':
                print()
                print('Coming SOON! Thanks for playing!')
                exit()
            elif self.command.lower() == 'save':
                print()
                print('Coming SOON! Thanks for playing!')
                exit()
            elif self.command.lower() == 'back':
                self.print_hub()
                self.ask_for_command()
            elif self.command.lower() == 'exit':
                print()
                print('Thanks for playing, bye!')
                exit()


new_game = GamePlay()

if __name__ == '__main__':
    new_game.start()
