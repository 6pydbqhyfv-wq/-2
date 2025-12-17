import random
import math

# ラジアン・度数対応
angles = [
    ("π/6", 30), ("π/4", 45), ("π/3", 60), ("π/2", 90),
    ("2π/3", 120), ("3π/4", 135), ("5π/6", 150), ("π", 180)
]

# 正確な三角比の値
values = {
    ("sin", 30): "1/2", ("cos", 30): "√3/2", ("tan", 30): "1/√3",
    ("sin", 45): "1/√2", ("cos", 45): "1/√2", ("tan", 45): "1",
    ("sin", 60): "√3/2", ("cos", 60): "1/2", ("tan", 60): "√3",
    ("sin", 90): "1", ("cos", 90): "0", ("tan", 90): "定義されない",
    ("sin",120): "√3/2", ("cos",120): "-1/2", ("tan",120): "-√3",
    ("sin",135): "1/√2", ("cos",135): "-1/√2", ("tan",135): "-1",
    ("sin",150): "1/2", ("cos",150): "-√3/2", ("tan",150): "-1/√3",
    ("sin",180): "0", ("cos",180): "-1", ("tan",180): "0"
}

functions = ["sin", "cos", "tan"]

score = 0
TOTAL = 10

print("=== 三角比 選択式テスト（全10問） ===")

for i in range(TOTAL):
    rad, deg = random.choice(angles)
    func = random.choice(functions)
    correct = values[(func, deg)]

    # 選択肢作成
    choices = list(set(random.sample(list(values.values()), 3)))
    if correct not in choices:
        choices.append(correct)

    choices = choices[:4]
    random.shuffle(choices)

    print(f"\n第{i+1}問：{func}({rad} ラジアン) はどれ？")
    for j, c in enumerate(choices):
        print(f"{j+1}: {c}")

    ans = int(input("番号で答えよ："))

    if choices[ans-1] == correct:
        print("○ 正解！")
        score += 1
    else:
        print(f"× 不正解。正解は {correct}")

print(f"\n結果：{score} / {TOTAL} 点")
if score >= 7:
    print("🎉 合格！")
else:
    print("❌ もう一回チャレンジ！")
