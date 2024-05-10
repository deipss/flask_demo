import json
import  os
import yaml
if __name__ == '__main__':
    print(__file__)
    relpath = os.path.relpath(__file__)
    print(os.path.split(relpath))
    print(relpath)
    print(os.getcwd())


    path = os.path.join('dir1', 'dir2', 'file.txt')
    print(path)


