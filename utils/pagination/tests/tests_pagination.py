from unittest import TestCase
import math


def make_pagination_range(page_range,
                          qty_pages,
                          current_page,
                          ):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    if start_range < 0:
        start_range = 0
        stop_range = qty_pages

    if stop_range >= total_pages:
        start_range = total_pages - qty_pages
        stop_range = total_pages

    if total_pages < qty_pages:
        start_range = 0
        stop_range = total_pages

    pagination = page_range[start_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'has_previous_page': current_page > middle_range,
        'has_next_page': current_page < total_pages,
    }


class TestMakePaginationRange(TestCase):
    def test_pagination_range_returns_a_range(self) -> None:
        pagination = make_pagination_range(list(range(1, 10)),
                                           qty_pages=4,
                                           current_page=1,
                                           )

        self.assertEqual(pagination, [1, 2, 3, 4])

    def test_pagination_range_is_static_when_current_page_is_less_than_middle_page(self) -> None:  # noqa: E501
        pagination_0 = make_pagination_range(list(range(1, 2)),
                                             qty_pages=4,
                                             current_page=1,
                                             )
        self.assertEqual(pagination_0['pagination'], [1])

        pagination_1 = make_pagination_range(list(range(1, 3)),
                                             qty_pages=4,
                                             current_page=1,
                                             )
        self.assertEqual(pagination_1['pagination'], [1, 2])

        pagination_2 = make_pagination_range(list(range(1, 20)),
                                             qty_pages=4,
                                             current_page=1,
                                             )
        self.assertEqual(pagination_2['pagination'], [1, 2, 3, 4])

        pagination_3 = make_pagination_range(list(range(1, 20)),
                                             qty_pages=4,
                                             current_page=2,
                                             )
        self.assertEqual(pagination_3['pagination'], [1, 2, 3, 4])

        pagination_4 = make_pagination_range(list(range(1, 20)),
                                             qty_pages=4,
                                             current_page=3,
                                             )
        self.assertEqual(pagination_4['pagination'], [2, 3, 4, 5])

        pagination_5 = make_pagination_range(list(range(1, 20)),
                                             qty_pages=4,
                                             current_page=4,
                                             )
        self.assertEqual(pagination_5['pagination'], [3, 4, 5, 6])

        pagination_6 = make_pagination_range(list(range(1, 20)),
                                             qty_pages=4,
                                             current_page=5,
                                             )
        self.assertEqual(pagination_6['pagination'], [4, 5, 6, 7])

    def test_pagination_range_is_static_when_last_page_is_next(self) -> None:
        pagination_0 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=5,
                                             )
        self.assertEqual(pagination_0['pagination'], [4, 5, 6, 7])

        pagination_1 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=6,
                                             )
        self.assertEqual(pagination_1['pagination'], [5, 6, 7, 8])

        pagination_1 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=7,
                                             )
        self.assertEqual(pagination_1['pagination'], [6, 7, 8, 9])

        pagination_2 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=8,
                                             )
        self.assertEqual(pagination_2['pagination'], [6, 7, 8, 9])

        pagination_3 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=9,
                                             )
        self.assertEqual(pagination_3['pagination'], [6, 7, 8, 9])

        pagination_4 = make_pagination_range(list(range(1, 10)),
                                             qty_pages=4,
                                             current_page=10,
                                             )
        self.assertEqual(pagination_4['pagination'], [6, 7, 8, 9])

    def test_pagination_range_load_correct_qty_of_pages_if_page_range_less_than_qty_pages(self) -> None:  # noqa: E501
        pagination_0 = make_pagination_range(list(range(1, 2)),
                                             qty_pages=4,
                                             current_page=10,
                                             )
        self.assertEqual(pagination_0['pagination'], [1])

        pagination_1 = make_pagination_range(list(range(1, 3)),
                                             qty_pages=4,
                                             current_page=10,
                                             )
        self.assertEqual(pagination_1['pagination'], [1, 2])

        pagination_2 = make_pagination_range(list(range(1, 4)),
                                             qty_pages=4,
                                             current_page=10,
                                             )
        self.assertEqual(pagination_2['pagination'], [1, 2, 3])

        pagination_2 = make_pagination_range(list(range(1, 4)),
                                             qty_pages=5,
                                             current_page=10,
                                             )
        self.assertEqual(pagination_2['pagination'], [1, 2, 3])
