import re


def parse_para(data, para):
    ret = {}
    for k, v in para.items():
        if v:
            for vl in v:
                x = ret[k].get(vl) if ret.get(k) else data.get(vl)
                if isinstance(x, dict):
                    ret[k] = x
                elif isinstance(x, list):
                    ret[k] = x[0]
                else:
                    ret[k] = x
                    break
        else:
            ret[k] = ''
    return ret


_data = {
    'name': 'hehao',
    'age': [0, 18],
    'marjor': {'one': 'java', 'two': ['python', 'other']},
    'time': None,
    'marjor2': {'one': 'java', 'two': None},
    'marjor3': {'one': 'java', 'two': 0}
}
_para = {'name': ['name'], 'age': ['age'], 'marjor': ['marjor', 'two'], 'time': [], 'marjor2': ['marjor2', 'two'], 'marjor3': ['marjor3', 'two']}
print(parse_para(_data, _para))

# str = "https://api-h2-eagle.tiktokv.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAAOFmAycXAZsAGA_jWiPfG3N8EI6nq9-HeI71wciXJpmsSz7XvDLsECFxcCmKbWmE5&count=20"
# print(re.findall('sec_user_id=(.*?)&', str)[0])