#Student Identity
LAST_NAME = "Velasco"
STUDENT_ID = "TUPM-26-1934"

#dERIVE COMPUTATIONAL PARAMETERS
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

#ENCAPSULATE STATE INTO A DICTIONARY (ASSOCIATIVE MAP)
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

#DISPLAY SYSTEM STATE
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")

#Initialize a list using the system configuration
base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]

print(f"Initial Sequence: {number_sequence}")

#Append a new value to the sequence
number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
print(f"After Extend: {number_sequence}")

#Count occurences of the base value
base_count = number_sequence.count(base_val)
print(f"Occurences of {base_val}: {base_count}")

#Sort the sequence in ascending order
number_sequence.sort()
print(f"Sorted Sequence: {number_sequence}")
