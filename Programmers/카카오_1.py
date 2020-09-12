def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2,3단계
    new_id = list(new_id)
    length = len(new_id)
    temp = ""
    for idx,val in enumerate(new_id):
        if val.isalnum() or val == '_' or val == '.' or val == '-':
            temp+=val
    new_id = temp
    #3단계
    temp = new_id
    new_id = ""
    flag = True
    for val in temp:
        if val == '.':
            if flag:
                new_id += val
                flag = False
            else:
                continue
        else:
            flag = True
            new_id+= val

    #4단계
    new_id = "".join(new_id)
    new_id = new_id.strip(".")

    #5단계
    if new_id == "":
        new_id = "a"
    #6단계
    if len(new_id)>15:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    elif len(new_id)<3:
        new_id = (new_id+new_id[-1]*3)[:3]
    return new_id
print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))

