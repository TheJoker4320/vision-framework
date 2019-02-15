from pipeline import Pipeline
import logging

from modifiers.modifier import Modifier
from extractors.extractor import Extractor
from filters.filter import Filter
from calculations.calculation import Calculation
from publishers.publish import Publish


class PipelineFactory(object):
    @staticmethod
    def modifier_registry():
        return {modifier_class.__name__: modifier_class for modifier_class in Modifier.__subclasses__()}

    @staticmethod
    def extractor_registry():
        return {extractor_class.__name__: extractor_class for extractor_class in Extractor.__subclasses__()}

    @staticmethod
    def filter_registry():
        return {filter_class.__name__: filter_class for filter_class in Filter.__subclasses__()}

    @staticmethod
    def calculation_registry():
        return {calculation_class.__name__: calculation_class for calculation_class in Calculation.__subclasses__()}

    @staticmethod
    def publisher_registry():
        return {publisher_class.__name__: publisher_class for publisher_class in Publish.__subclasses__()}

    @staticmethod
    def create_pipeline(proprties):
        """ Creates and returns a single pipeline"""
        requested_modifiers = PipelineFactory.get_modifiers(proprties)
        requested_extractors = PipelineFactory.get_extractors(proprties)
        requested_filters = PipelineFactory.get_filters(proprties)
        requested_calcs = PipelineFactory.get_calcs(proprties)
        requested_publishers = PipelineFactory.get_publish(proprties)

        modifier_list = PipelineFactory.build_list(requested_modifiers, PipelineFactory.modifier_registry())
        extractor_list = PipelineFactory.build_list(requested_extractors, PipelineFactory.extractor_registry())
        filter_list = PipelineFactory.build_list(requested_filters, PipelineFactory.filter_registry())
        calculation_list = PipelineFactory.build_list(requested_calcs, PipelineFactory.calculation_registry())
        publish_list = PipelineFactory.build_list(requested_publishers, PipelineFactory.publisher_registry())

        new_pipeline = Pipeline(modifier_list, extractor_list, filter_list, calculation_list, publish_list)
        return new_pipeline

    @staticmethod
    def get_modifiers(properties):
        """ A function that returns the list with all the modifiers"""
        modifiers_list = properties['modifiers']
        return modifiers_list

    @staticmethod
    def get_extractors(properties):
        """ A function that returns the list with all the extractors"""
        extractors_list = properties['extractors']
        return extractors_list

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
        :param dictionary: Dictionary of modifier/filter/calculation/publish
        :type dictionary: dictionary
        :param registry: Registry of modifier/filter/calculation/publish
        :type registry: dictionary
        :return: A list of the built instances from the same type that was received
        :rtype: list
        """
        return [registry[name](**properties) for name, properties in dictionary.iteritems() if
                PipelineFactory.__is_in_registry(name, registry)]

    @staticmethod
    def __is_in_registry(name, registry):
        """
        Checks if the name exists in the registry if not logs a warning
        :param name: name of modifier/filter/calculation/publish
        :type name: string
        :param registry: registry of modifier/filter/calculation/publish
        :type registry: dictionary
        :return: is the name exists in the registry
        :rtype: bool
        """
        if name in registry:
            return True

        logging.warning("{} is not registered at the registries".format(name))
        return False
