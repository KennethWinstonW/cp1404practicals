class Project:
    def __init__(self, name='', start_date='', priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (
            f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimated_cost: {self.cost_estimate}, "
            f"completion: {self.completion_percentage}")

    def __iter__(self, other):
        return self.priority < other.priority

    def is_completed(self):
        return self.completion_percentage == 100
