"""
Created by adam on 8/24/18
"""
import os

__author__ = 'adam'


def makeDataFileIterator(folderPath, exclude=[]):
    """
    Returns an iterator of all files in the source directory
    so that each file has its path appended to it.

    Args:
        folderPath: The path to get file names from
        exclude: file names which should not be included in the output list

    """
    exclude = exclude if any(exclude) else ['.DS_Store']
    for root, dirs, files in os.walk(folderPath):
        for name in files:
            if name not in exclude:
                yield os.path.join(root, name)


if __name__ == '__main__':
    pass