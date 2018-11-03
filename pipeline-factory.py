from pipeline import Pipeline


class PipelineFactory(object):
    registered_modifiers = {}
    registered_filters = {}
    registered_calcs = {}
    registered_publish = {}

    """ Creates and returns a single pipeline"""

    @staticmethod
    def create_pipeline(proprties):
        modifiers_dic = proprties.get_modifiers(proprties)
        filters_dic = proprties.get_filters(proprties)
        calcs_dic = proprties.get_calcs(proprties)
        publish_dic = proprties.get_publish(proprties)

        modifiers_list = []
        filters_list = []
        calcs_list = []
        publish_list = []

        for modifier_name in modifiers_dic:
            if modifier_name in PipelineFactory.registered_modifiers:
                instanc = PipelineFactory.registered_modifiers[modifier_name](**modifiers_dic[modifier_name])
                modifiers_list.append(instanc)

        for filter_name in filters_dic:
            if filter_name in PipelineFactory.registered_filters:
                instanc = PipelineFactory.registered_filters[filter_name](**filters_dic[filter_name])
                modifiers_list.append(instanc)

        for calc_name in calcs_dic:
            if calc_name in PipelineFactory.registered_calcs:
                instanc = PipelineFactory.registered_calcs[calc_name](**calcs_dic[calc_name])
                modifiers_list.append(instanc)

        for publish_name in publish_dic:
            if publish_name in PipelineFactory.registered_publish:
                instanc = PipelineFactory.registered_publish[publish_name](**publish_dic[publish_name])
                modifiers_list.append(instanc)

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
        PipelineFactory.registered_modifiers[modifier.__name__] = modifier

    """A class decorator that registers the filter in the pipeline factory"""

    @staticmethod
    def register_filter(filterr):
        PipelineFactory.registered_filters[filter.__name__] = filterr

    """A class decorator that registers the calculation in the pipeline factory"""

    @staticmethod
    def register_calc(calc):
        PipelineFactory.registered_calcs[calc.__name__] = calc

    """A decorator that registers the publisher in the pipeline factory"""

    @staticmethod
    def register_publisher(publisher):
        PipelineFactory.registered_publish[publisher.__name__] = publisher
