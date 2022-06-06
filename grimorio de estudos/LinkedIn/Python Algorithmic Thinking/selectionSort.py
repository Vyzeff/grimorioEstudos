
from tempfile import tempdir


def selection_sort(xs):
    for index_start in range(0, len(xs) - 1):
        min_index = index_start
        for x in range(index_start + 1, len(xs)):
            if xs[x] < xs[min_index]:
                min_index = x
                
        temp = xs[index_start]
        xs[index_start] = xs[min_index]
        xs[min_index] = temp
        print(xs)


xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))