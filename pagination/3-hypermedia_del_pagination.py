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
            # NB: l'énoncé montre un truncated_dataset mais l'exemple de sortie
            # indique qu'on indexe tout (Nb items ~ 19418). On suit l'exemple.
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a page in a deletion-resilient way.

        Args:
            index (int): Start index for the page (0-based). If None, starts at 0.
            page_size (int): Number of items to return.

        Returns:
            Dict[str, Any]: {
                "index": current start index,
                "next_index": index to query next,
                "page_size": number of items returned,
                "data": list of rows
            }
        """
        # Handle None as 0 (exigence de l'énoncé)
        if index is None:
            index = 0

        # Validations
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        # On valide contre la taille d'origine du dataset (comme l'exemple)
        assert index < len(self.dataset())

        data: List[List] = []
        current = index

        # Avance jusqu'à collecter page_size éléments encore présents
        # ou jusqu'à épuisement des indices valides
        upper_bound = len(self.dataset())
        while len(data) < page_size and current < upper_bound:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current
        }
