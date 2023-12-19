N, K = map(int, input().split())
elec = list(map(int, input().split()))

'''
뺄 필요가 없는 경우 뺴지 않는다
'''
cnt = 0
socket = set()
for i in range(K):
    now = elec[i]

    if now in socket:
        # 이미 소켓에 있음
        continue

    if len(socket) < N:
        # 소켓에 여유가 있음
        socket.add(now)
        continue

    last = 0
    for plug in socket:

        if plug not in elec[i+1:]:
            # 만약 나중에 다시 사용되지 않거나
            socket.remove(plug)
            cnt += 1
            break

        for k in range(i+1, K):
            # 가장 나중에 사용되는
            if elec[k] == plug:
                last = max(last, k)
                break

    if len(socket) == N:  # 나중에 사용되는 plug를 아직 안 지웠으면
        socket.remove(elec[last])
        cnt += 1

    socket.add(now)

print(cnt)
