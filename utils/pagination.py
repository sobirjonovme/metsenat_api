from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "size"
    page_size = 10

    def get_paginated_response(self, data):
        current = self.page.number
        total_pages = self.page.paginator.num_pages

        previous_page = None if current == 1 else current-1
        next_page = None if current == total_pages else current+1

        response = {
            "current": current,
            'previous': previous_page,
            'next': next_page,
            "total_pages": total_pages,
            "page_items": len(self.page),
            "total_items": self.page.paginator.count,
            "results": data,
        }

        return Response(response)
