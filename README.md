# Notes

## String formatting

https://realpython.com/python-string-formatting/

1. Template library
2. then string interpolation
3. then str.format


## Initialize m x n array

Using list comprehension
```python
[[0] * n for _ in range(m)]
```


## Enumerate

https://stackoverflow.com/questions/24150762/pythonic-range-vs-enumerate-in-python-for-loop

2nd position argument is the start enumeration but it does not slice the list

```python
for idx, val in enumerate(a, 0):
    print idx, val
```

## Range

Use if you need list to be sliced

`range(start, stop, step)`

Stop arg is non-inclusive

Use `.reversed()` to iterate backwards

```python
arr = [1, 2, 3, 4, 5]
for idx in reversed(range(len(arr))):
    print(f'reversed {idx}: {arr[idx]}')

for idx in range(len(arr) - 1, -1, -1):
    print(f'step back {idx}: {arr[idx]}')

for idx, val in reversed(list(enumerate(arr))):
    print(f'enumerate {idx}: {val}')
```

Above produces the same result
- You need to use list for enumerate
- You need to subtract 1 from the stop value since stop is non-inclusive
- reversed + range seems to be cleanest


## Difference between str.find and str.index
Use find since index returns an exception when not found

https://stackoverflow.com/questions/22190064/difference-between-find-and-index

`.find(value, start, end)`

## Strings

### Determine if string is alphanumeric
`str.isalnum()`

### str.split(' ') must contain a character. Otherwise use list(str)


## Testing

### Asserting list equality
`assertListEqual`
`assertCountEqual` for unordered lists

## Sorting

`nums.sort()` will mutate
`sorted(nums)` will return a new list

## Sets

`.remove` will throw exception if doesn't exist
`.discard` will remove from set regardless if in set

### Cannot add list to sets. Use tuples. Coerce list to tuple by using
`tuple([1, 2, 3])`

## Dicts

### Merge dict by
`dict3 = {**dict1, **dict2}`

## Importing

Not sure if this is correct. Added `PYTHONPATH=.` in profile. Then you can use absolute imports from the file.

`from leet.data_structures.list_node import ListNode`

## Functions

You can pass lists or tuples into functions by setting the variable and using *

```python
args = (1, 2, 3)

my_func(*args)
```
