from barnum import gen_data
import random
from dataclasses import dataclass
from typing import Iterator,Iterable

def write_random_persons_to_file(filepath,n_persons):
    with open(filepath,"a", encoding="utf-8") as file:
        for i in range(n_persons):
            name = " ".join(gen_data.create_name())
            job_title = gen_data.create_job_title()
            city = gen_data.create_city_state_zip()[1]
            age = random.randint(18,99)
            file.write(f"{name};{job_title};{city};{age}\n")



@dataclass
class Person:
    name: str
    job_title: str
    city: str
    age: str



def read_persons_from_file(filepath, batch_size=10)->Iterator[list[Person]]:
    with open(filepath, "r", encoding="utf-8") as file:
        persons = []
        for i, line in enumerate(file, start=1):
            
            name, job_title,city,age = line.split(";")
            person = Person(name,job_title,city,age)

            
            persons.append(person)
            if i % batch_size == 0:
                yield persons
                persons.clear()



def search_person_by_name(collection_of_persons: Iterable[Person], name:str) -> Person or None:
    output = []

    name = name.lower()
    for person in collection_of_persons:
        if person.name.lower() in name or name in person.name.lower():
            output.append(person)
    
    return output









if __name__=="__main__":
    filepath = "persons.txt"
    
    write_random_persons_to_file(filepath)
    person_generator = read_persons_from_file(filepath)
    while True:
        try:
            batch_of_persons = next(person_generator)
        except StopIteration:
            print("No more persons in file")

        name_to_search_for = input("Enter name to search for: ")
        search_result = search_person_by_name(collection_of_persons=batch_of_persons,name=name_to_search_for)
        
        if not search_result:
            continue
            
        print(f"Search result: {search_result}")

        if input("Hit enter to continue, or 'q' to exit") == "q":
            exit()
        


    
