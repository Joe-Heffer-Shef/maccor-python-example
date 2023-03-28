#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path

import batdata.extractors.maccor

DESCRIPTION = """
Battery data MACCOR file format processing example.

Please see README.md
"""

logger = logging.getLogger(__name__)


def get_args() -> argparse.Namespace:
    """
    Configure command-line arguments
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('-l', '--loglevel', default='INFO',
                        help='Verbosity: DEBUG,INFO,WARNING,ERROR')
    parser.add_argument('-p', '--path', type=Path, default=Path(),
                        help='The path of a directory containing MACCOR files. Default: current directory')
    parser.add_argument('--eps', type=float, default=None)

    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(level=args.loglevel)

    # Initialise the MACCOR extractor
    extractor = batdata.extractors.maccor.MACCORExtractor(eps=args.eps)

    # Iterate over MACCOR files
    for group in map(list, extractor.identify_files(path=args.path)):
        logger.info(f"MACCOR group: {group}")
        data = extractor.parse_to_dataframe(group)

        logger.info(repr(data))


if __name__ == '__main__':
    main()
