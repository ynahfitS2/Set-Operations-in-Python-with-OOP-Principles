from abc import ABC, abstractmethod

class SetOperation(ABC):
    def __init__(self, set_a, set_b):
        self._set_a = set_a
        self._set_b = set_b
    
    @abstractmethod
    def apply(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

    def get_sets(self):
        return self._set_a, self._set_b
    
    def set_sets(self, set_a, set_b):
        self._set_a = set_a
        self._set_b = set_b
    
class SubsetOperation(SetOperation):
    def apply(self):
        return self._set_a.issubset(self._set_b) 

    def description(self):
        return "\nSUBSET\nA 'subset' is a set whose elements are also in another set. \nSymbol: ⊆ \n\nChecking if set A is a subset of set B..."

class UnionOperation(SetOperation):
    def apply(self):
        return self._set_a.union(self._set_b)

    def description(self):
        return "\nUNION\nThe union of two sets is the set containing all the distinct elements from both sets. \nSymbol: ∪ \n\nThe union of set A and set B is..."

class IntersectionOperation(SetOperation):
    def apply(self):
        return self._set_a.intersection(self._set_b)

    def description(self):
        return "\nINTERSECTION\nThe intersection of sets A and B is the set containing all elements that are present in both A and B. \nSymbol: ∩ \n\nThe intersection of set A and set B is..."

class SymmetricDifferenceOperation(SetOperation):
    def apply(self):
        return set.symmetric_difference(self._set_a, self._set_b)

    def description(self):
        return "\nSYMMETRIC DIFFERENCE\nThe symmetric difference is the set of elements that are in A or B, but not in both. \nSymbol: Δ \n\nThe symmetric difference of set A and set B is..."
    
def read_set(set_name):
    set_length = int(input(f"Enter the number of elements in Set {set_name}: "))
    new_set = set()
    for i in range(set_length):
        element = input(f"Enter element {i + 1} for Set {set_name}: ")
        new_set.add(element)
    return new_set
    
def main():
    set_a = read_set("A")
    set_b = read_set("B")
    
    operations = {
        "1": SubsetOperation(set_a, set_b),
        "2": UnionOperation(set_a, set_b),
        "3": IntersectionOperation(set_a, set_b),
        "4": SymmetricDifferenceOperation(set_a, set_b),
    }
    
    while True:
        print("____________________________________")
        print("LEARNING SET OPERATIONS\n")
        print("\nChoose an operation:")
        print("1. Subset")
        print("2. Union")
        print("3. Intersection")
        print("4. Symmetric Difference")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == "5":
            print("\nExiting Program... \nI hope you learn something. Happy learning!")
            break

        operation = operations.get(choice)
        
        if operation:
            print(f"\nDescription: {operation.description()}")
            set_a, set_b = operation.get_sets()
            print(f"\nSet A: {set_a}")
            print(f"Set B: {set_b}")
            result = operation.apply()
            print(f"\nResult: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Special thanks to:
# Jenny's Lectures CS IT (YouTube) for her OPP principles tutorials
# W3schools (for Set Operations and 00P principles)
# GeeksfoGeeks (00P principles in python)
