def solution(tickets):
    ticket_dict = dict()
    for ticket in tickets:
        if ticket[0] in ticket_dict:
            ticket_dict[ticket[0]].append(ticket[1])
            ticket_dict[ticket[0]].sort(reverse = True)
        else:
            ticket_dict[ticket[0]] = [ticket[1]]
    stack = ["ICN"]
    path = []
    while stack:
        #다음이 없는 경우
        now = stack[-1]
        if now not in ticket_dict or not ticket_dict[now]:
            path.append(stack.pop())
            continue
        stack.append(ticket_dict[now].pop())
    path.reverse()
    return path