class Observer:
    def __init__(self, name, subject):
        self.name = name
        subject.subscribe(self)

    def notification(self, subject):
        print(f'{self.name} react to event from {subject.name}')


class Subject:
    def __init__(self, name):
        self.name = name
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notification(self):
        for obs in self._observers:
            obs.notification(self)

    def unsubscribe(self, observer):
        self._observers.remove(observer)