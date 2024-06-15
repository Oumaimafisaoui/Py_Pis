
def myFunc(x):
  if x < 18:
    return False
  else:
    return True

def ft_filter(func, iterable):
    return iter([x for x in iterable if func(x)])

def main():
    iterable =  [5, 12, 17, 18, 24, 32]
    mine = ft_filter(myFunc, iterable)
    other = filter(myFunc, iterable)
    print(mine)
    print(other)


if __name__ == "__main__":
    main()