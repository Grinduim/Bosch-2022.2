import os
import glob
import time
import shutil
from threading import Thread


class ErrorPastNotFound(Exception):
    def __init__(self, directory):
        self.directory = directory
        self.mensage = f"Caminho '{self.directory}' não encontrado!"
        super().__init__(self.mensage)


class FolderMonitor:
    def __init__(self, path_folder, dst_folder):
        self.path_folder = path_folder
        self._dst_folder = dst_folder

    def start_monitor(self):
        print('Monitorando... ')
        while True:
            for file in os.listdir(self.path_folder):
                shutil.move(f'{self.path_folder}\\{file}', f'{self.dst_folder}\\{file}')

    @property
    def dst_folder(self):
        return self._dst_folder

    @dst_folder.setter
    def dst_folder(self, new_path):
        if not os.path.isdir(new_path):
            raise FolderDoesNotExist("Caminho da pasta não existe", new_path)
        self._dst_folder = new_path


def _set_src_folder():
    folder = ''
    try:
        folder = input('Qual Pasta você quer monitorar?')
        if os.path.exists(folder):
            return folder
        else:
            raise ErrorPastNotFound(folder)
    except ErrorPastNotFound as e:
        print(e)
        op = int(input("[1] - Tentar Novamente\n[2] - Criar Pasta\n R:"))
        if op == 1:
            folder = _set_src_folder()
        else:
            os.mkdir(folder)
    return folder


def _set_dst_folder():
    folder = ''
    try:
        folder = input('Qual a pasta de destino?')
        if os.path.exists(folder):
            return folder
        else:
            raise ErrorPastNotFound(folder)
    except ErrorPastNotFound as e:
        print(e)
        op = int(input("[1] - Tentar Novamente\n[2] - Criar Pasta\n R:"))
        if op == 1:
            folder = _set_dst_folder()
        else:
            os.mkdir(folder)
    return folder
    pass


def main():
    src = _set_src_folder()
    dst = _set_dst_folder()
    folder_monitor = FolderMonitor(src, dst)

    t1 = Thread(target=folder_monitor.start_monitor)
    t1.daemon = True
    t1.start()

    while True:
        res = int(input('\n\nDigite 1 para sair: '))
        if res == 1:
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
