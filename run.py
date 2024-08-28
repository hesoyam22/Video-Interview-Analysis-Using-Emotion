import multiprocessing
from subprocess import Popen,PIPE
import subprocess
def worker(file):
    print('# your subprocess code')
    subprocess.Popen(['python', 'video_interview.py'])
    subprocess.Popen(['python', 'quizstar.py'])


if __name__ == '__main__':
    files = ["video_interview.py"]
    print("loaded")
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()