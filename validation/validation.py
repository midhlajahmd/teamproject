def validate_name(name: str) -> bool:
    if not name or not name.isalpha():
        print("Invalid name. Name must only contain alphabets.")
        return False
    return True

def validate_age(age: int) -> bool:
    if not (18 <= age <= 65):
        print("Invalid age. Age must be between 18 and 65.")
        return False
    return True
