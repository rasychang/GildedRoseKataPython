# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    
    def test_single_update(self):
        items = [Item("single", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("single", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)
    
    def test_multiple_items_update(self):
        items = [Item("first", 1, 1), Item("second", 2, 2), Item("Third", 30, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("first", items[0].name)
        self.assertEquals("second", items[1].name)
        self.assertEquals("Third", items[2].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(1, items[1].sell_in)
        self.assertEquals(1, items[1].quality)
        self.assertEquals(29, items[2].sell_in)
        self.assertEquals(29, items[2].quality)
    
    def test_quality_not_negative(self):
        items = [Item("single", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("single", items[0].name)
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(0, items[0].quality)
    
    def test_Aged_Brie_quality_increase(self):
        items = [Item("Aged Brie", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(4, items[0].quality)
    
    def test_quality_increase_no_more_than_50(self):
        items = [Item("Aged Brie", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(50, items[0].quality)
    
    def test_Sulfuras_not_degrade(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 21)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(21, items[0].quality)


if __name__ == '__main__':
    unittest.main()
