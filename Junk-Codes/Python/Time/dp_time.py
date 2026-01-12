import time

time_sta = time.time()

# ここから時間計測したい部分
N = 20000
dp = [0] * (N + 1)
num_kitte = 8
kitte = [1, 2, 5, 10, 20, 50, 63, 84]
dp[0] = 1
for x in kitte:
    for i in range(N - x + 1):
        dp[i + x] += dp[i]
print(str(dp[N]) + "通り")
# ここまで時間計測したい部分

time_end = time.time()
time = time_end - time_sta
print("実行時間:" + str(f"{time:10}") + "秒")
