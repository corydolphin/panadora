#!/usr/bin/env python
import unittest
from pandora import Pandora
import json

class TestPandora(unittest.TestCase):
    def setUp(self):
        self.pandora = Pandora()
        self.pandora.connect('killarcha@live.com','sweetness')

    def test_jsonify(self):
        str_rep = json.dumps(self.pandora.json())
        print str_rep
        print len(str_rep)
        new_inst = Pandora.hydrate(json.loads(str_rep))

        new_inst.get_stations()
        assert len(new_inst.stations) > 0

        print new_inst.stations[0].get_playlist(new_inst)


if __name__ == '__main__':
    unittest.main()
