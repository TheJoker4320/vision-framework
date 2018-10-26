import cv2


class PipelineFactory(object):
    modifiers = {}
    filters = {}
    calcs = {}
    publish = {}

    """ wip """
    def get_modifiers(self, proprties):
        self.modifiers = proprties['modifiers']

    """ wip """
    def get_filters(self, proprties):
        self.modifiers = proprties['filters']

    """ wip """
    def get_calcs(self, proprties):
        self.modifiers = proprties['calcs']

    """ wip """
    def get_publish(self, proprties):
        self.modifiers = proprties['publish']

    """A class decorator that registers the modifier in the pipeline factory"""
    @staticmethod
    def register_modifier(modifier):
        PipelineFactory.modifiers[modifier.__name__] = modifier

    """A class decorator that registers the filter in the pipeline factory"""
    @staticmethod
    def register_filter(filter):
        PipelineFactory.modifiers[filter.__name__] = filter

    """A class decorator that registers the calculation in the pipeline factory"""
    @staticmethod
    def register_calc(calc):
        PipelineFactory.modifiers[calc.__name__] = calc

    """A decorator that registers the publisher in the pipeline factory"""
    @staticmethod
    def register_publisher(publisher):
        PipelineFactory.modifiers[publisher.__name__] = publisher
