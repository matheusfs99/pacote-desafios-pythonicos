"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""
import heapq
def linear_merge(list1, list2):
    # +++ SUA SOLUÇÃO +++
    # response = []
    #
    # while len(list1) + len(list2) > 0:  # while = O(n)
    #     has_only_list1 = list1 and not list2
    #     has_both_lists = list1 and list2
    #     pop_from_list1 = has_only_list1 or (has_both_lists and list1[-1] > list2[-1])
    #     response.append(list1.pop(-1) if pop_from_list1 else list2.pop(-1))  # append = O(1)
    #
    # response.reverse()  # reverse = O(n)
    # return response

    # Resposta com complexidade linear usando heapq
    import heapq
    return list(heapq.merge(list1, list2))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
