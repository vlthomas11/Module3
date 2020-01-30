from format_output import average_scores


class MyTestCase(average_scores.TestCase):
    def test_average(self):
        with mock.patch('builtins.input',side_effects=[85,90,95]):
        assert topic2.average() == 90

        #self.assertEqual(True, False)


if __name__ == '__main__':
    average_scores.main()
