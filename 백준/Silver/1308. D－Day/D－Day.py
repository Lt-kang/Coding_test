from datetime import datetime, timedelta


y1, m1, d1 = map(int, input().split())
today = datetime(y1, m1, d1)

y2, m2, d2 = map(int, input().split())
d_day = datetime(y2, m2, d2)


if (datetime(y1 + 1000, m1, d1)) <= d_day:
    print("gg")
else:
    print(f"D-{(d_day-today).days}")

