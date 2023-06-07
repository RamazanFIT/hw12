from typing import List, Any, Dict, Set, Generator

"""
Exercise-1: List Comprehension to Squares
Write a function "squares(n: int) -> List[int]" that uses a list comprehension to return a list of the squares of all numbers up to 'n'.

Example:
squares(5) -> [0, 1, 4, 9, 16]
"""
def squares(n: int):
    # pass 
    return [x ** 2 for x in range(n)]

# print(squares(5))
"""
Exercise-2: Set Comprehension with Filtering
Write a function "unique_squares(numbers: List[int]) -> Set[int]" that uses a set comprehension to return the squares of the unique numbers from the input list.

Example:
unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) -> {1, 4, 9, 16}
"""
def unique_squares(numbers: List[int]) -> Set[int]:
    # pass 
    return {x ** 2 for x in numbers}
# print(unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
"""
Exercise-3: Dictionary Comprehension to Count Characters
Write a function "char_counts(text: str) -> Dict[str, int]" that uses a dictionary comprehension to count the occurrence of each character in a string.

Example:
char_counts("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
def char_counts(text: str) -> Dict[str, int]:
    # pass 
    some_dict = {}
    {key: 1 if key not in some_dict and not some_dict.update({key: 1}) else some_dict[key] + 1 if some_dict.update({key:some_dict[key] + 1}) else 1 for key in text}
    return some_dict
# print(char_counts('asdsadDASDFASCSAASAS'))
# dict_1 = {}
# if True and not dict_1.update({"roma":"krassava"}):
#     pass
# print(dict_1)
# if None:
#     print("yeah")
"""
Exercise-4: Nested List Comprehension
Write a function "flatten(nested_list: List[List[Any]]) -> List[Any]" that uses a nested list comprehension to flatten a list of lists.

Example:
flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def flatten(nested_list: List[List[Any]]) -> List[Any]:
    # pass 
    list_1 = []
    [list_1.extend(x) for x in nested_list]
    return list_1
# print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
Exercise-5: Generator Expression to Yield Squares
Write a function "squares_gen(n: int) -> Generator[int]" that uses a generator expression to yield the squares of all numbers up to 'n'.

Example:
list(squares_gen(5)) -> [0, 1, 4, 9, 16]
"""
def squares_gen(n: int) -> Generator[int, None, None]:
    # pass
    # yield [x ** 2 for x in range(n)] 
    # for x in range(n):
    #     yield x ** 2
    return [x ** 2 for x in range(n)]
# print(squares_gen(1001))
# print(squares_gen(5))
# gen = *squares_gen(5)
"""
Exercise-6: Set Comprehension to Find Odd Squares
Write a function "odd_squares(n: int) -> Set[int]" that uses a set comprehension to find the squares of all odd numbers up to 'n'.

Example:
odd_squares(10) -> {1, 9, 25, 49, 81}
"""
def odd_squares(n: int) -> set[int]:
    # pass 
    # return {x ** 2 for x in range(1, n, 2)}
    return {x ** 2 if x % 2 != 0 else 1 for x in range(1, n + 1)}

# print(odd_squares(10))

"""
Exercise-7: Dictionary Comprehension to Map Indices
Write a function "index_map(text: str) -> Dict[str, int]" that uses a dictionary comprehension to map each character in a string to its index.

Example:
index_map("hello") -> {'h': 0, 'e': 1, 'l': 3, 'o': 4}
"""
def index_map(text: str) -> dict[str, int]:
    # pass 
    return {text[x] : x for x in range(len(text))}
# print(index_map("hello"))
# print(index_map("a"*1000 + "b"*1000))
# print("a"*1000 + "b"*1000)
"""
Exercise-8: Nested Set Comprehension
Write a function "unique_values(nested_list: List[List[Any]]) -> Set[Any]" that uses a nested set comprehension to find the unique values in a nested list.

Example:
unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {1, 2, 3, 4, 5}
"""
def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    # pass 
    some_set = set()
    {some_set.update(x) for x in nested_list}
    return some_set
# print(unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
"""
Exercise-9: Fibonacci Sequence with Generators
Write a function "fibonacci_gen(n: int) -> Generator[int]" that uses a generator to yield the Fibonacci sequence up to the nth term.

Example:
list(fibonacci_gen(10)) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
def fibonacci_gen(n: int) -> Generator[int, None, None]:
    # pass 
    x = 0
    y = 1
    for i in range(n):
        yield x
        x, y = y, x + y
   
# print(list(fibonacci_gen(100)))
"""
Exercise-10: Dictionary Comprehension to Invert a Dictionary
Write a function "invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]" that uses a dictionary comprehension to invert a dictionary.

Example:
invert_dict({'a': 1, 'b': 2, 'c': 3}) -> {1: 'a', 2: 'b', 3: 'c'}
"""
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    # pass 
    return {x : y for y, x in d.items()}
# print(invert_dict({'a': 1, 'b': 2, 'c': 3}))
"""
Exercise-11: Prime Numbers with List Comprehension
Write a function "primes(n: int) -> List[int]" that uses a list comprehension to return a list of all prime numbers up to 'n'.

Example:
primes(10) -> [2, 3, 5, 7]
"""
def primes(n: int) -> List[int]:
    # pass 
    some_bolean = [0] * (n + 1)
    primes = []
    for x in range(2, n + 1):
        if not some_bolean[x]:
            primes.append(x)
        for y in range(x * x, n + 1, x):
            some_bolean[y] = True
    return primes
# print(primes(100))
"""
Exercise-12: Set Comprehension to Intersect Sets
Write a function "intersection(sets: List[Set[Any]]) -> Set[Any]" that uses a set comprehension to return the intersection of a list of sets.

Example:
intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]) -> {3}
"""
def intersection(sets: List[Set[Any]]) -> Set[Any]:
    # pass 
    ans = sets[0]
    {ans.intersection_update(x) for x in sets}
    return ans
# print(intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]))
"""
Exercise-13: Generator Expression to Yield Factorials
Write a function "factorials_gen(n: int) -> Generator[int]" that uses a generator expression to yield the factorials of all numbers up to 'n'.

Example:
list(factorials_gen(5)) -> [1, 2, 6, 24, 120]
"""
def factorials_gen(n: int) -> Generator[int, None, None]:
    # pass 
    k = 1
    for x in range(1, n + 1):
        yield k
        k *= x
        
# print(list(factorials_gen(5)))
"""
Exercise-14: Dictionary Comprehension to Map Strings to Lengths
Write a function "str_lengths(strings: List[str]) -> Dict[str, int]" that uses a dictionary comprehension to map strings to their lengths.

Example:
str_lengths(['hello', 'world', 'python']) -> {'hello': 5, 'world': 5, 'python': 6}
"""
def str_lengths(strings: List[str]) -> Dict[str, int]:
    # pass 
    return {x : len(x) for x in strings}
# print(str_lengths(['hello', 'world', 'python']))
"""
Exercise-15: Nested List Comprehension to Transpose Matrix
Write a function "transpose(matrix: List[List[Any]]) -> List[List[Any]]" that uses a nested list comprehension to transpose a matrix.

Example:
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    # pass 
    list_1 = [[] for x in range(len(matrix[0]))]
    [list_1[x].append(y[x]) for y in matrix for x in range(len(y))]
    return list_1
# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
Exercise-16: Generator to Yield Reversed List
Write a function "reverse_gen(lst: List[Any]) -> Generator[Any]" that returns a generator which yields elements from the list in reverse order.

Example:
list(reverse_gen([1, 2, 3, 4, 5])) -> [5, 4, 3, 2, 1]
"""
def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    # pass 
    for x in range(len(lst)):
        yield lst[len(lst) - x - 1]
# print(list(reverse_gen([1, 2, 3, 4, 5])))
"""
Exercise-17: Dictionary Comprehension to Group By Length
Write a function "group_by_length(words: List[str]) -> Dict[int, List[str]]" that uses a dictionary comprehension to group words by their length.

Example:
group_by_length(['hello', 'world', 'python', 'is', 'fun']) -> {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun']}
"""
def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    # pass 
    some_dict_to_ans = {}
    {some_dict_to_ans.update({value: [key]}) if value not in some_dict_to_ans else 1 if some_dict_to_ans[value].append(key) else 1 for key, value in {x : len(x) for x in words}.items()}

    return some_dict_to_ans

# print(group_by_length(['hello', 'world', 'python', 'is', 'fun']))
"""
Exercise-18: Set Comprehension to Find Common Elements
Write a function "common_elements(lists: List[List[Any]]) -> Set[Any]" that uses a set comprehension to find the common elements in a list of lists.

Example:
common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {3}
"""
def common_elements(lists: List[List[Any]]) -> Set[Any]:
    # pass 
    set_1 = set(lists[0])
    {set_1.intersection_update(x) for x in lists}
    return set_1
# print(common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
"""
Exercise-19: Generator Expression to Yield Primes
Write a function "primes_gen(n: int) -> Generator[int]" that uses a generator expression to yield all prime numbers up to 'n'.

Example:
list(primes_gen(10)) -> [2, 3, 5, 7]
"""
def primes_gen(n: int) -> Generator[int, None, None]:
    some_bolean = [0] * (n + 1)
    for x in range(2, n + 1):
        if not some_bolean[x]:   
            yield x
        for y in range(x * x, n + 1, x):
            some_bolean[y] = True
    
# print(list(primes_gen(10)))

"""
Exercise-20: Dictionary Comprehension to Convert List to Dict
Write a function "list_to_dict(lst: List[Any]) -> Dict[int, Any]" that uses a dictionary comprehension to convert a list into a dictionary where the keys are the indices of the list elements.

Example:
list_to_dict(['a', 'b', 'c']) -> {0: 'a', 1: 'b', 2: 'c'}
"""
def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    # pass 
    return {x : lst[x] for x in range(len(lst))}

# print(list_to_dict(['a', 'b', 'c']))