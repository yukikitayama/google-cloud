import sys
import pkg_resources


def main():
    print(f'Python version: {sys.version}')
    print(f'Installed packages:')
    # key is package name, version is package version number
    for package in sorted([f'{i.key}=={i.version}' for i in pkg_resources.working_set]):
        print(package)


if __name__ == '__main__':
    main()
