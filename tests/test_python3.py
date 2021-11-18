import unittest
from subprocess import Popen, PIPE

import os
from os import path

class TestPython3(unittest.TestCase):

    def setUp(self):
        if os.environ.get('TEST_PYTHON_EXEC'):
            self.pythonExec = os.environ.get('TEST_PYTHON_EXEC')
        else:
            self.pythonExec = 'python'

    def test_run_99bottles(self):
        pathBFProgam = path.join('bf-programs-samples', '99bottles.b')
        pathBFProgamOuput = path.join('bf-programs-samples', '99bottles.output')
        pathPythonScript =  path.join('src', 'bf-interpreter__python3.py')

        p = Popen([self.pythonExec, pathPythonScript, pathBFProgam], stdout=PIPE)
        stdout, _ = p.communicate()

        with open(pathBFProgamOuput, 'rb') as file:
            contents = file.read()

        self.assertEqual(stdout.replace(b'\r\r\n', b'\r\n'), contents)
    
    def test_run_hello_world(self):
        pathBFProgam = path.join('bf-programs-samples', 'hello-world.b')
        pathBFProgamOuput = path.join('bf-programs-samples', 'hello-world.output')
        pathPythonScript =  path.join('src', 'bf-interpreter__python3.py')

        p = Popen([self.pythonExec, pathPythonScript, pathBFProgam], stdout=PIPE)
        stdout, _ = p.communicate()

        with open(pathBFProgamOuput, 'rb') as file:
            contents = file.read()

        self.assertEqual(stdout.replace(b'\r\n', b'\n'), contents)

if __name__ == '__main__':
    unittest.main()