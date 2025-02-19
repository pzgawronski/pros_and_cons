class Element:

    def __init__(self, title: str, is_pro: bool, rating: int, comment: str):
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

    def change_rating(self, new_rating: int):
        if new_rating not in range(1, 11):
            print("New rating is out of range. Please submit a rating on a scale of 1 to 10.")
        else:
            self.rating = new_rating


class Pro(Element):

    def __init__(self, title, rating=5, comment=None):
        super().__init__(title=title, rating=rating, comment=comment, is_pro=True)


class Con(Element):

    def __init__(self, title, rating=5, comment=None):
        super().__init__(title=title, rating=rating, comment=comment, is_pro=False)


if __name__ == "__main__":

    def test_display(test_element_display: Element):
        return f"{test_element_display.get_pro_or_con()}\t{test_element_display}"

    test_pro = Pro("test_pro_2", rating=2)
    test_con = Con("test_con_2", rating=2)

    test_pro_comment = Pro("test_pro_comment", rating=4, comment="Test comment")
    test_con_comment = Con("test_con_comment", rating=4, comment="Test comment")

    for test_element in [test_pro, test_con, test_pro_comment, test_con_comment]:
        print(test_display(test_element))

    test_pro_cond = Pro("test_pro_cond", rating=6)
    test_con_prod = Con("test_con_prod", rating=6)

    test_pro_2_to_4 = Pro("test_pro_2_to_4", rating=2)
    print(test_display(test_pro_2_to_4))
    test_pro_2_to_4.change_rating(4)
    print(test_display(test_pro_2_to_4))

    test_con_2_to_4 = Pro("test_con_2_to_4", rating=2)
    print(test_display(test_con_2_to_4))
    test_con_2_to_4.change_rating(4)
    print(test_display(test_con_2_to_4))

    test_pro_2_to_11 = Pro("test_pro_2_to_11", rating=2)
    print(test_display(test_con_2_to_4))
    test_pro_2_to_11.change_rating(11)
    print(test_display(test_con_2_to_4))

    test_con_2_to_11 = Pro("test_con_2_to_11", rating=2)
    print(test_display(test_con_2_to_4))
    test_con_2_to_11.change_rating(11)
    print(test_display(test_con_2_to_4))