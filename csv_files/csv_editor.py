import csv
class csv_editor:
    def __init__(self, choice):
        self.choice = choice
        if(self.choice == 0):
            self.csv = 'csv_files/user_database.csv'
            self.cache_csv = 'csv_files/cache_user_database.csv'
            self.fieldnames = ['user_name', 'id', 'is_bot', 'joined', 'top_role']
            self.comparison = 1
        elif(self.choice == 1):
            self.csv = 'csv_files/profanity_database.csv'
            self.cache_csv = 'csv_files/cache_profanity_database.csv'
            self.fieldnames = ['key_words']
            self.comparison = 0

    def read_csv(self):
        with open(self.csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row)

    def update(self,user):
        user_name = user.name
        user_id = user.id
        user_bot = user.bot
        user_joined = user.joined_at
        user_top_role = user.top_role
        __returnmsg = ""
        __new = True
        with open(self.csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open(self.cache_csv, 'w') as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=self.fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    if(row[self.fieldnames[self.comparison]] == user_id):
                        csv_writer.writerow({self.fieldnames[0]: row[self.fieldnames[0]], self.fieldnames[1]: row[self.fieldnames[1]], self.fieldnames[2]: user_bot, self.fieldnames[3]: user_joined, self.fieldnames[4]: user_top_role})
                        __new = False
                    else:
                        csv_writer.writerow(row)
                if(__new == True):
                    csv_writer.writerow({self.fieldnames[0]: user_name, self.fieldnames[1]: user_id, self.fieldnames[2]: user_bot, self.fieldnames[3]: user_joined, self.fieldnames[4]: user_top_role})
                    __returnmsg = "Welcome " + str(user_name)
                else:
                    __returnmsg = "Welcome back " + str(user_name)
                __new = True
        with open(self.cache_csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open(self.csv, 'w') as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=self.fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                        csv_writer.writerow(row)
        return __returnmsg

    def add_profanity(self, arg):
        __returnmsg = ""
        __new = True
        with open(self.csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open(self.cache_csv, 'w') as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=self.fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    if(row[self.fieldnames[self.comparison]] == arg):
                        csv_writer.writerow({self.fieldnames[0]: row[self.fieldnames[0]]})
                        __new = False
                    else:
                        csv_writer.writerow(row)
                if(__new == True):
                    csv_writer.writerow({self.fieldnames[0]: arg})
                    __returnmsg = "Added " + str(arg) + "to filter words"
                else:
                    __returnmsg = str(arg) + " is already a filter word"
                __new = True
        with open(self.cache_csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open(self.csv, 'w') as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=self.fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                        csv_writer.writerow(row)
        return __returnmsg