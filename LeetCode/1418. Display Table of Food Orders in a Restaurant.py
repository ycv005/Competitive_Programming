from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        res = [["Table"]]
        items = set()
        tables = set()
        d = {}
        for _, table, item in orders:
            table = int(table)
            items.add(item)
            tables.add(table)
            if table not in d:
                d[table] = {}
            if item not in d[table]:
                d[table][item] = 1
            else:
                d[table][item] += 1
        items = sorted(list(items))
        tables = sorted(list(tables))
        res[0] += items
        for table in tables:
            tmp = [str(table)]
            for item in items:
                if item in d[table]:
                    tmp.append(str(d[table][item]))
                else:
                    tmp.append('0')
            res.append(tmp)
        return res
