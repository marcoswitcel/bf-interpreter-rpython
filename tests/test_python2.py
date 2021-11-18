import unittest
from subprocess import Popen, PIPE

import os
from os import path

TESTE_SKIP = os.environ.get('TEST_PYTHON2_EXEC') == None
MENSAGEM_SKIP = "Para rodas os teste da versão dois é necessário explicitamente informar o caminho do executável"

class TestPython2(unittest.TestCase):

    def setUp(self):
        self.pythonExec = os.environ.get('TEST_PYTHON2_EXEC')

    @unittest.skipIf(TESTE_SKIP, MENSAGEM_SKIP)
    def test_run_99bottles(self):
        pathBFProgam = path.join('bf-programs-samples', '99bottles.b')
        pathBFProgamOuput = path.join('bf-programs-samples', '99bottles.output')
        pathPythonScript =  path.join('src', 'bf-interpreter__python2-rpython.py')

        p = Popen([self.pythonExec, pathPythonScript, pathBFProgam], stdout=PIPE)
        stdout, _ = p.communicate()

        with open(pathBFProgamOuput, 'rb') as file:
            contents = file.read()

        self.assertEqual(stdout.replace(b'\r\r\n', b'\r\n'), contents)
    
    @unittest.skipIf(TESTE_SKIP, MENSAGEM_SKIP)
    def test_run_hello_world(self):
        pathBFProgam = path.join('bf-programs-samples', 'hello-world.b')
        pathBFProgamOuput = path.join('bf-programs-samples', 'hello-world.output')
        pathPythonScript =  path.join('src', 'bf-interpreter__python2-rpython.py')

        p = Popen([self.pythonExec, pathPythonScript, pathBFProgam], stdout=PIPE)
        stdout, _ = p.communicate()

        with open(pathBFProgamOuput, 'rb') as file:
            contents = file.read()

        self.assertEqual(stdout.replace(b'\r\n', b'\n'), contents)

if __name__ == '__main__':
    unittest.main()