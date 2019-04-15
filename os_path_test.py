import os

os.chdir(' write dir path ')

for dirpath, dirname, filename in os.walk(' write dir path '):
    print('current path is ', dirpath)
    print('current dirname is ', dirname)
    print('current filename is ', filename)


file_path = os.path.join(os.environ.get(' HOME (where make the file)', ' file name '))

with open(file_path, mode='w') as f:
    f.write('sfsadsadsa')
