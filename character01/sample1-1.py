"""
@Time    : 2020/6/9 16:02
@Author  : weijiang
@Site    : 
@File    : sample1-1.py
@Software: PyCharm
"""
import collections
from random import choice

# 可以通过该方法构造一个类(没有方法,只有简单对象的类)
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]


deck = FrenchDeck()
print('纸牌的数量:', len(deck))

print('纸牌:', deck._cards)

print('随机抽取一张纸牌', choice(deck))

print('获取牌堆上的头三张纸牌:', deck[:3])

# [n::m]从n元素开始每隔m取一个元素
print('获取A纸牌:', deck[12::13])

for card in sorted(deck, key=spades_high):
    print(card)


