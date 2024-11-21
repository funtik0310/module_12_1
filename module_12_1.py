import runner
import unittest

class Runnertest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner('Леша')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('Егор')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = runner.Runner('Илья')
        runner_4 = runner.Runner('Андрей')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == '__main__':
    unittest.main()

