import csv

class dummy:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def format(self):
        return [self.name, self.number]


class Dummys:
    def __init__(self):
        self.dummies = []
    
    def addDummy(self, Dummy: dummy):
        self.dummies.append(Dummy)
    
    def read(self):
        with open ("people.csv", "r", newline='') as file: #reads list 
            reader = csv.reader(file, delimiter =',')

            for row in reader:
                temp = dummy(row[0], row[1])
                self.addDummy(temp)

    def write(self):
        with open ("people.csv", "w", newline='') as file: #rewrites list

            writer = csv.writer(file, delimiter=',')

            for d in self.dummies:
                writer.writerow(d.format())


if __name__ == '__main__':
    collection = Dummys()
    collection.read()

    print(collection.dummies[2].name)
    








    



    



