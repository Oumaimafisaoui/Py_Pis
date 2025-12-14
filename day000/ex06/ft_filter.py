

def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    print(ft_filter(lambda n: n % 2 == 0, [1,2,4,5]))
    print(filter(lambda n: n % 2 == 0, [1,2,4,5]))
if __name__ == "__main__":
    main()