h, m, s = map(int, input().split())
t = int(input())

if t >= 3600:
    h += t // 3600
    t = t % 3600
if t >= 60:
    m += t // 60
    t = t % 60
if t < 60:
    s += t
if s >= 60:
    m += s // 60
    s = s % 60
if m >= 60:
    h += m // 60
    m = m % 60
if h >= 24:
    h = h % 24
print(h, m, s)
