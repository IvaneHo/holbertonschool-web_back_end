#!/usr/bin/env python3
"""
Module 0-simple_helper_function
This module contains a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index
        and the end index for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
