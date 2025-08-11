#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the dataset using a deletion-resilient approach.

        Args:
            index (int): Start index for the page.
            page_size (int): Number of items to return.

        Returns:
            Dict[str, Any]: Dictionary containing:
                - index: the current start index
                - next_index: the next index to query
                - page_size: size of the returned page
                - data: the dataset page
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index

        # Collect items until reaching page_size or running out of data
        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
