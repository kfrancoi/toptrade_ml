import collections
import json
import os
from typing import Any

import numpy as np


def create_dir(dir_path: str) -> bool:
    """Create the directory specified by dir_path if not exists.

    Args:
        dir_path: the path to the directory

    Requires:
        dir_path is not None

    Returns:
        a boolean stating if the creation succeded

    """
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return True
    except Exception as err:
        print("Creating directory {} error: {}".format(dir_path, err))
    return False


def load_json(file_path: str) -> Any:
    """Load a json formated object from file_path.

    Args:
        file_path: the path to the file

    Requires:
        filepath is not None and file_path exists

    Returns:
        The loaded object

    """
    with open(file_path) as json_file:
        o_file = json_file.read()
    return json.loads(o_file)


def dump_json(
    data: Any, path: str, sort_keys: bool = False, indent: Any = None
) -> None:
    """Save a datastructure to a json file.

    Args:
        data: the datastructure to be saved
        path: the path to the json file
        sort_keys: should the keys be sorted in the output file
        indent: how to represent indentations ?

    Requires:
        data is JsonSerializable
        path is valid

    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, sort_keys=sort_keys, indent=indent)


def one_hot_to_id(vector: np.array) -> int:
    """Transform one hot vector to its value.

    Args:
        vector: the one hot vector

    Requires:
        the vector have a single value that is > 0

    Returns:
        the id of the biggest value in the vector

    """
    return np.argmax(vector)


def one_hots_to_ids(vectors: np.array) -> np.array:
    """Transform one hot encoded vector to their values.

    Args:
        vectors: an array of one hot vectors

    Requires:
        each vector have a single value that is > 0

    Returns:
        An array of id of the biggest value in the vector

    """
    return np.array([one_hot_to_id(vector) for vector in vectors])


def recursive_merge(data, update):
    """Recursively merge 2 dictionnaries.

    Args:
        data: the source dictionnary
        update: the dictionnary that will be merged

    Requires:
        no argument is None

    Returns:
        the recursively merged dictionnary

    """
    data = data.copy()
    for key, value in update.items():
        if isinstance(value, collections.Mapping):
            data[key] = recursive_merge(data.get(key, {}), value)
        else:
            data[key] = value
    return data
