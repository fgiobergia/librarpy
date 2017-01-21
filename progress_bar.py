import sys

class ProgressBar:
    def __init__(self, value, scale, **kwargs):
        self.value = value
        self.scale = scale

        # some default values here
        self.primary = kwargs['primary'] if 'primary' in kwargs else u'\u2588'
        self.secondary = kwargs['secondary'] if 'secondary' in kwargs else ' '
        self.length = kwargs['length'] if 'length' in kwargs else 20

        self.percentage = int(float(self.value) / self.scale * 100)

    def show(self, custom_message=''):
        bar_len = int(self.length * float(self.value) / self.scale)

        print u'{} {:>5}% [{bar}{bg}] {read}/{tot}'.format( \
                                                 custom_message, \
                                                 self.percentage, \
                                                 bar=self.primary * bar_len, \
                                                 bg=self.secondary * (self.length - bar_len), \
                                                 read=self.value, \
                                                 tot=self.scale)
