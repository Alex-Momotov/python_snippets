from memory_time import memory_time
import random

@memory_time
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

@memory_time
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

@memory_time
def waiting_func(secs):
    import time
    time.sleep(secs)
    return

@memory_time
def iterate_gen():
    people = people_generator(1000000)
    var = 0
    for x in people: var += x['id']
    return var

names = ['John', 'Alisa', 'Stephen', 'Priya', 'Michael', 'Eddie']
majors = ['Maths', 'CompSci', 'Physics', 'Biology', 'Chemistry', 'History']

# Our waiting function.
# waiting_func(2)

# HERE, CREATING LIST TOOK 270 Mb OF MEMORY AND 1.75 SECONDS.
# people = people_list(1000000)

# HERE, CREATING GENERATOR OBJECT TOOK 0.00 SECONDS AND 0.00 Mb OF MEMORY.
# people = people_generator(1000000)

# HERE, CREATING AND ITERATING THROUGH THE GENERATOR TOOK 1.72 SEC (SAME AS LIST) BUT 0.0Mb OF MEMORY.
# num = iterate_gen()

