from main import write_random_persons_to_file, read_persons_from_file



if __name__ == "__main__":
    filepath = "persons.txt"
    
    write_random_persons_to_file(filepath)
    person_generator = read_persons_from_file(filepath)
    print("1. Search by name",
          "2. Search by job title",
          "3. Search by city",
          "4. Add new persons to list", sep="\n")
    while True:

        try:
            batch_of_persons = next(person_generator)
        except StopIteration:
            print("No more persons in file")
            break

        batch_of_persons.sort(key=lambda x: x.age)

        for i in batch_of_persons:
            print(i)
