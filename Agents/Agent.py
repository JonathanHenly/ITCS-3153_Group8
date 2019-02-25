class Agent:

    def __init__(self):
        self.name = ''
        self.env = ''
        self.act = []
        self.sen = []
        self.met = []
    
    def __init__(self, name, environment, actuators, sensors, metrics):
        self.name = name
        self.env = environment
        self.act = actuators
        self.sen = sensors
        self.met = metrics

    def print(self):
        print(f"name: {self.name}\n  environment: {self.env}\n  actuators: {self.act}\n  sensors: {self.sen}\n  performace metrics: {self.met}")

vc = Agent('Vaccum Cleaner', 'Living Room', ['motor', 'person'], ['', 'bfoo'], ['fast', 'slow'])
vc.print()

htub = Agent('Hot Tub', 'Back Porch', ['pump', 'heaters', 'jets'], ['thermometer', 'water gauge'], ['cubic liters per second', 'delta degrees celcius per second'])
