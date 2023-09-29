# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: str=None, predict: str=None):  # noqa: E501
        """Pet - a model defined in Swagger

        :param data: The data of this Pet.  # noqa: E501
        :type data: str
        :param predict: The predict of this Pet.  # noqa: E501
        :type predict: str
        """
        self.swagger_types = {
            'data': str,
            'predict': str
        }

        self.attribute_map = {
            'data': 'data',
            'predict': 'predict'
        }
        self._data = data
        self._predict = predict

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.  # noqa: E501
        :rtype: Pet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> str:
        """Gets the data of this Pet.


        :return: The data of this Pet.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this Pet.


        :param data: The data of this Pet.
        :type data: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def predict(self) -> str:
        """Gets the predict of this Pet.


        :return: The predict of this Pet.
        :rtype: str
        """
        return self._predict

    @predict.setter
    def predict(self, predict: str):
        """Sets the predict of this Pet.


        :param predict: The predict of this Pet.
        :type predict: str
        """

        self._predict = predict