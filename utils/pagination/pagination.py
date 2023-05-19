from django.core.paginator import Paginator
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
        'first_page_out_of_range': (
            current_page > middle_range and len(page_range) > qty_pages
            ),
        'last_page_out_of_range': stop_range < total_pages,
    }


def make_pagination(request,
                    query_set,
                    objects_per_page,
                    qty_pages=4
                    ) -> Paginator:
    paginator = Paginator(query_set, objects_per_page)

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    page_object = paginator.get_page(current_page)

    pagination_range = make_pagination_range(paginator.page_range,
                                             qty_pages,
                                             current_page,
                                             )
    return page_object, pagination_range
