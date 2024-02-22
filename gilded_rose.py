# -*- coding: utf-8 -*-
from collections import defaultdict

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class DegradeSetting:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, aged=1, degrade=1, multiplier=1):
        self.aged = aged
        self.degrade = degrade
        self.multiplier = multiplier

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        def get_backstage_pass_multi(quality, sell_in):
            if sell_in <= 0:
                return -quality
            if sell_in <= 5:
                return 3
            if sell_in <= 10:
                return 2
            return 1

        for item in self.items:
            
            default_multiplier = 1 + int(item.sell_in <= 0)
            item_config = defaultdict(lambda: DegradeSetting(), {
                "Aged Brie": DegradeSetting(degrade=-1, multiplier=default_multiplier),
                "Sulfuras, Hand of Ragnaros": DegradeSetting(0, 0, default_multiplier),
                "Backstage passes to a TAFKAL80ETC concert": DegradeSetting(degrade=-1, multiplier=get_backstage_pass_multi(item.quality, item.sell_in)),
            })

            
            item.quality = min(max(0, item.quality - item_config[item.name].degrade * item_config[item.name].multiplier), 50)
            item.sell_in = item.sell_in - item_config[item.name].aged
    