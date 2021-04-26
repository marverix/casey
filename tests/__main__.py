import unittest
import casey


class TestCasey(unittest.TestCase):

    def test_clean(self):
        expected = 'every 1 WORD is very IMPORTANT'

        self.assertEqual(
            casey.clean('every1WORDIsVeryIMPORTANT'),
            expected,
            'Supports camelCase'
        )

        self.assertEqual(
            casey.clean('Every1WORDIsVeryIMPORTANT'),
            expected,
            'Supports PamelCase'
        )

        self.assertEqual(
            casey.clean('every-1-WORD-is-very-IMPORTANT'),
            expected,
            'Supports kebab-case'
        )

        self.assertEqual(
            casey.clean('every_1_WORD_is_very_IMPORTANT'),
            expected,
            'Supports snake_case'
        )

        self.assertEqual(
            casey.clean('EVERY_1_WORD_IS_VERY_IMPORTANT'),
            expected.lower(),
            'Supports UPPER_SNAKE_CASE'
        )

    def test_camel(self):
        self.assertEqual(
            casey.camel('hello'),
            'hello',
            'Should make no change at all'
        )

        self.assertEqual(
            casey.camel("Hello, I'm from District 9 and I'm looking for a job!"),
            'helloImFromDistrict9AndImLookingForAJob',
            'Supports normal sentence'
        )

        self.assertEqual(
            casey.camel('every-1-WORD-is-very-IMPORTANT'),
            'every1WORDIsVeryIMPORTANT',
            'Supports kebab-case'
        )

        self.assertEqual(
            casey.camel('every_1_WORD_is_very_IMPORTANT'),
            'every1WORDIsVeryIMPORTANT',
            'Supports snake_case'
        )

        self.assertEqual(
            casey.camel('EVERY_1_WORD_IMPORTANT'),
            'every1WordImportant',
            'Supports UPPER_SNAKE_CASE'
        )

    def test_pascal(self):
        self.assertEqual(
            casey.pascal('Hello'),
            'Hello',
            'Should make no change at all'
        )

        self.assertEqual(
            casey.pascal("Hello, I'm from District 9 and I'm looking for a job!"),
            'HelloImFromDistrict9AndImLookingForAJob',
            'Supports normal sentence'
        )

        self.assertEqual(
            casey.pascal('every-1-WORD-is-very-IMPORTANT'),
            'Every1WORDIsVeryIMPORTANT',
            'Supports kebab-case'
        )

        self.assertEqual(
            casey.pascal('every_1_WORD_is_very_IMPORTANT'),
            'Every1WORDIsVeryIMPORTANT',
            'Supports snake_case'
        )

        self.assertEqual(
            casey.pascal('EVERY_1_WORD_IMPORTANT'),
            'Every1WordImportant',
            'Supports UPPER_SNAKE_CASE'
        )

    def test_kebab(self):
        self.assertEqual(
            casey.kebab('hello-world'),
            'hello-world',
            'Should make no change at all'
        )

        self.assertEqual(
            casey.kebab("Hello, I'm from District 9 and I'm looking for a job!"),
            'hello-im-from-district-9-and-im-looking-for-a-job',
            'Supports normal sentence'
        )

        self.assertEqual(
            casey.kebab('every1WORDIsVeryIMPORTANT'),
            'every-1-WORD-is-very-IMPORTANT',
            'Supports camelCase'
        )

        self.assertEqual(
            casey.kebab('every_1_WORD_is_very_IMPORTANT'),
            'every-1-WORD-is-very-IMPORTANT',
            'Supports snake_case'
        )

        self.assertEqual(
            casey.kebab('EVERY_1_WORD'),
            'every-1-word',
            'Supports UPPER_SNAKE_CASE'
        )

    def test_snake(self):
        self.assertEqual(
            casey.snake('hello_world'),
            'hello_world',
            'Should make no change at all'
        )

        self.assertEqual(
            casey.snake("Hello, I'm from District 9 and I'm looking for a job!"),
            'hello_im_from_district_9_and_im_looking_for_a_job',
            'Supports normal sentence'
        )

        self.assertEqual(
            casey.snake('every1WORDIsVeryIMPORTANT'),
            'every_1_WORD_is_very_IMPORTANT',
            'Supports camelCase'
        )

        self.assertEqual(
            casey.snake('every-1-WORD-is-very-IMPORTANT'),
            'every_1_WORD_is_very_IMPORTANT',
            'Supports kebab-case'
        )

    def test_snake_with_upper(self):
        self.assertEqual(
            casey.snake('HELLO_WORLD', upper=True),
            'HELLO_WORLD',
            'Should make no change at all'
        )

        self.assertEqual(
            casey.snake("Hello, I'm from District 9 and I'm looking for a job!", upper=True),
            'HELLO_IM_FROM_DISTRICT_9_AND_IM_LOOKING_FOR_A_JOB',
            'Supports normal sentence'
        )

        self.assertEqual(
            casey.snake('every1WORDIsVeryIMPORTANT', upper=True),
            'EVERY_1_WORD_IS_VERY_IMPORTANT',
            'Supports camelCase'
        )

        self.assertEqual(
            casey.snake('every-1-WORD-is-very-IMPORTANT', upper=True),
            'EVERY_1_WORD_IS_VERY_IMPORTANT',
            'Supports kebab-case'
        )

    def test_upper_first(self):
        self.assertEqual(
            casey.upper_first('que Tal?'),
            'Que Tal?',
            'Return string with only first letter upper'
        )

        self.assertEqual(
            casey.upper_first('?worKs!'),
            '?WorKs!',
            'Return string with very first letter upper'
        )

    def test_lower_first(self):
        self.assertEqual(
            casey.lower_first('Que Tal?'),
            'que Tal?',
            'Return string with only first letter lower'
        )

        self.assertEqual(
            casey.lower_first('?WOrkS!'),
            '?wOrkS!',
            'Return string with very first letter lower'
        )


if __name__ == '__main__':
    unittest.main()
