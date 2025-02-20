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

        display_pros = [[pro.title, pro.rating, pro.comment] for pro in self.pros]
        display_cons = [[con.title, con.rating, con.comment] for con in self.cons]

        tab_pros = tab.tabulate(display_pros, headers=element_headers, tablefmt="rst")
        tab_cons = tab.tabulate(display_cons, headers=element_headers, tablefmt="rst")

        tab_total = f"PROS\n" \
                    f"{tab_pros}\n" \
                    f"CONS\n" \
                    f"{tab_cons}\n"

        return tab_total

    def _add_element(self, element: Element, element_list: list):
        element_list.append(element)

    def add_pro(self, pro: Pro):
        self._add_element(pro, self.pros)

    def add_con(self, con: Con):
        self._add_element(con, self.cons)

    def _get_partial_score(self, elements: list[Element]):
        partial_rating = 0
        for element in elements:
            print(element)
            print(element.rating)
            partial_rating += element.rating

        return partial_rating

    def _get_pro_score(self):
        return self._get_partial_score(self.pros)

    def _get_con_score(self):
        return self._get_partial_score(self.cons)

    def get_score(self) -> float:
        pro_score = self._get_pro_score()
        con_score = self._get_con_score()
        return pro_score-con_score


if __name__ == "__main__":
    test_pro = Pro("test_pro_2", rating=2)
    test_con = Con("test_con_2", rating=2)

    test_collection = Collection("test collection")
    test_collection.add_pro(test_pro)
    test_collection.add_con(test_con)

    print(test_collection)

    print(test_collection.get_score())

