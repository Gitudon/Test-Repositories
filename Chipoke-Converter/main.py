def convert_chipoke_number(chipoke_number: str):
    if 'a' <= chipoke_number[-1] <= 'z':
        # 末尾がアルファベットならその部分を取得
        alpha = chipoke_number[-1]
    else:
        # 末尾がアルファベットでなければそのまま返す
        return chipoke_number
    # 数字の部分を取得
    number = chipoke_number[:-1]
    # アルファベットの数値を計算
    alpha_value = ord(alpha) - ord('a') + 1
    # 実際の数値を計算
    actual_value = int(float(number) * (10 ** (3 * alpha_value)))
    return actual_value

def main():
    target = input("変換したい数値を入力してください: ")
    convert_chipoke_number(target)
    print(f"変換結果: {convert_chipoke_number(target)}")

if __name__=="__main__":
    main()