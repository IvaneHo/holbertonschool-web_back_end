#!/usr/bin/env python3
"""
Module 1-simple_pagination
Implements basic pagination for a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Args:
            page (int): Page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the page.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        # Return the slice, or [] if out of range
        if start_idx >= len(dataset):
            return []
        return dataset[start_idx:end_idx]
