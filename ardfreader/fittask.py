# University of Illinois at Urbana-Champaign
# Illinois Informatics
# 
# ARDF file reader with concurrency
# To use in the analysis of fast force map AFM data
#
# @author: Santiago Nunez-Corrales <nunezco2@illinois.edu>

from copy import copy

from ardfreader.model import Model
from ardfreader.curve import Curve


class FittingTask:

    def __init__(self, pixel, model: Model):
        self.pixel = pixel
        self.model = copy(model)

    def __call__(self) -> Curve:
        return self.model.fit(self.pixel)

    def __str__(self):
        return f'x: {self.pixel.x}\ty: {self.pixel.y}\tw: {self.model.name()}'
