from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from model import *
import warnings
import time

warnings.filterwarnings("ignore")


encoder, decoder, voc, pairs, embedding = initGenModel()
encoder.eval()
decoder.eval()

searcher = GreedySearchDecoder(encoder, decoder)
def answer(str):
    time.sleep(1)
    res = generateAnswer(str, searcher, voc)
    return res
# Initialize search module
