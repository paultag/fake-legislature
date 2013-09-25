# Copyright (c) Sunlight Labs, 2013, under the terms of the BSD-3 clause
# license.
#
#  Contributors:
#
#    - Paul Tagliamonte <paultag@sunlightfoundation.com>


from pupa.scrape import Scraper, Legislator, Committee



class VoidPersonScraper(Scraper):


    def get_people(self):
        root = Committee(name='Root Committee')
        root.add_source("fake-data")
        yield root

        com = Committee(name='Root A')
        com.add_source("fake-data")
        yield com

        com = Committee(name='Subcommitee of Root Committee 1')
        com.add_source("fake-data")
        com.parent = root
        yield com

        com1 = Committee(name='Subcommitee of Root Committee 2')
        com1.add_source("fake-data")
        com1.parent = root
        yield com1

        com = Committee(name='Double Subcommitee of Root Committee 2')
        com.add_source("fake-data")
        com.parent = com1
        yield com

        com1j = Committee(name='Subcommitee of Root A Committee 1')
        com1j.add_source("fake-data")
        com1j.parent = com
        yield com1j

        com1j = Committee(name='Subcommitee of Root A Committee 2')
        com1j.add_source("fake-data")
        com1j.parent = com
        yield com1j
