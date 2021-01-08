import argparse


def get_args() -> argparse.Namespace:
    """Get the arguments of the command line.

    Returns:
        A namespace containing the arguments

    """
    argparser = argparse.ArgumentParser(description=__doc__)
    # Used in data_main.py
    argparser.add_argument(
        "-p",
        "--process",
        dest="process",
        action="store_true",
        default=False,
        help="Process raw data",
    )
    argparser.add_argument(
        "-u",
        "--upload",
        dest="upload",
        action="store_true",
        default=False,
        help="Upload processed data",
    )
    # Used in model_main.py, model_opti.py and model_prod.py
    argparser.add_argument(
        "-c",
        "--config",
        dest="config",
        metavar="C",
        default=None,
        type=str,
        help="The Configuration file",
    )
    # Used in model_opti.py
    argparser.add_argument(
        "-hs",
        "--hyperspace",
        dest="hyperspace",
        metavar="HS",
        default=None,
        type=str,
        help="The hyperspace python file",
    )
    argparser.add_argument(
        "-t",
        "--trials",
        dest="trials",
        metavar="T",
        default=None,
        help="The trials pickle file",
    )
    args = argparser.parse_args()
    return args
