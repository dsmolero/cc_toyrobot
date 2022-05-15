import sys
from core.runners.interactive import interactive_runner


if __name__ == '__main__':
    print(f'sys.argv: {sys.argv}')
    interactive_runner()
