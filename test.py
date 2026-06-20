import re
def check_the_bt_state(s):
    pattern = r'.*не готов[а]? к командировкам.*'
    pat_2 = r'.*[^н][^е] готов[а]? к \w*\s*командировкам.*'
    res = re.match(pattern=pattern, string=s)
    res_2 = re.match(pattern=pat_2, string=s)
    if res:
        return False
    elif res_2:
        return True
    else:
        return False
    

print(check_the_bt_state("… , не готов к командировкам , …"))