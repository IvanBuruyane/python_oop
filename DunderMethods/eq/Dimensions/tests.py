from Dimensions import Dimensions, lst_shop, lst_shop_sorted


class TestDimensions:

    def test_no_unprotected_properties(self):
        dim = Dimensions(40, 30, 120)
        args = dim.__dict__
        assert args.get("a") is None
        assert args.get("b") is None
        assert args.get("c") is None

    def test_get_object_property(self):
        dim = Dimensions(40, 30, 120)
        assert dim.a == 40
        assert dim.b == 30
        assert dim.c == 120

    def test_set_object_property_success(self):
        dim = Dimensions(40, 30, 120)
        new_a, new_b, new_c = Dimensions.MIN_DIMENSION, 43, Dimensions.MAX_DIMENSION
        dim.a = new_a
        dim.b = new_b
        dim.c = new_c
        args = dim.__dict__
        assert dim.a == new_a
        assert dim.b == new_b
        assert dim.c == new_c
        assert args.get("a") is None
        assert args.get("b") is None
        assert args.get("c") is None

    def test_set_object_property_not_valid(self):
        dim = Dimensions(40, 30, 120)
        new_a, new_b, new_c = 9, 49.43432, 100001
        dim.a = new_a
        dim.b = new_b
        dim.c = new_c
        args = dim.__dict__
        assert dim.a == 40
        assert dim.b == 30
        assert dim.c == 120
        assert args.get("a") is None
        assert args.get("b") is None
        assert args.get("c") is None

    def test_greater(self):
        dim1 = Dimensions(40, 30, 120)
        dim2 = Dimensions(2000, 600, 500)
        assert dim2 > dim1

    def test_greater_or_equal(self):
        dim1 = Dimensions(40, 30, 120)
        dim3 = Dimensions(100, 20, 72)
        dim2 = Dimensions(2000, 600, 500)
        assert dim2 >= dim1
        assert dim3 >= dim1

    def test_lower(self):
        dim1 = Dimensions(40, 30, 120)
        dim2 = Dimensions(2000, 600, 500)
        assert dim1 < dim2

    def test_greater_or_equal(self):
        dim1 = Dimensions(40, 30, 120)
        dim3 = Dimensions(100, 20, 72)
        dim2 = Dimensions(2000, 600, 500)
        assert dim1 <= dim2
        assert dim3 <= dim1


class TestShopItem:

    def test_sorting_by_dimension(self):
        exp_lst_shop = [
            ("кеды", 1024, 40, 30, 120),
            ("зонт", 500.24, 10, 20, 50),
            ("холодильник", 40000, 2000, 600, 500),
            ("табуретка", 2000.99, 500, 200, 200)
        ]
        exp_lst_shop_sorted = [
            ("зонт", 500.24, 10, 20, 50),
            ("кеды", 1024, 40, 30, 120),
            ("табуретка", 2000.99, 500, 200, 200),
            ("холодильник", 40000, 2000, 600, 500)
        ]
        act_lst_shop = [(item.name, item.price, item.dim.a, item.dim.b, item.dim.c) for item in lst_shop]
        act_lst_shop_sorted = [(item.name, item.price, item.dim.a, item.dim.b, item.dim.c) for item in lst_shop_sorted]
        assert act_lst_shop == exp_lst_shop
        assert act_lst_shop_sorted == exp_lst_shop_sorted
