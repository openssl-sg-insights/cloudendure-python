"""
    CloudEndure API documentation

    © 2021 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    The version of the OpenAPI document: 5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cloudendure
from cloudendure.model.machine_license import MachineLicense
from cloudendure.model.machine_life_cycle import MachineLifeCycle
from cloudendure.model.machine_replication_configuration import MachineReplicationConfiguration
from cloudendure.model.machine_replication_info import MachineReplicationInfo
from cloudendure.model.machine_source_properties import MachineSourceProperties
from cloudendure.model.point_in_time import PointInTime
globals()['MachineLicense'] = MachineLicense
globals()['MachineLifeCycle'] = MachineLifeCycle
globals()['MachineReplicationConfiguration'] = MachineReplicationConfiguration
globals()['MachineReplicationInfo'] = MachineReplicationInfo
globals()['MachineSourceProperties'] = MachineSourceProperties
globals()['PointInTime'] = PointInTime
from cloudendure.model.machine import Machine


class TestMachine(unittest.TestCase):
    """Machine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMachine(self):
        """Test Machine"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Machine()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
