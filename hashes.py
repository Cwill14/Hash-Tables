import hashlib

key = b"line_1"

print(f"key: {key}")
# print(f"hashlib.sha256(key): {hashlib.sha256(key)}")
# print(f"hashlib.sha256(key).hexdigest(): {hashlib.sha256(key).hexdigest()}")

sha256key = hashlib.sha256(key).hexdigest()

def djb2(key):
    # start from an arbitrarily large prime number
    hash_value = 5381

    # bit-shift and sum value for each character

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value

print(f"djb2(key): {djb2(key)}")
print(f"sha256key: {sha256key}")
print(f"djb2(key) % 10: {djb2(key) % 10}")
# print(f"sha256key % 10: {sha256key % 10}")