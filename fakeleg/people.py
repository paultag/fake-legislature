# Copyright (c) Sunlight Labs, 2013, under the terms of the BSD-3 clause
# license.
#
#  Contributors:
#
#    - Paul Tagliamonte <paultag@sunlightfoundation.com>


from pupa.scrape import Scraper, Legislator, Committee
import random



class VoidPersonScraper(Scraper):


    def get_people(self):
        objs = []

        for x in range(2):
            root = Committee(name='FOO ROOT %s' % (x))
            root.add_source("fake-data")
            objs.append(root)

            com1 = Committee(name='FOO SUBSUB %s' % (x))
            com1.add_source("fake-data")


            com = Committee(name='FOO SUB %s' % (x))
            com.add_source("fake-data")
            com.parent = root
            objs.append(com)

            com1.parent = com
            objs.append(com1)

        random.shuffle(objs)
        return objs
