
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)

    for x in a:
        freq[x] += 1

    prefix = 0
    ans = 0

    for i in range(n + 1):
        prefix += freq[i]

        if freq[i] == 0:
            break

        if prefix < k * (i + 1):
            break

        ans = i + 1

    print(ans)
