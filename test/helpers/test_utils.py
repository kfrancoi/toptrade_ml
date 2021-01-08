import unittest

from src.helpers.utils import one_hot_to_id, one_hots_to_ids, recursive_merge


class ControllerChecker(unittest.TestCase):
    def test_one_hot_to_id(self):
        vector = [0, 0, 1, 0, 0]
        vector_id = one_hot_to_id(vector)

        self.assertEqual(vector_id, 2)

    def test_one_hots_to_ids(self):
        vectors = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]

        vector_ids = one_hots_to_ids(vectors)

        self.assertEqual(vector_ids[0], 1)
        self.assertEqual(vector_ids[1], 2)
        self.assertEqual(vector_ids[2], 3)
        self.assertEqual(vector_ids[3], 4)

    def test_recursive_merge(self):
        initial = {
            "a1": "hello",
            "a2": "world",
            "b": {
                "c1": "hello",
                "c2": "world"
            }
        }

        update = {
            "a2": "people",
            "b": {
                "c1": "hi",
                "c3": "!"
            },
            "d": "End"
        }

        updated_dict = recursive_merge(initial, update)

        self.assertEqual(updated_dict, {
            "a1": "hello",
            "a2": "people",
            "b": {
                "c1": "hi",
                "c2": "world",
                "c3": "!"
            },
            "d": "End"
        })
