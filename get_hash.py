import hashlib

def calculate_file_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()
    

def check_file_for_changes(file_path, stored_hash):
    current_hash = calculate_file_hash(file_path)
    return current_hash == stored_hash


# file_path = '/bitnami/wordpress/wp-content/uploads/Book1.xlsx'  
# stored_hash = '64ba32406ce3b1ea15e81e0f5519896da073fe6129e98b833bf9c121b88b7064'

# initial_hash = calculate_file_hash(file_path)
# if not stored_hash:
#     stored_hash = initial_hash
#     # You can store the initial_hash in a variable or save it to a database/file


# has_changed = not check_file_for_changes(file_path, stored_hash)

# if has_changed:
#     print("The file has been changed.")
#     # Do something when the file has changed (e.g., notify or process it)
# else:
#     print("The file has not been changed.")
