from itertools import product
import hashlib

def get_hash_string(message: str):
    
    hash_object = hashlib.sha256()
    hash_object.update(message.encode())
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

def append_permutation(initial_message: str, permutation: tuple[str]):
    
    output = initial_message
    
    last_digit = permutation[-1]
    
    for digit in permutation[:-1]:
        output = f"{output}{digit}, "
    output = f"{output}{last_digit}"
    
    return output

def find_message(n: int):

    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    initial_message = "The SHA256 hash for this message starts with : "
    answer = ""
    
    for permutation in list(product(hex_digits, repeat=n)):
        
        complete_message = append_permutation(initial_message, permutation)
        
        complete_message_hash = get_hash_string(complete_message)
        
        if (complete_message_hash[:n] == (''.join(permutation))[:n]):
            answer = complete_message
            break

    # assert : message is a message that predicts the first n hex digits of its sha256 hash
    
    return answer

def main():

    print(find_message(6))
    
main()