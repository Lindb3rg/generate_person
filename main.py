from barnum import gen_data
import random
from models import Person
from typing import Iterator,Iterable
from search_functions import search_person_by_name,search_person_by_job_title, search_person_by_city,search_person_by_age_span

def write_random_persons_to_file(filepath,n_persons=0):
    with open(filepath,"a", encoding="utf-8") as file:
        for i in range(n_persons):
            name = " ".join(gen_data.create_name())
            job_title = gen_data.create_job_title()
            city = gen_data.create_city_state_zip()[1]
            age = random.randint(18,99)
            file.write(f"{name};{job_title};{city};{age}\n")







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


if __name__=="__main__":

    filepath = "persons.txt"
    
    write_random_persons_to_file(filepath)
    person_generator = read_persons_from_file(filepath)
    print("1. Search by name",
          "2. Search by job title",
          "3. Search by city",
          "4. Search by age span", sep="\n")
    

    while True:

        try:
            batch_of_persons = next(person_generator)
        except StopIteration:
            print("No more persons in file")
            break

        if input("Enter: ") == "1":
            name_to_search_for = input("Enter name to search for: ")
            search_result = search_person_by_name(collection_of_persons=batch_of_persons,name=name_to_search_for)
        
        elif input("Enter: ") == "2":
            job_title_to_search_for = input("Enter job title to search for: ")
            search_result = search_person_by_job_title(collection_of_persons=batch_of_persons,job_title=job_title_to_search_for)
        

        elif input("Enter: ") == "3":
            city_to_search_for = input("Enter city to search for: ")
            search_result = search_person_by_city(collection_of_persons=batch_of_persons,city=city_to_search_for)
        
        elif input("Enter: ") == "4":
            age_span_to_search_for = input("Enter age span to search for (separate by space):").split(" ")
            search_result = search_person_by_age_span(collection_of_persons=batch_of_persons,age_span=age_span_to_search_for)




        if not search_result:
            continue
            
        print(f"*** Person found ***")
        print("Search result: ", *search_result, sep="\n\t")
        
        if input("Hit enter to continue, or 'q' to exit") == "q":
            exit()
        


    
