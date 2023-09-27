from typing import Iterable
from main import Person




def search_person_by_name(collection_of_persons: Iterable[Person], name:str) -> Person or None:
    return search(collection_of_persons, attribute_name="name",search_term=name)

def search_person_by_job_title(collection_of_persons: Iterable[Person], job_title:str) -> Person or None:
    return search(collection_of_persons, attribute_name="job_title",search_term=job_title)







def search(collection_of_persons: Iterable[Person],
           attribute_name:str,
           search_term:any) -> Person or None:
    
    output = []
    search_term = search_term.lower()

    for person in collection_of_persons:
        attribute_value = getattr(person, attribute_name.lower())
    
        if attribute_value in search_term or search_term in attribute_value:
            output.append(person)
    
    return output


    