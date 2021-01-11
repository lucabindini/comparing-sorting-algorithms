import sys
import matplotlib.pyplot as plt
import random
from timeit import default_timer as timer

sys.setrecursionlimit(100000)


def random_list(n):
    ls = list(range(n))
    random.shuffle(ls)
    return ls


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def insertion_sort_time(a):
    start = timer()
    insertion_sort(a)
    end = timer()
    time = end - start
    print("Tempo di esecuzione di Insertion-Sort:", time)
    return time


def quicksort_time(a, n):
    start = timer()
    quicksort(a, 0, n - 1)
    end = timer()
    time = end - start
    print("Tempo di esecuzione di Quicksort:", time)
    return time


def average(values):
    sum = 0
    for j in range(0, len(values)):
        sum += values[j]
    return sum / len(values)


def main():
    MAXDIM = 5000
    num_prove = 10
    step = 50

    dim = 0
    size = []
    insertion_times = []
    quick_times = []
    while dim <= MAXDIM:
        print("Dimensione array:", dim)
        size.append(dim)
        insertion_single_time = []
        quick_single_time = []
        for j in range(0, num_prove):
            array = random_list(dim)
            array_copy = array[:]
            print("Numero Prova:", j + 1)
            print("Array:", array)
            insertion_single_time.append(insertion_sort_time(array))
            quick_single_time.append(quicksort_time(array_copy, dim))
        avg_insertion = average(insertion_single_time)
        avg_quicksort = average(quick_single_time)
        insertion_times.append(avg_insertion)
        quick_times.append(avg_quicksort)
        print("Tempo medio Insertion-Sort:", avg_insertion)
        print("Tempo medio Quicksort:", avg_quicksort)
        dim += step
    plt.title('Caso medio di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.savefig('Caso medio di Insertion-Sort')
    plt.clf()
    plt.title('Caso medio di Quicksort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, quick_times)
    plt.savefig('Caso medio di Quicksort')
    plt.clf()
    plt.title('Confronto nel caso medio')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.plot(size, quick_times)
    plt.legend(['Insertion-Sort', 'Quicksort'])
    plt.savefig('Confronto nel caso medio')
    plt.clf()

    dim = 0
    size = []
    insertion_times = []
    quick_times = []
    while dim <= MAXDIM:
        print("Dimensione:", dim)
        size.append(dim)
        insertion_single_time = []
        quick_single_time = []
        for j in range(0, num_prove):
            array = list(range(dim))
            array_copy = array[:]
            print("Numero Prova:", j + 1)
            print("Array:", array)
            insertion_single_time.append(insertion_sort_time(array))
            quick_single_time.append(quicksort_time(array_copy, dim))
        avg_insertion = average(insertion_single_time)
        avg_quicksort = average(quick_single_time)
        insertion_times.append(avg_insertion)
        quick_times.append(avg_quicksort)
        print("Tempo medio Insertion-Sort:", avg_insertion)
        print("Tempo medio Quicksort", avg_quicksort)
        dim += step
    plt.title('Caso migliore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.savefig('Caso migliore di Insertion-Sort')
    plt.clf()
    plt.title('Quicksort nel caso migliore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, quick_times)
    plt.savefig('Quicksort nel caso migliore di Insertion-Sort')
    plt.clf()
    plt.title('Confronto nel caso migliore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.plot(size, quick_times)
    plt.legend(['Insertion-Sort', 'Quicksort'])
    plt.savefig('Confronto nel caso migliore di Insertion-Sort')
    plt.clf()

    dim = 0
    size = []
    insertion_times = []
    quick_times = []
    while dim <= MAXDIM:
        print("Dimensione:", dim)
        size.append(dim)
        insertion_single_time = []
        quick_single_time = []
        for j in range(0, num_prove):
            array = list(reversed(list(range(dim))))
            array_copy = array[:]
            print("Numero Prova:", j + 1)
            print("Array:", array)
            insertion_single_time.append(insertion_sort_time(array))
            quick_single_time.append(quicksort_time(array_copy, dim))
        avg_insertion = average(insertion_single_time)
        avg_quicksort = average(quick_single_time)
        insertion_times.append(avg_insertion)
        quick_times.append(avg_quicksort)
        print("Tempo medio Insertion-Sort:", avg_insertion)
        print("Tempo medio Quicksort", avg_quicksort)
        dim += step
    plt.title('Caso peggiore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.savefig('Caso peggiore di Insertion-Sort')
    plt.clf()
    plt.title('Quicksort nel caso peggiore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, quick_times)
    plt.savefig('Quicksort nel caso peggiore di Insertion-Sort')
    plt.clf()
    plt.title('Confronto nel caso peggiore di Insertion-Sort')
    plt.xlabel('Dimensione')
    plt.ylabel('Tempo di esecuzione')
    plt.plot(size, insertion_times)
    plt.plot(size, quick_times)
    plt.legend(['Insertion-Sort', 'Quicksort'])
    plt.savefig('Confronto nel caso peggiore di Insertion-Sort')
    plt.clf()


if __name__ == '__main__':
    main()
