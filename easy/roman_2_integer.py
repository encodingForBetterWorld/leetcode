# coding=utf-8
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

# 右加左减, 重复数次

rule = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    ret = 0
    if len(s) == 1:
        return rule[s]
    else:
        pre = None
        count = 0
        while count < len(s):
            i = s[count]
            c_num = rule.get(i)
            if pre is not None:
                if pre == c_num:
                    ret += pre
                else:
                    # 左减
                    if pre < c_num:
                        ret -= pre
                    elif len(str(c_num))-len(str(pre)) < 2:
                        ret += pre
                    else:
                        s = s[count:]
                        count = 0
            pre = c_num
            count+=1
        ret += pre
        return ret

# print romanToInt("XLV")


convert_rule1 = {
    1: "I",
    2: "X",
    3: "C",
    4: "M"
}

convert_rule2 = {
    1: "V",
    2: "L",
    3: "D",
}

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    pre = None
    idx = 1
    pos = 1
    ret = ""
    while num:
        c = num / idx
        tmp = num - c * idx
        if pre is not None:
            target = tmp / (idx / 10)
            if target == 0:
                target = ""
            if 0 < target < 4:
                target = convert_rule1.get(pos) * target
            elif target == 4:
                target = convert_rule1.get(pos) + convert_rule2.get(pos)
            elif target == 5:
                target = convert_rule2.get(pos)
            elif target < 9:
                target = convert_rule2.get(pos) + (convert_rule1.get(pos) * (target - 5))
            elif target == 9:
                target = convert_rule1.get(pos) + convert_rule1.get(pos+1)
            ret = target + ret
            pos += 1
        if c == 0:
            break
        pre = c
        idx *= 10
    return ret

print intToRoman(999)