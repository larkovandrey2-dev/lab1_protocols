import unittest
import json
import os

from src.protocol import Task, TaskProtocol
from src.sources import GeneratorSource, FileSource, APISource


class TestTaskSystem(unittest.TestCase):

    def test_generator_creates_correct_amount(self):
        count = 10
        source = GeneratorSource(count)
        tasks = source.get_tasks()

        self.assertEqual(len(tasks), count)
        self.assertIsInstance(tasks[0], Task)
        self.assertEqual(tasks[0].id, 1)

    def setUp(self):
        self.test_file = "test_tasks.json"
        data = [
            {"id": 99, "payload": {"test": "data"}},
            {"id": 100, "payload": {"test": "data2"}}
        ]
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_source_reads_correctly(self):
        source = FileSource(self.test_file)
        tasks = source.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, 99)
        self.assertEqual(tasks[0].payload["test"], "data")

    def test_file_source_missing_file(self):
        source = FileSource("non_existent_file.json")
        with self.assertRaises(FileNotFoundError):
            source.get_tasks()

    def test_api_source_init(self):
        source = APISource("http://fake.url")
        tasks = source.get_tasks()
        self.assertIsInstance(tasks, list)
        self.assertTrue(len(tasks) > 0)

    def test_protocol_compliance(self):
        gen = GeneratorSource()
        file_src = FileSource(self.test_file)
        api_src = APISource()
        self.assertTrue(isinstance(gen, TaskProtocol))
        self.assertTrue(isinstance(file_src, TaskProtocol))
        self.assertTrue(isinstance(api_src, TaskProtocol))

    def test_protocol_fail(self):
        class NotASource:
            def hello(self): pass

        obj = NotASource()
        self.assertFalse(isinstance(obj, TaskProtocol))


if __name__ == '__main__':
    unittest.main()
