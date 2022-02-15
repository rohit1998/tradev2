import datetime as dt
import backtrader as bt
from backtrader import date2num, num2date
from trade.data_fetch.jdata import get_live_symbol_data_line
from trade.utils.data_util import get_data_file
import time
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

class DataFeed(bt.feeds.GenericCSVData):


    def __init__(self, config):
        self.config = config

        self.init_params()
                # self.file_header = ()        
        # date,open,high,low,previousClose,close,volume

    def init_params(self):
        self.p.dtformat = self.config['data_feed']['p']['dtformat']
        self.p.datetime = self.config['data_feed']['p']['datetime']
        self.p.open = self.config['data_feed']['p']['open']
        self.p.high = self.config['data_feed']['p']['high']
        self.p.low = self.config['data_feed']['p']['low']
        self.p.close = self.config['data_feed']['p']['close']
        self.p.volume = self.config['data_feed']['p']['volume']
        self.p.time = self.config['data_feed']['p']['time']
        self.p.openinterest = self.config['data_feed']['p']['openinterest']
        self.p.reverse = self.config['data_feed']['p']['reverse']

        self.output_file_object = get_data_file(self.config)

    def _load(self):
        if self.f is None:
            return False

        line = get_live_symbol_data_line(self.config['data_feed']['symbol_name'])
        self.output_file_object.write(line)
        self.output_file_object.flush()
        time.sleep(30)

        if not line:
            return False

        line = line.rstrip('\n')
        linetokens = line.split(self.separator)
        return self._loadline(linetokens)
