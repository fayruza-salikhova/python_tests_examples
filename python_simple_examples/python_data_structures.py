# 1. List (mutable, ordered collection)
my_list = [1, 2, 3]  # create a list with 3 elements

my_list.append(4)      # add element 4 to the end -> [1, 2, 3, 4]
my_list.insert(1, 10)  # insert 10 at index 1 -> [1, 10, 2, 3, 4]
my_list[2] = 20        # change element at index 2 -> [1, 10, 20, 3, 4]

my_list.remove(3)      # remove first occurrence of value 3 -> [1, 10, 20, 4]
removed = my_list.pop(1)  # remove element at index 1 and return it (10)

length = len(my_list)  # get the number of elements in the list

if 20 in my_list:     # check if 20 is in the list
    print("20 is in list")

for item in my_list:  # iterate over list elements
    print(item)


# 2. Tuple (immutable, ordered collection)
my_tuple = (1, 2, 3)   # create a tuple

print(my_tuple[1])      # access element by index, prints 2
print(len(my_tuple))    # length of tuple

if 2 in my_tuple:       # check membership
    print("2 is in tuple")

# Tuples cannot be changed:
# my_tuple[1] = 5  # will raise TypeError


# 3. Set (mutable, unordered collection of unique elements)
my_set = {1, 2, 3}    # create a set

my_set.add(4)         # add element 4 -> {1, 2, 3, 4}
my_set.remove(2)      # remove element 2, error if not present
my_set.discard(5)     # remove element 5 if exists, no error if not

if 3 in my_set:       # check membership
    print("3 is in set")

print(len(my_set))    # size of the set

for elem in my_set:   # iterate over elements (order not guaranteed)
    print(elem)


# 4. Dictionary (mutable key:value store)
my_dict = {"username": "testuser", "password": "pass123"}  # create dict

my_dict["email"] = "test@example.com"  # add or update key 'email'
my_dict["password"] = "newpass"         # update existing key

print(my_dict["username"])               # access by key
print(my_dict.get("phone", "No phone")) # safe get with default

my_dict.pop("password")                  # remove key and get value

print(len(my_dict))                      # count of keys

if "email" in my_dict:                   # check if key exists
    print("Email key exists")

for key in my_dict:                      # iterate keys
    print(key, my_dict[key])

for key, value in my_dict.items():      # iterate key-value pairs
    print(key, value)


# 5. String (immutable text)
my_str = "hello world"

print(len(my_str))       # string length
print(my_str[0])         # first character 'h'

if "world" in my_str:    # check substring presence
    print("'world' is in string")

new_str = my_str.replace("world", "QA")  # create new string with replacement
print(new_str)          # prints "hello QA"

words = my_str.split()  # split string into list of words ['hello', 'world']

print(my_str.upper())   # convert to uppercase
print(my_str.lower())   # convert to lowercase


# Examples of usage in tests:

# Assert list length from API response
response = {"items": [1, 2, 3, 4]}
assert len(response["items"]) == 4

# Assert uniqueness using set
items = [1, 2, 2, 3]
unique_items = set(items)
assert len(unique_items) == 3

# Assert dict contains key and expected value
user = {"username": "testuser", "role": "admin"}
assert "username" in user
assert user["role"] == "admin"

# Update dict in test and assert new value
user["status"] = "active"
assert user.get("status") == "active"
