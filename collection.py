import tabulate as tab
from elements import Element, Pro, Con
class Collection:

    def __init__(self, title):
        self.title = title
        self.pros = []
        self.cons = []

        self.score = self.get_score()

    def __str__(self):
        element_headers = ["Title", "Rating", "Comment"]
        collection_headers = ["PROS", "CONS"]

        display_pros = [[pro.title, pro.rating, pro.comment] for pro in self.pros]
        display_cons = [[con.title, con.rating, con.comment] for con in self.cons]

        tab_pros = tab.tabulate(display_pros, headers=element_headers)
        print(tab_pros)
        tab_cons = tab.tabulate(display_cons, headers=element_headers)
        print(tab_cons)

        # This doesn't work
        tab_total = tab.tabulate([tab_pros, tab_cons], headers=collection_headers)

        return tab_total

    def _add_element(self, element: Element, element_list: list):
        element_list.append(element)

    def add_pro(self, pro: Pro):
        self._add_element(pro, self.pros)

    def add_con(self, con: Con):
        self._add_element(con, self.cons)

    def get_score(self) -> float:
        # TO DO: Calculate the weighed pro/con balance based on the number of pros/cons and their .rating attribute
        return 0.0

if __name__ == "__main__":
    test_pro = Pro("test_pro_2", rating=2)
    test_con = Con("test_con_2", rating=2)

    test_collection = Collection("test collection")
    test_collection.add_pro(test_pro)
    test_collection.add_con(test_con)

    print(test_collection)