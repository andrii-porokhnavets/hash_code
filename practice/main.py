def parse_file(filename):
    with open('in/' + filename, 'r') as f:
        content = f.readlines()
        l1 = content[0].split()
        print(l1)
        # slices = [int(i) for i in content[1].split()]
        # limit = int(l1[0])

    return 1, 1


def write_answer(filename, answer):
    with open('practice/out/' + filename, 'w+') as f:
        f.write(str(len(answer)) + '\n')
        f.write(' '.join(str(s) for s in answer))


def solve(pizza_slices, limit):
    slices_sum = 0
    for i, s in enumerate(pizza_slices):
        slices_sum += s
        if slices_sum > limit:
            slices_sum -= s
            break

    return list(range(i))


# filenames = ['a_example', 'b_small', 'c_medium', 'd_quite_big', 'e_also_big']
filenames = ['a_example']
for filename in filenames:
    slices, limit = parse_file(filename + '.txt')
    result = solve(slices, limit)
    write_answer(filename + '.out', result)

