import os
from multiprocessing import Pool


def run_flask_process(process):
    print(f'RUN {process}')
    os.system('python {}'.format(process))


def run_django_process(process):
    print(f'RUN {process}')
    os.system(f'python {process} runserver 0.0.0.0:8000')


def run_process(process):
    name, ptype = process
    if ptype == 'flask':
        run_flask_process(name)
    if ptype == 'django':
        run_django_process(name)


FLASK_RUN = 'main.py'
DJANGO_RUN = 'manage.py'
run_files = []
for path, folders, files in os.walk(os.getcwd()):
    if FLASK_RUN in files:
        run_path = os.path.join(path, FLASK_RUN)
        run_files.append((run_path, 'flask'))
    if DJANGO_RUN in files:
        run_path = os.path.join(path, DJANGO_RUN)
        run_files.append((run_path, 'django'))

if __name__ == '__main__':
    pool = Pool(processes=len(run_files))
    pool.map(run_process, run_files)
