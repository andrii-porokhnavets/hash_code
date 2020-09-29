import numpy as np
import math


class Lib:
    def __init__(self, i, line1, line2):
        line1_int = [int(a) for a in line1.split()]
        self.count_of_books = line1_int[0]
        self.sign_up_days = line1_int[1]
        self.books_per_day = line1_int[2]
        self.books = np.array([int(b) for b in line2.split()], dtype='int')
        self.index = i
        self.score = 0
        self.max_score = 0

    def calc_score(self, max_days, scores):
        book_days = (max_days - self.sign_up_days) * self.books_per_day
        # book_scores = np.sort(np.take(scores, self.books))[::-1]
        book_scores = sorted(self.books, key=lambda x: scores[x], reverse=True)
        # print(book_scores)
        self.score = sum(book_scores[:book_days])
        self.max_score = sum(book_scores)

        return self.score

    def __repr__(self):
        return f'Lib: ({self.index} {self.count_of_books} {self.sign_up_days} {self.books_per_day} {self.score} {self.max_score})'


def parse_file(filename):
    with open('in/' + filename, 'r') as f:
        content = f.readlines()
        header = [int(score) for score in content[0].split()]

        count_of_diff_books = header[0]
        count_of_libs = header[1]
        days_to_scan = header[2]
        books_score = np.array([int(score) for score in content[1].split()], dtype='int')

        libs = []
        for i in range(count_of_libs):
            lib = Lib(i, content[i * 2 + 2], content[i * 2 + 3])
            # lib.calc_score(days_to_scan, books_score)
            libs.append(lib)

    return count_of_diff_books, count_of_libs, days_to_scan, books_score, libs


def write_answer(filename, libs):
    # res = ''
    # count_of_libs = 0
    # for lib in libs:
    #     books_to_send_str = ''
    #     books_to_send_count = 0
    #     days_to_scan -= lib.sign_up_days
    #     count_books_to_send = days_to_scan * lib.books_per_day
    #     sorted_books = sorted(lib.books, key=lambda v: books_score[v], reverse=True)
    #     for book_index in sorted_books:
    #         score = books_score[book_index]
    #         if score > 0 and books_to_send_count <= count_books_to_send:
    #             books_score[book_index] = 0
    #             books_to_send_str += f'{book_index} '
    #             books_to_send_count += 1
    #
    #     if books_to_send_count > 0:
    #         count_of_libs += 1
    #         res += f'{lib.index} {books_to_send_count}\n{books_to_send_str[:-1]}\n'
    #
    # with open('out/' + filename, 'w+') as f:
    #     res = f'{count_of_libs}\n' + res
    #     f.write(res)

    with open('out/' + filename, 'w+') as f:
        f.write(f'{len(libs)}\n')
        for l in libs:
            f.write(f'{l.index} {len(l.books_to_send)}\n')
            f.write(' '.join(str(s) for s in l.books_to_send) + '\n')


def solve(libs, days_to_scan, books_score, count_of_libs):
    result_libs = []
    times = 0
    while days_to_scan > 0 and len(libs) > 0 and times < count_of_libs:
        times += 1

        # print(books_score)
        libs.sort(key=lambda x: (-x.calc_score(days_to_scan, books_score), x.sign_up_days), reverse=True)
        if days_to_scan - libs[-1].sign_up_days > 0:
            lib = libs.pop()
            days_to_scan -= lib.sign_up_days
            sorted_books = np.sort(np.take(books_score, lib.books))[::-1]
            # sorted_books = sorted(lib.books, key=lambda x: books_score[x], reverse=True)
            # print(sorted_books)
            books_to_send = sorted_books[:days_to_scan * lib.books_per_day]
            lib.books_to_send = books_to_send
            for b in books_to_send:
                books_score[b] = 0
            result_libs.append(lib)

    return result_libs


filenames = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
# filenames = ['e_so_many_books']
for filename in filenames:
    count_of_diff_books, count_of_libs, days_to_scan, books_score, libs = parse_file(filename + '.txt')
    print(sum(books_score))
    # print('start')
    # result = solve(libs, days_to_scan, books_score, count_of_libs)
    # print(filename)
    # print(result[:10])
    # write_answer(filename + '.txt', result)
    # print('finish')

