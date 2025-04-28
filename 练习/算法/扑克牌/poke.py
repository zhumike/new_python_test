# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :poke
# @Date     :2025/4/16 21:24
# @Author   :zhuzhenzhong
# @Software :PyCharm

输入：5 张牌，每张牌有两个属性：

花色：'♠'、'♥'、'♣'、'♦'（Spades, Hearts, Clubs, Diamonds）

点数：2–10，J，Q，K，A

目标：判断是否构成 同花顺（Straight Flush）

print(is_straight_flush(['♠10', '♠J', '♠Q', '♠K', '♠A']))  # True
print(is_straight_flush(['♠2', '♠3', '♠4', '♠5', '♠A']))  # True
print(is_straight_flush(['♠2', '♠3', '♠4', '♠6', '♠7']))  # False
print(is_straight_flush(['♠2', '♥3', '♠4', '♠5', '♠6']))  # False


-------------------------------------------------
"""

def is_straight_flush(cards):
    if len(cards) != 5:
        return False

    # 1. 分离花色与点数
    suits = [card[0] for card in cards]
    ranks = [card[1:] for card in cards]

    # 2. 检查是否同花
    if len(set(suits)) != 1:
        return False

    # 3. 点数转化为数字
    value_map = {
        'A': 14, 'K': 13, 'Q': 12, 'J': 11,
        '10': 10, '9': 9, '8': 8, '7': 7, '6': 6,
        '5': 5, '4': 4, '3': 3, '2': 2
    }

    try:
        values = [value_map[r] for r in ranks]
    except KeyError:
        return False

    values.sort()

    # 4. 检查顺子（A-2-3-4-5 特判）
    def is_consecutive(vals):
        return all(vals[i] + 1 == vals[i + 1] for i in range(4))

    return is_consecutive(values) or values == [2, 3, 4, 5, 14]  # 处理 A-2-3-4-5

print(is_straight_flush(['♠10', '♠J', '♠Q', '♠K', '♠A']))
#test1  new