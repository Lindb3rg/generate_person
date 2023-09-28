from typing import Iterable
from models import Person










def search_person_by_name(collection_of_persons: Iterable[Person], name:str) -> Person or None:
    return search(collection_of_persons, attribute_name="name",search_term=name)

def search_person_by_job_title(collection_of_persons: Iterable[Person], job_title:str) -> Person or None:
    return search(collection_of_persons, attribute_name="job_title",search_term=job_title)

def search_person_by_city(collection_of_persons: Iterable[Person], city:str) -> Person or None:
    return search(collection_of_persons, attribute_name="city",search_term=city)

def search_person_by_age_span(collection_of_persons: Iterable[Person], age_span:tuple) -> Person or None:
    return search(collection_of_persons, attribute_name="age_span",search_term=age_span)



def search(collection_of_persons: Iterable[Person],
           attribute_name:str,
           search_term:any) -> Person or None:
    
    output = []

    if attribute_name == "age_span":

        for person in collection_of_persons:
            if person.age >= search_term[0] and person.age <= search_term[1]:
                output.append(person)

    else:
        search_term = search_term.lower()

        for person in collection_of_persons:
            attribute_value = getattr(person, attribute_name).lower()
        
            if attribute_value in search_term or search_term in attribute_value:
                output.append(person)
    
    return output