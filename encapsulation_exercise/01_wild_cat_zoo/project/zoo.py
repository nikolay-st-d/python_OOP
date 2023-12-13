class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget > 0 and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_total = sum(worker.salary for worker in self.workers)
        if self.__budget >= salaries_total:
            self.__budget -= salaries_total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_animals_expenses = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= all_animals_expenses:
            self.__budget -= all_animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        for curr_animal in self.animals:
            animal_kind = curr_animal.__class__.__name__
            if animal_kind not in animals_dict.keys():
                animals_dict[animal_kind] = []
            animals_dict[animal_kind].append(repr(curr_animal))
        result = [f"You have {len(self.animals)} animals"]
        for name, animals in animals_dict.items():
            result.append(f'----- {len(animals)} {name}s:')
            for el in animals:
                result.append(el)
        return '\n'.join(result)

    def workers_status(self):
        workers_dict = {'Keeper': [], 'Caretaker': [], 'Vet': []}
        for curr_worker in self.workers:
            worker_position = curr_worker.__class__.__name__
            if worker_position not in workers_dict.keys():
                workers_dict[worker_position] = []
            workers_dict[worker_position].append(repr(curr_worker))
        result = [f"You have {len(self.workers)} workers"]
        for name, workers in workers_dict.items():
            result.append(f'----- {len(workers)} {name}s:')
            for el in workers:
                result.append(el)
        return '\n'.join(result)

