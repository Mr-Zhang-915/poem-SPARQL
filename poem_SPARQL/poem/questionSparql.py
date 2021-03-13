"""
coding=utf-8

File Name: questionSparql.py
Describe : 问题转换函数，将自然语言问题转换为SPARQL查询语句
Comments ：
"""

import wordHandle
import questionMapping

class QuestionSparql:
    def __init__(self, dict_paths):
        self.tw = wordHandle.Tagger(dict_paths)  # 自定义分词
        self.rules = questionMapping.rules  # 定义搜索规则

    def get_sparql(self, question):  # 语义解析
        word_objects = self.tw.get_word_objects(question)
        queries_dict = dict()
        for rule in self.rules:
            query, num = rule.apply(word_objects)
            if query is not None:
                queries_dict[num] = query

        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            for key, value in queries_dict.items():
                return value
        else:
            # 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]
