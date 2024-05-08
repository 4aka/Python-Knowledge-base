import subprocess
import globalVariables as vars

file_path = vars.PROJECT_DIR + "test.bat"


def run_batch(filePath):
    p = subprocess.Popen(filePath, shell=True, stdout=subprocess.PIPE)

    stdout, stderr = p.communicate()
    print(p.returncode)


if __name__ == '__main__':
    run_batch(file_path)
