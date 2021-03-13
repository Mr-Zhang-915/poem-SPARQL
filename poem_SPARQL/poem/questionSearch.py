"""
coding=utf-8

File Name: questionSearch.py
Describe : 问题查询函数，完成SPARQL请求与解析
Comments ：
"""

from collections import OrderedDict
from SPARQLWrapper import SPARQLWrapper, JSON

# 定义服务器连接类
class sparqlConnect:
    def __init__(self, url="http://localhost:3030/poem_kbqa"):
        self.sparqlConnect = SPARQLWrapper(url)     # 服务器连接

    def get_sparql_result(self, query):     # 获取查询结果函数
        self.sparqlConnect.setQuery(query)
        self.sparqlConnect.setReturnFormat(JSON)
        return self.sparqlConnect.query().convert()

    def parse_result(self, query_result):       # 解析结果
        try:
            query_head = query_result['head']['vars']
            query_results = list()
            for r in query_result['results']['bindings']:
                temp_dict = OrderedDict()
                for h in query_head:
                    temp_dict[h] =r[h]['value']
                query_results.append(temp_dict)
            return query_head, query_results
        except KeyError:
            return None, query_result['boolean']

    def get_sparql_result_value(self, query_result):
        query_head,query_result =self.parse_result(query_result)
        if query_head is None:
            return query_result
        else:
            values = list()
            for qr in query_result:
                for _, value in qr.items():
                    values.append(value)
            return values

