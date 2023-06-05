"""
A production facility needs an iterable object to keep track employ working hours.
Each worker have a string name and datetime object for when he arrives to work or timedelta after he left work
Iterating the object will return all workers that have worked less than 8h (name, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to set time when arriving to workplace
    d) 10p: Method to set time when leaving from workplace
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add arrival time (arrive(name, <datetime>))
        - John, 1 Jan 2022 10:30:32
        - Ana, 1 Jan 2022 9:20:25
        - Bob, 1 Jan 2022 9:10:30
    c) 10p: Set working hours (leave(name, <datetime>))
        - John, 1 Jan 2022 18:20:00
        - Ana, 1 Jan 2022 17:30:00
        - Bob, 1 Jan 2022 9:10:30
    d) 10p: Iterate the created object and write each worker with less than 8h worked in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""

from datetime import datetime, timedelta


class WorkerIter:
    def __init__(self, workers: dict):
        self.workers = workers
        self.workers_time = []
        for name, work_time in workers.items():
            if work_time.seconds < 28800:
                self.workers_time.append((name,work_time))

    def __iter__(self):
        return self

    def __next__(self):
        if self.workers_time:
            return self.workers_time.pop()
        else:
            raise StopIteration


class Workers:
    """ class for tracking employees working hours"""
    worker = {}

    def __init__(self):
        pass

    def arrived_hour(self, name: str, dt: datetime):
        """ add arrived hour """
        self.worker[name] = dt

    def leaving_hour(self, name: str, td: datetime):
        """ add leaving hour"""
        self.worker[name] = td - self.worker[name]

    def __iter__(self):
        return WorkerIter(self.worker)


tracker = Workers()
tracker.arrived_hour('John', datetime(2022, 1, 1, 10, 30, 32))
tracker.arrived_hour('Ana', datetime(2022, 1, 1, 9, 20, 25))
tracker.arrived_hour('Bob', datetime(2022, 1, 1, 9, 10, 30))
print(tracker.worker)
print(90 * '=')
tracker.leaving_hour('John', datetime(2022, 1, 1, 18, 30, 32))
tracker.leaving_hour('Ana', datetime(2022, 1, 1, 16, 20, 25))
tracker.leaving_hour('Bob', datetime(2022, 1, 1, 14, 10, 30))
print(tracker.worker)

with open('Final.txt', 'w') as file:
    for data in tracker:
        file.write(str(data))
