from rest_framework.pagination import PageNumberPagination


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'qtd'
    max_page_size = 100
    invalid_page_message = 'Mano???'