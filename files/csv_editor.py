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
            with open('files/new_user_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id','status']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    csv_writer.writerow(row)
    def update(self,user_id):
        with open('files/user_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('files/new_user_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id','status']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    if(row['id'] == user_id):
                        csv_writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]], fieldnames[2]: 'online'})
                    else:
                        csv_writer.writerow(row)
        with open('files/new_user_database.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('files/user_database.csv', 'w') as new_file:
                fieldnames = ['user_name', 'id','status']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                        csv_writer.writerow(row)