# Easy Rider Bus Company 3/6
import logging
import json
import re

logging.basicConfig(filename='bo.log', level=logging.DEBUG, filemode='a',
                    format='%(levelname)s - %(message)s')


class Rider:
    fields = {'bus_id': int,
              'stop_id': int,
              'stop_name': str,
              'next_stop': int,
              'stop_type': str,  # 1 character
              'a_time': str}

    format_errors = {'stop_name': 0,
                     'stop_type': 0,
                     'a_time': 0}

    def __init__(self):
        self.data = None
        self.errors = {'bus_id': 0,
                       'stop_id': 0,
                       'stop_name': 0,
                       'next_stop': 0,
                       'stop_type': 0,
                       'a_time': 0}
        self.format_errors = {'stop_name': 0,
                              'stop_type': 0,
                              'a_time': 0}
        self.bus_lines = dict()

    def get_data(self):
        self.data = json.loads(input())
        # _str = '[{"bus_id" : 128, "stop_id" : 3, "stop_name" : "", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : "7", "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : "", "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : ""}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : "0", "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : "512", "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : 5, "a_time" : "08:16"}]'
        # self.data = json.loads(_str)

    def check_type(self):
        """Check that the data types match.
        Check that the required fields are filled in."""
        logging.info('...def check1...')
        for entry in self.data:
            logging.debug(entry)
            for key in list(Rider.fields.keys()):
                count = 0
                if key == 'stop_type':
                    if not (isinstance(entry[key], str)) or (isinstance(entry[key], str) and len(entry[key]) > 1):
                        logging.debug(key)
                        count += 1
                elif not (type(entry[key]) == Rider.fields[key]):
                    logging.debug(key)
                    count += 1
                elif key in ('stop_name', 'a_time'):
                    if not (len(entry[key]) > 0):
                        logging.debug(key)
                        count += 1
                current_count = self.errors[key]
                self.errors.update({key: current_count + count})
        logging.debug(self.errors)

    def check_format(self):
        """Check that the data format complies with the documentation."""
        logging.info('...def check_format...')
        count0, count1, count2 = 0, 0, 0
        for entry in self.data:
            logging.debug(entry)
            correct_suffix = re.match(r'[A-Z].+[ ](?=Road$|Avenue$|Boulevard$|Street$)', entry['stop_name'])
            if not (correct_suffix and len(entry['stop_name']) > 0):
                logging.debug('stop_name')
                count0 += 1
            if entry['stop_type'] not in ('S', 'O', "F", ""):
                logging.debug('stop_type')
                count1 += 1
            military_time = re.match(r'^([01]\d|2[0-3]):?([0-5]\d)$', entry['a_time'])
            if not military_time and len(entry['a_time']) > 0:
                logging.debug('a_time')
                count2 += 1
        self.format_errors.update({'stop_name': count0})
        self.format_errors.update({'stop_type': count1})
        self.format_errors.update({'a_time': count2})
        logging.debug(self.format_errors)

    def check_lines(self):
        """how many bus lines we have and how many stops there are on each line"""
        logging.info('...def check_lines...')
        for entry in self.data:
            logging.debug(entry['bus_id'], entry['stop_id'])
            if entry['bus_id'] not in list(self.bus_lines.keys()):
                if entry['bus_id'] != '':
                    self.bus_lines[entry['bus_id']] = [entry['stop_id'], ]
            else:
                current_values = self.bus_lines[entry['bus_id']]
                current_values.append(entry['stop_id'])
                self.bus_lines.update({entry['bus_id']: current_values})
        logging.debug(self.bus_lines)

    def display_errors(self):
        # print(f'Type and required field validation: {sum(list(self.errors.values()))} errors')
        # for key, value in self.errors.items():
        #     print(f'{key}: {value}')
        # logging.debug(sum(list(self.format_errors.values())))
        # print(f'Format validation: {sum(list(self.format_errors.values()))} errors')
        # for key, value in self.format_errors.items():
        #     print(f'{key}: {value}')
        print('Line names and number of stops:')
        for key, value in self.bus_lines.items():
            print(f'bus_id: {key}, stops: {len(value)}')

    def validation(self):
        self.get_data()
        # self.check_type()
        # self.check_format()
        self.check_lines()
        self.display_errors()


def main():
    new = Rider()
    new.validation()


if __name__ == '__main__':
    main()

