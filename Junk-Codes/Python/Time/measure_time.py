import time

time_sta = time.time()

# ここから時間計測したい部分

print(60 * 60 * 24 * 365)

# ここまで時間計測したい部分

time_end = time.time()
time = time_end - time_sta
print("実行時間:" + str(f"{time:10}") + "秒")
