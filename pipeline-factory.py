from pipeline import Pipeline


class PipelineFactory(object):
    rgst_mods = {}  # Registered modifiers
    rgst_fltrs = {}  # Registered filters
    rgst_calcs = {}  # Registered Calculations
    rgst_publish = {}  # Registered Publishers

    """ Creates and returns a single pipeline"""

    @staticmethod
    def create_pipeline(proprties):
        mod_dic = proprties.get_modifiers(proprties)  # Modifiers Dictionary
        fltr_dic = proprties.get_filters(proprties)  # Filters Dictionary
        calc_dic = proprties.get_calcs(proprties)  # Calculations Dictionary
        pub_dic = proprties.get_publish(proprties)  # Publishers Dictionary

        mods_lst = []  # Modifiers List
        fltrs_lst = []  # Filters List
        calcs_lst = []   # Calculation List
        publish_lst = []  # Publishers List

        for mod_name in mod_dic:
            if mod_name in PipelineFactory.rgst_mods:
                i = PipelineFactory.rgst_mods[mod_name](**mod_dic[mod_name])
                mods_lst.append(i)  # i stands for instance

        for flr_name in fltr_dic:
            if flr_name in PipelineFactory.rgst_fltrs:
                i = PipelineFactory.rgst_fltrs[flr_name](**fltr_dic[flr_name])
                fltrs_lst.append(i)  # i stands for instance

        for cal_name in calc_dic:
            if cal_name in PipelineFactory.rgst_calcs:
                i = PipelineFactory.rgst_calcs[cal_name](**calc_dic[cal_name])
                calcs_lst.append(i)  # i stands for instance

        for pub_name in pub_dic:
            if pub_name in PipelineFactory.rgst_publish:
                i = PipelineFactory.rgst_publish[pub_name](**pub_dic[pub_name])
                publish_lst.append(i)  # i stands for instance

        n_pipe = Pipeline(mods_lst, fltrs_lst, calcs_lst, publish_lst)
        return n_pipe

    """ A function that returns the list with all the modifiers"""

    @staticmethod
    def get_modifiers(props):
        modifiers_list = props['modifiers']
        return modifiers_list

    """ A function that returns the list with all the filters"""

    @staticmethod
    def get_filters(props):
        filters_list = props['filters']
        return filters_list

    """ A function that returns the list with all the calculations"""

    @staticmethod
    def get_calcs(props):
        calcs_list = props['calcs']
        return calcs_list

    """ A function that returns the list with all the publishers"""

    @staticmethod
    def get_publish(props):
        publish_list = props['publish']
        return publish_list

    """A class decorator that registers the modifier in the pipeline factory"""

    @staticmethod
    def register_modifier(modifier):
        PipelineFactory.rgst_mods[modifier.__name__] = modifier

    """A class decorator that registers the filter in the pipeline factory"""

    @staticmethod
    def register_filter(filterr):
        PipelineFactory.rgst_fltrs[filterr.__name__] = filterr

    """A class decorator that registers the calc in the pipeline factory"""

    @staticmethod
    def register_calc(calc):
        PipelineFactory.rgst_calcs[calc.__name__] = calc

    """A decorator that registers the publisher in the pipeline factory"""

    @staticmethod
    def register_publisher(publisher):
        PipelineFactory.rgst_publish[publisher.__name__] = publisher
