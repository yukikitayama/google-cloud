import argparse


def main(arg1, arg2):
    print(f'In main(), arg1: {arg1}, arg2: {arg2}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=str, help='arg1 type is string')
    parser.add_argument('arg2', type=int, help='arg2 type is integer')
    args = parser.parse_args()
    arg1 = args.arg1
    arg2 = args.arg2
    print(f'Before main(), arg1: {arg1}, arg2: {arg2}')
    main(arg1=arg1, arg2=arg2)
