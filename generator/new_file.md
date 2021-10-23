## Generator of md-files

(no link)

```python
def get_files():
    txt_file = open('solution.txt', 'r')
    py_file = open('tests.py', 'r')
    return txt_file, py_file


solution, tests = get_files()
result_file = open('arrays.md', 'w')

result_file.write('## ' + solution.readline() + '\n')  # заголовок
result_file.write(solution.readline() + '\n')  # ссылка на leetcode

# основная программа
result_file.write('```python\n')
result_file.write(solution.read() + '\n')
result_file.write('```\n\n')
solution.close()

# тесты
result_file.write('<details><summary>Test cases</summary><blockquote>\n\n')  # ссылка на тесты
result_file.write('```python\n')
result_file.write(tests.read() + '\n')
result_file.write('```\n\n')
result_file.write('</blockquote></details>\n\n')  # "закрыть" ссылку на тесты
tests.close()

result_file.close()

```

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import generator_md


class TestGeneratorMd(unittest.TestCase):
    def test_test5(self):
        self.assertEqual(5, 5)

    # ???

```

</blockquote></details>

