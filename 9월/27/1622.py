import sys

sys.stdin = open('input.txt')

def mk_list(s):
    ret_list = []
    for w in s:
        if not w in ret_list:
            ret_list.append(w)
    return ret_list

def check(a, b):
    ans = []
    ans_str = ''
    for w in a:
        if w in b:
            ans.append(w)
    ans.sort()
    for s in ans:
        ans_str += s
    return ans_str



while True:
    try:
        a = input()
        b = input()
    except:
        break
    
    list_a = mk_list(a)
    list_b = mk_list(b)
    ans_str = check(list_a, list_b)
    print(ans_str)