"""
@Time    : 2020/6/11 14:55
@Author  : weijiang
@Site    : 
@File    : 6把元组用作记录.py
@Software: PyCharm
"""
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('{}/{}'.format(passport[0], passport[1]))

for country, _ in traveler_ids:
    print(country, '-', _)
