# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     max_score = 0
#     le = len(strs)
#     if le == 0:
#         return ""
#     elif le == 1:
#         return strs[0]
#     ret = ""
#     for idx, s in enumerate(strs):
#         for rs in strs[(idx+1):]:
#             count = 1
#             c = 0
#             prefix = ""
#             while count <= len(s):
#                 prefix = s[:count]
#                 if rs[:count] == prefix:
#                     c += 1
#                 else:
#                     break
#                 count += 1
#             if c > max_score:
#                 ret = prefix[:(count-1)]
#                 max_score = c
#     return ret

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    for idx, s in enumerate(strs):
        if idx == 0:
            prefix = s
        else:
            le = len(s)
            for i,ps in enumerate(prefix):
                if i>=le or ps != s[i]:
                    prefix = s[:i]
                    break
                else:
                    prefix = s[:(i+1)]
    return prefix

print longestCommonPrefix(["a", "ab",  "ab"])