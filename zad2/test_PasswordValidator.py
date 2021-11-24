import unittest  # pragma: no cover
from assertpy import assert_that  # pragma: no cover
from PasswordValidator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = PasswordValidator()

    def test_not_valid_empty(self) -> None:
        assert_that(self.temp.check("")).is_false()

    def test_valid_password(self) -> None:
        assert_that(self.temp.check("zaq1@WSXpl")).is_true()

    def test_long_not_valid(self) -> None:
        assert_that(self.temp.check("ASDFSFSFDSF#$$#@$@#$@#$@$@asda")).is_false()

    def test_only_numbers(self) -> None:
        assert_that(self.temp.check("15654316516")).is_false()

    def test_not_valid_number(self) -> None:
        assert_that(self.temp.check("Tojsdsjak$%^^&")).is_false()

    def test_not_valid_letters(self) -> None:
        assert_that(self.temp.check("TsQ54564$%^^&")).is_false()

    def test_not_valid_special(self) -> None:
        assert_that(self.temp.check("FGASSFDkjasdjahjk4564656")).is_false()

    def test_not_valid_upper(self) -> None:
        assert_that(self.temp.check("zaq1@wsxpl")).is_false()

    def test_valid_password_diff(self) -> None:
        assert_that(self.temp.check("zaq1$&WSXpl")).is_true()

    def test_numbers(self) -> None:
        assert_that(self.temp.check).raises(
            TypeError).when_called_with(45645646465)

    def tearDown(self) -> None:
        self.temp = None


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
