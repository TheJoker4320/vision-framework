from pipeline import Pipeline
import logging

from modifiers.modifier import Modifier
from filters.filter import Filter
from calculations.calculation import Calculation
from publishers.publish import Publish


class PipelineFactory(object):
    @staticmethod
    def modifier_registry():
        return {modifier_class.__name__: modifier_class for modifier_class in Modifier.__subclasses__()}

    @staticmethod
    def filter_registry():
        return {filter_class.__name__: filter_class for filter_class in Filter.__subclasses__()}

    @staticmethod
    def calculation_registry():
        return {calculation_class.__name__: calculation_class for calculation_class in Calculation.__subclasses__()}

    @staticmethod
    def publisher_registry():
        return {publisher_class.__name__: publisher_class for publisher_class in Publish.__subclasses__()}

    """ Creates and returns a single pipeline"""

    @staticmethod
    def create_pipeline(proprties):
        modifier_dict = PipelineFactory.get_modifiers(proprties)
        filter_dict = PipelineFactory.get_filters(proprties)
        calculation_dict = PipelineFactory.get_calcs(proprties)
        publish_dict = PipelineFactory.get_publish(proprties)

        modifier_list = PipelineFactory.build_list(modifier_dict, PipelineFactory.modifier_registry())
        filter_list = PipelineFactory.build_list(filter_dict, PipelineFactory.filter_registry())
        calculation_list = PipelineFactory.build_list(calculation_dict, PipelineFactory.calculation_registry())
        publish_list = PipelineFactory.build_list(publish_dict, PipelineFactory.publisher_registry())

        new_pipeline = Pipeline(modifier_list, filter_list, calculation_list, publish_list)
        return new_pipeline

    @staticmethod
    def get_modifiers(properties):
        """ A function that returns the list with all the modifiers"""
        modifiers_list = properties['modifiers']
        return modifiers_list

    @staticmethod
    def get_filters(properties):
        """ A function that returns the list with all the filters"""
        filters_list = properties['filters']
        return filters_list

    @staticmethod
    def get_calcs(properties):
        """ A function that returns the list with all the calculations"""
        calcs_list = properties['calculations']
        return calcs_list

    @staticmethod
    def get_publish(properties):
        """ A function that returns the list with all the publishers"""
        publish_list = properties['publishers']
        return publish_list

    @staticmethod
    def build_list(dictionary, registry):
        """

        :param dictionary: dictionary of modifier/filter/calculation/publish
        :type dictionary: dictionary
        :param registry: registry of modifier/filter/calculation/publish
        :type registry: dictionary
        :return: list of build instances from the same type that was recieved
        :rtype: list
        """
        return [registry[name](**properties) for name, properties in dictionary.iteritems() if
                PipelineFactory.__in_registry(name, registry)]

    @staticmethod
    def __in_registry(name, registry):
        """
        checks if the name exists in the registery
        if not logs a warning

        :param name: name of modifier/filter/calculation/publish
        :type name: string
        :param registry: registery of modifier/filter/calculation/publish
        :type registry: dictionary
        :return: is the name exists in the registery
        :rtype: bool
        """
        if name in registry:
            return True

        logging.warning("{} is not registered at the registries".format(name))
        return False
