from pipeline import Pipeline


class PipelineFactory(object):
    modifiers = {}
    filters = {}
    calcs = {}
    publish = {}

    """ Creates and returns a single pipeline"""

    @staticmethod
    def create_pipeline(proprties):
        modifiers_list = proprties.get_modifiers(proprties)
        filters_list = proprties.get_filters(proprties)
        calcs_list = proprties.get_calcs(proprties)
        publish_list = proprties.get_publish(proprties)
        new_pipeline = Pipeline(modifiers_list, filters_list, calcs_list, publish_list)
        return new_pipeline

    """ A function that returns the list with all the modifiers"""

    @staticmethod
    def get_modifiers(proprties):
        modifiers_list = proprties['modifiers']
        return modifiers_list

    """ A function that returns the list with all the filters"""

    @staticmethod
    def get_filters(proprties):
        filters_list = proprties['filters']
        return filters_list

    """ A function that returns the list with all the calculations"""

    @staticmethod
    def get_calcs(proprties):
        calcs_list = proprties['calcs']
        return calcs_list

    """ A function that returns the list with all the publishers"""

    @staticmethod
    def get_publish(proprties):
        publish_list = proprties['publish']
        return publish_list

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



