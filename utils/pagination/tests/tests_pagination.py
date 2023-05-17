from unittest import TestCase
from utils.pagination.pagination import make_pagination_range


class TestMakePaginationRange(TestCase):
    def test_pagination_range_returns_a_range(self) -> None:
        pagination = make_pagination_range(list(range(1, 10)),
                                           qty_pages=4,
                                           current_page=1,
                                           )

        self.assertEqual(pagination['pagination'], [1, 2, 3, 4])

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
        self.assertTrue(pagination_4['first_page_out_of_range'])

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
        self.assertTrue(pagination_0['first_page_out_of_range'])
        self.assertTrue(pagination_0['last_page_out_of_range'])

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
        self.assertTrue(pagination_4['first_page_out_of_range'])

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
