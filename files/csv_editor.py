import csv
class csv_editor:
    def __init__(self):
        self.temp = 0

    def read_csv(self):
        with open('files/user_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row)
    def write_csv(self):
        with open('files/user_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('files/cache_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    csv_writer.writerow(row)
    def update(self,user_name,user_id):
        __returnmsg = ""
        __new = True
        with open('files/user_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('files/cache_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    if(row['id'] == user_id):
                        csv_writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]]})
                        __new = False
                    else:
                        csv_writer.writerow(row)
                if(__new == True):
                    csv_writer.writerow({fieldnames[0]: user_name, fieldnames[1]: user_id})
                    __returnmsg = "Welcome " + str(user_name)
                else:
                    __returnmsg = "Welcome back " + str(user_name)
                __new = True
        with open('files/cache_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('files/user_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                        csv_writer.writerow(row)
        return __returnmsg