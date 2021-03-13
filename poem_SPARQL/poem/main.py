"""
coding=utf-8

File Name: main.py
Describe : 主函数
Comments : 在运行主函数之前，要启动Fuseki服务器
"""
import questionSearch
import questionSparql


if __name__ == '__main__':
    sparql = questionSearch.sparqlConnect()
    q2s = questionSparql.QuestionSparql([u'./data/poem.txt', u'./data/poet.txt', u'./data/dynasty.txt', u'./data/verse.txt', u'./data/extendWords.txt'])

    while True:
        question = input("请输入问题(q退出): ")

        if question == 'q':
            break

        query = q2s.get_sparql(question)
        if query is not None:
            result = sparql.get_sparql_result(query)
            values = sparql.get_sparql_result_value(result)

            if len(values):
                print("、".join(values))
            else:
                print("没有找你要的答案，我会继续努力学习的喔")
        else:
            print("俺不懂你说的是啥嘞")

