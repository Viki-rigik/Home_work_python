class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       """Встановлює початкове значення лічильника."""
       self.current = start

   def set_max(self, max_max):
       """Встановлює максимальне значення лічильника."""
       self.max_value = max_max

   def set_min(self, min_min):
       """Встановлює мінімальне значення лічильника."""
       self.min_value = min_min

   def step_up(self):
       """Збільшує значення лічильника на 1."""
       if self.current >= self.max_value:  # Якщо досягли максимуму
           raise ValueError("Досягнуто максимуму")
       self.current += 1

   def step_down(self):
       """Зменшує значення лічильника на 1."""
       if self.current <= self.min_value:  # Якщо досягли мінімуму
           raise ValueError("Досягнуто мінімуму")
       self.current -= 1

   def get_current(self):
       """Повертає поточне значення лічильника."""
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Досягнуто максимуму
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Досягнуто мінімуму
assert counter.get_current() == 7, 'Test4'
