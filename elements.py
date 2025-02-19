class Element:

    def __init__(self, title: str, is_pro: bool = True, rating: int = 5, comment=None):
        self.title = title
        self.is_pro = is_pro
        self.rating = rating
        self.comment = comment

    def __str__(self):
        description_string = f"{self.title}\t{self.rating}\t{self.comment}"
        return description_string

    def get_pro_or_con(self):
        pro_con_status = "PRO" if self.is_pro is True else "CON"
        return pro_con_status

    def flip_pro_con(self):
        self.is_pro = not self.is_pro

    def change_rating(self, new_rating: int):
        if new_rating not in range(1, 11):
            print("New rating is out of range. Please submit a rating on a scale of 1 to 10.")
        else:
            self.rating = new_rating


if __name__ == "__main__":

    def test_display(test_element_display: Element):
        return f"{test_element_display.get_pro_or_con()}\t{test_element_display}"

    test_pro = Element("test_pro_2", True, rating=2)
    test_con = Element("test_con_2", False, rating=2)

    test_pro_comment = Element("test_pro_comment", True, rating=4, comment="Test comment")
    test_con_comment = Element("test_con_comment", False, rating=4, comment="Test comment")

    for test_element in [test_pro, test_con, test_pro_comment, test_con_comment]:
        print(test_display(test_element))

    test_pro_cond = Element("test_pro_cond", True, rating=6)
    test_con_prod = Element("test_con_prod", False, rating=6)

    for test_element in [test_pro_cond, test_con_prod]:
        print(test_display(test_element))
        test_element.flip_pro_con()
        print(test_display(test_element))

    test_pro_2_to_4 = Element("test_pro_2", True, rating=2)
    print(test_display(test_pro_2_to_4))
    test_pro_2_to_4.change_rating(4)
    print(test_display(test_pro_2_to_4))

    test_pro_2_to_11 = Element("test_pro_2", True, rating=2)
    print(test_display(test_pro_2_to_4))
    test_pro_2_to_11.change_rating(11)
    print(test_display(test_pro_2_to_4))
