import sys

def spelling_test(s, l):
    # total_sub_len = 0
    # for i in l:
    #     total_sub_len += len(i)
    # if total_sub_len != s:
    #     return False
    true_l = []
    for i in range(len(l)):
        if l[i] in s:
            true_l.append(l[i])
    if my_spell_help(s, true_l, "") != None:
        return True
    else:
        return False
def spelling_test_helper(s, l):
    return
def my_spell_help(s, l, curr_word):
    if curr_word == s:
        return True
    for i in range(len(l)):
        if (curr_word + l[i]) in s:
            curr_str = l.pop(i)
            if my_spell_help(s, l, curr_word + curr_str) != None:
                return True
            l.insert(i, curr_str)


def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))
if __name__ == "__main__":
    main()