class Solution:
    def __init__(self):
        self.des_city = {}
        self.src_city = {}


    def destCity(self, paths: List[List[str]]) -> str:
        for src, des in paths:
            if des not in self.des_city:
                self.des_city[des]=1
            if src not in self.src_city:
                self.src_city[src]=1

        for k in self.des_city.keys():
            if k not in self.src_city:
                return k
