import os
import datetime


def _main():
    date = datetime.datetime.now()

    print(date.strftime('Today is %d/%m/%Y %H:%M:%S'))

    print(f"Usuário : {os.getenv('username')}")
    print(f"Domain : {os.getenv('USERDNSDOMAIN')}")
    print(f"Home directory : {os.getenv('HOME')}")

    print(f"Processor Architecture : {os.getenv('PROCESSOR_ARCHITECTURE')}")
    print(f"# of Processors : {os.getenv('NUMBER_OF_PROCESSORS')}")

    print(f"Im running from {os.getcwd()}")
    print("Have a nice Day!")

    os.system("PAUSE")


if __name__ == '__main__':
    _main()
