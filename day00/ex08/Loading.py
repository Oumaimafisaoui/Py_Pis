"""In this project I created a virtual environment using python3 -m venv myenv """
from time import sleep

def ft_tqdm(lst: range) -> None:
    l = len(lst)
    for current in lst:
        yield current
        bare_length = 89
        counter = int((current / l) * 101)
        filled = int((current / l) * bare_length)
        if (filled == bare_length - 1):
            bare = '=' * filled + '>'
        else:
            bare = '=' * filled + ' ' * (bare_length - filled)
        print(f'\r{counter}%|[{bare}]', end='')
        print(f'| {current + 1}/{l}', end='')
    print()



def main():
    for _ in ft_tqdm(range(300)):
        sleep(0.01)


if __name__ == "__main__":
    main()