# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_azure_file_volume_source import V1AzureFileVolumeSource


class TestV1AzureFileVolumeSource(unittest.TestCase):
    """ V1AzureFileVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1AzureFileVolumeSource(self):
        """
        Test V1AzureFileVolumeSource
        """
        model = kubernetes.client.models.v1_azure_file_volume_source.V1AzureFileVolumeSource()


if __name__ == '__main__':
    unittest.main()