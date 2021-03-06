# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CloudEndureBlueprint:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "iam_role": "str",
        "scsi_adapter_type": "str",
        "public_ip_action": "str",
        "machine_name": "str",
        "cpus": "int",
        "security_group_i_ds": "list[str]",
        "run_after_launch": "bool",
        "recommended_private_ip": "str",
        "network_interface": "str",
        "id": "str",
        "mb_ram": "int",
        "instance_type": "str",
        "subnet_i_ds": "list[str]",
        "cores_per_cpu": "int",
        "recommended_instance_type": "str",
        "static_ip": "str",
        "tags": "list[object]",
        "security_group_action": "str",
        "private_i_ps": "list[str]",
        "tenancy": "str",
        "compute_location_id": "str",
        "subnets_host_project": "str",
        "logical_location_id": "str",
        "network_adapter_type": "str",
        "byol_on_dedicated_instance": "bool",
        "placement_group": "str",
        "machine_id": "str",
        "region": "str",
        "disks": "list[object]",
        "private_ip_action": "str",
        "static_ip_action": "str",
        "dedicated_host_identifier": "str",
        "use_shared_ram": "bool",
    }

    attribute_map = {
        "iam_role": "iamRole",
        "scsi_adapter_type": "scsiAdapterType",
        "public_ip_action": "publicIPAction",
        "machine_name": "machineName",
        "cpus": "cpus",
        "security_group_i_ds": "securityGroupIDs",
        "run_after_launch": "runAfterLaunch",
        "recommended_private_ip": "recommendedPrivateIP",
        "network_interface": "networkInterface",
        "id": "id",
        "mb_ram": "mbRam",
        "instance_type": "instanceType",
        "subnet_i_ds": "subnetIDs",
        "cores_per_cpu": "coresPerCpu",
        "recommended_instance_type": "recommendedInstanceType",
        "static_ip": "staticIp",
        "tags": "tags",
        "security_group_action": "securityGroupAction",
        "private_i_ps": "privateIPs",
        "tenancy": "tenancy",
        "compute_location_id": "computeLocationId",
        "subnets_host_project": "subnetsHostProject",
        "logical_location_id": "logicalLocationId",
        "network_adapter_type": "networkAdapterType",
        "byol_on_dedicated_instance": "byolOnDedicatedInstance",
        "placement_group": "placementGroup",
        "machine_id": "machineId",
        "region": "region",
        "disks": "disks",
        "private_ip_action": "privateIPAction",
        "static_ip_action": "staticIpAction",
        "dedicated_host_identifier": "dedicatedHostIdentifier",
        "use_shared_ram": "useSharedRam",
    }

    def __init__(
        self,
        iam_role=None,
        scsi_adapter_type=None,
        public_ip_action=None,
        machine_name=None,
        cpus=None,
        security_group_i_ds=None,
        run_after_launch=None,
        recommended_private_ip=None,
        network_interface=None,
        id=None,
        mb_ram=None,
        instance_type=None,
        subnet_i_ds=None,
        cores_per_cpu=None,
        recommended_instance_type=None,
        static_ip=None,
        tags=None,
        security_group_action=None,
        private_i_ps=None,
        tenancy=None,
        compute_location_id=None,
        subnets_host_project=None,
        logical_location_id=None,
        network_adapter_type=None,
        byol_on_dedicated_instance=None,
        placement_group=None,
        machine_id=None,
        region=None,
        disks=None,
        private_ip_action=None,
        static_ip_action=None,
        dedicated_host_identifier=None,
        use_shared_ram=None,
    ):  # noqa: E501
        """CloudEndureBlueprint - a model defined in Swagger"""  # noqa: E501
        self._iam_role = None
        self._scsi_adapter_type = None
        self._public_ip_action = None
        self._machine_name = None
        self._cpus = None
        self._security_group_i_ds = None
        self._run_after_launch = None
        self._recommended_private_ip = None
        self._network_interface = None
        self._id = None
        self._mb_ram = None
        self._instance_type = None
        self._subnet_i_ds = None
        self._cores_per_cpu = None
        self._recommended_instance_type = None
        self._static_ip = None
        self._tags = None
        self._security_group_action = None
        self._private_i_ps = None
        self._tenancy = None
        self._compute_location_id = None
        self._subnets_host_project = None
        self._logical_location_id = None
        self._network_adapter_type = None
        self._byol_on_dedicated_instance = None
        self._placement_group = None
        self._machine_id = None
        self._region = None
        self._disks = None
        self._private_ip_action = None
        self._static_ip_action = None
        self._dedicated_host_identifier = None
        self._use_shared_ram = None
        self.discriminator = None
        if iam_role is not None:
            self.iam_role = iam_role
        if scsi_adapter_type is not None:
            self.scsi_adapter_type = scsi_adapter_type
        if public_ip_action is not None:
            self.public_ip_action = public_ip_action
        if machine_name is not None:
            self.machine_name = machine_name
        if cpus is not None:
            self.cpus = cpus
        if security_group_i_ds is not None:
            self.security_group_i_ds = security_group_i_ds
        if run_after_launch is not None:
            self.run_after_launch = run_after_launch
        if recommended_private_ip is not None:
            self.recommended_private_ip = recommended_private_ip
        if network_interface is not None:
            self.network_interface = network_interface
        if id is not None:
            self.id = id
        if mb_ram is not None:
            self.mb_ram = mb_ram
        if instance_type is not None:
            self.instance_type = instance_type
        if subnet_i_ds is not None:
            self.subnet_i_ds = subnet_i_ds
        if cores_per_cpu is not None:
            self.cores_per_cpu = cores_per_cpu
        if recommended_instance_type is not None:
            self.recommended_instance_type = recommended_instance_type
        if static_ip is not None:
            self.static_ip = static_ip
        if tags is not None:
            self.tags = tags
        if security_group_action is not None:
            self.security_group_action = security_group_action
        if private_i_ps is not None:
            self.private_i_ps = private_i_ps
        if tenancy is not None:
            self.tenancy = tenancy
        if compute_location_id is not None:
            self.compute_location_id = compute_location_id
        if subnets_host_project is not None:
            self.subnets_host_project = subnets_host_project
        if logical_location_id is not None:
            self.logical_location_id = logical_location_id
        if network_adapter_type is not None:
            self.network_adapter_type = network_adapter_type
        if byol_on_dedicated_instance is not None:
            self.byol_on_dedicated_instance = byol_on_dedicated_instance
        if placement_group is not None:
            self.placement_group = placement_group
        if machine_id is not None:
            self.machine_id = machine_id
        if region is not None:
            self.region = region
        if disks is not None:
            self.disks = disks
        if private_ip_action is not None:
            self.private_ip_action = private_ip_action
        if static_ip_action is not None:
            self.static_ip_action = static_ip_action
        if dedicated_host_identifier is not None:
            self.dedicated_host_identifier = dedicated_host_identifier
        if use_shared_ram is not None:
            self.use_shared_ram = use_shared_ram

    @property
    def iam_role(self):
        """Gets the iam_role of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The iam_role of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._iam_role

    @iam_role.setter
    def iam_role(self, iam_role):
        """Sets the iam_role of this CloudEndureBlueprint.

        AWS only. Possible values can be fetched from the Region object.  # noqa: E501

        :param iam_role: The iam_role of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._iam_role = iam_role

    @property
    def scsi_adapter_type(self):
        """Gets the scsi_adapter_type of this CloudEndureBlueprint.  # noqa: E501

        Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The scsi_adapter_type of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._scsi_adapter_type

    @scsi_adapter_type.setter
    def scsi_adapter_type(self, scsi_adapter_type):
        """Sets the scsi_adapter_type of this CloudEndureBlueprint.

        Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object.  # noqa: E501

        :param scsi_adapter_type: The scsi_adapter_type of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._scsi_adapter_type = scsi_adapter_type

    @property
    def public_ip_action(self):
        """Gets the public_ip_action of this CloudEndureBlueprint.  # noqa: E501

        Whether to allocate an ephemeral public IP, or not. AS_SUBNET causes CloudEndure to copy this property from the source machine.  # noqa: E501

        :return: The public_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_action

    @public_ip_action.setter
    def public_ip_action(self, public_ip_action):
        """Sets the public_ip_action of this CloudEndureBlueprint.

        Whether to allocate an ephemeral public IP, or not. AS_SUBNET causes CloudEndure to copy this property from the source machine.  # noqa: E501

        :param public_ip_action: The public_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOCATE", "DONT_ALLOCATE", "AS_SUBNET"]  # noqa: E501
        if public_ip_action not in allowed_values:
            raise ValueError(
                "Invalid value for `public_ip_action` ({0}), must be one of {1}".format(  # noqa: E501
                    public_ip_action, allowed_values
                )
            )

        self._public_ip_action = public_ip_action

    @property
    def machine_name(self):
        """Gets the machine_name of this CloudEndureBlueprint.  # noqa: E501


        :return: The machine_name of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this CloudEndureBlueprint.


        :param machine_name: The machine_name of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._machine_name = machine_name

    @property
    def cpus(self):
        """Gets the cpus of this CloudEndureBlueprint.  # noqa: E501

        Number of CPUs per per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxCpusPerMachine property of the Region object.   # noqa: E501

        :return: The cpus of this CloudEndureBlueprint.  # noqa: E501
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this CloudEndureBlueprint.

        Number of CPUs per per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxCpusPerMachine property of the Region object.   # noqa: E501

        :param cpus: The cpus of this CloudEndureBlueprint.  # noqa: E501
        :type: int
        """

        self._cpus = cpus

    @property
    def security_group_i_ds(self):
        """Gets the security_group_i_ds of this CloudEndureBlueprint.  # noqa: E501

        AWS only. The security groups that will be applied to the target machine. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The security_group_i_ds of this CloudEndureBlueprint.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_i_ds

    @security_group_i_ds.setter
    def security_group_i_ds(self, security_group_i_ds):
        """Sets the security_group_i_ds of this CloudEndureBlueprint.

        AWS only. The security groups that will be applied to the target machine. Possible values can be fetched from the Region object.  # noqa: E501

        :param security_group_i_ds: The security_group_i_ds of this CloudEndureBlueprint.  # noqa: E501
        :type: list[str]
        """

        self._security_group_i_ds = security_group_i_ds

    @property
    def run_after_launch(self):
        """Gets the run_after_launch of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Whether to power on the launched target machine after launch. True by default.  # noqa: E501

        :return: The run_after_launch of this CloudEndureBlueprint.  # noqa: E501
        :rtype: bool
        """
        return self._run_after_launch

    @run_after_launch.setter
    def run_after_launch(self, run_after_launch):
        """Sets the run_after_launch of this CloudEndureBlueprint.

        AWS only. Whether to power on the launched target machine after launch. True by default.  # noqa: E501

        :param run_after_launch: The run_after_launch of this CloudEndureBlueprint.  # noqa: E501
        :type: bool
        """

        self._run_after_launch = run_after_launch

    @property
    def recommended_private_ip(self):
        """Gets the recommended_private_ip of this CloudEndureBlueprint.  # noqa: E501

        The private IP address recommended for use with this machine.  # noqa: E501

        :return: The recommended_private_ip of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._recommended_private_ip

    @recommended_private_ip.setter
    def recommended_private_ip(self, recommended_private_ip):
        """Sets the recommended_private_ip of this CloudEndureBlueprint.

        The private IP address recommended for use with this machine.  # noqa: E501

        :param recommended_private_ip: The recommended_private_ip of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._recommended_private_ip = recommended_private_ip

    @property
    def network_interface(self):
        """Gets the network_interface of this CloudEndureBlueprint.  # noqa: E501


        :return: The network_interface of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._network_interface

    @network_interface.setter
    def network_interface(self, network_interface):
        """Sets the network_interface of this CloudEndureBlueprint.


        :param network_interface: The network_interface of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._network_interface = network_interface

    @property
    def id(self):
        """Gets the id of this CloudEndureBlueprint.  # noqa: E501


        :return: The id of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureBlueprint.


        :param id: The id of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mb_ram(self):
        """Gets the mb_ram of this CloudEndureBlueprint.  # noqa: E501

        MB RAM per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxMbRamPerMachine property of the Region object.   # noqa: E501

        :return: The mb_ram of this CloudEndureBlueprint.  # noqa: E501
        :rtype: int
        """
        return self._mb_ram

    @mb_ram.setter
    def mb_ram(self, mb_ram):
        """Sets the mb_ram of this CloudEndureBlueprint.

        MB RAM per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxMbRamPerMachine property of the Region object.   # noqa: E501

        :param mb_ram: The mb_ram of this CloudEndureBlueprint.  # noqa: E501
        :type: int
        """

        self._mb_ram = mb_ram

    @property
    def instance_type(self):
        """Gets the instance_type of this CloudEndureBlueprint.  # noqa: E501

        Possible values can be fetched from the Region object, plus special values \"COPY_ORIGIN\" or \"CUSTOM\"  # noqa: E501

        :return: The instance_type of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CloudEndureBlueprint.

        Possible values can be fetched from the Region object, plus special values \"COPY_ORIGIN\" or \"CUSTOM\"  # noqa: E501

        :param instance_type: The instance_type of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def subnet_i_ds(self):
        """Gets the subnet_i_ds of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Configures a subnets in which the instance network interface will take part. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The subnet_i_ds of this CloudEndureBlueprint.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_i_ds

    @subnet_i_ds.setter
    def subnet_i_ds(self, subnet_i_ds):
        """Sets the subnet_i_ds of this CloudEndureBlueprint.

        AWS only. Configures a subnets in which the instance network interface will take part. Possible values can be fetched from the Region object.  # noqa: E501

        :param subnet_i_ds: The subnet_i_ds of this CloudEndureBlueprint.  # noqa: E501
        :type: list[str]
        """

        self._subnet_i_ds = subnet_i_ds

    @property
    def cores_per_cpu(self):
        """Gets the cores_per_cpu of this CloudEndureBlueprint.  # noqa: E501

        Number of CPU cores per CPU in Target machine; Currently relevant for vCenter cloud only.  # noqa: E501

        :return: The cores_per_cpu of this CloudEndureBlueprint.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_cpu

    @cores_per_cpu.setter
    def cores_per_cpu(self, cores_per_cpu):
        """Sets the cores_per_cpu of this CloudEndureBlueprint.

        Number of CPU cores per CPU in Target machine; Currently relevant for vCenter cloud only.  # noqa: E501

        :param cores_per_cpu: The cores_per_cpu of this CloudEndureBlueprint.  # noqa: E501
        :type: int
        """

        self._cores_per_cpu = cores_per_cpu

    @property
    def recommended_instance_type(self):
        """Gets the recommended_instance_type of this CloudEndureBlueprint.  # noqa: E501

        When instance rightsizing is enabled, the instance type suitable for the source machine's HW  # noqa: E501

        :return: The recommended_instance_type of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._recommended_instance_type

    @recommended_instance_type.setter
    def recommended_instance_type(self, recommended_instance_type):
        """Sets the recommended_instance_type of this CloudEndureBlueprint.

        When instance rightsizing is enabled, the instance type suitable for the source machine's HW  # noqa: E501

        :param recommended_instance_type: The recommended_instance_type of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._recommended_instance_type = recommended_instance_type

    @property
    def static_ip(self):
        """Gets the static_ip of this CloudEndureBlueprint.  # noqa: E501

        Possible values can be fetched from the Region object.  # noqa: E501

        :return: The static_ip of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        """Sets the static_ip of this CloudEndureBlueprint.

        Possible values can be fetched from the Region object.  # noqa: E501

        :param static_ip: The static_ip of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._static_ip = static_ip

    @property
    def tags(self):
        """Gets the tags of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Tags that will be applied to the target machine.  # noqa: E501

        :return: The tags of this CloudEndureBlueprint.  # noqa: E501
        :rtype: list[object]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudEndureBlueprint.

        AWS only. Tags that will be applied to the target machine.  # noqa: E501

        :param tags: The tags of this CloudEndureBlueprint.  # noqa: E501
        :type: list[object]
        """

        self._tags = tags

    @property
    def security_group_action(self):
        """Gets the security_group_action of this CloudEndureBlueprint.  # noqa: E501

        How to assign a security group to the target machine.  # noqa: E501

        :return: The security_group_action of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._security_group_action

    @security_group_action.setter
    def security_group_action(self, security_group_action):
        """Sets the security_group_action of this CloudEndureBlueprint.

        How to assign a security group to the target machine.  # noqa: E501

        :param security_group_action: The security_group_action of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM_POLICY"]  # noqa: E501
        if security_group_action not in allowed_values:
            raise ValueError(
                "Invalid value for `security_group_action` ({0}), must be one of {1}".format(  # noqa: E501
                    security_group_action, allowed_values
                )
            )

        self._security_group_action = security_group_action

    @property
    def private_i_ps(self):
        """Gets the private_i_ps of this CloudEndureBlueprint.  # noqa: E501


        :return: The private_i_ps of this CloudEndureBlueprint.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_i_ps

    @private_i_ps.setter
    def private_i_ps(self, private_i_ps):
        """Sets the private_i_ps of this CloudEndureBlueprint.


        :param private_i_ps: The private_i_ps of this CloudEndureBlueprint.  # noqa: E501
        :type: list[str]
        """

        self._private_i_ps = private_i_ps

    @property
    def tenancy(self):
        """Gets the tenancy of this CloudEndureBlueprint.  # noqa: E501


        :return: The tenancy of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this CloudEndureBlueprint.


        :param tenancy: The tenancy of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """
        allowed_values = ["SHARED", "DEDICATED", "HOST"]  # noqa: E501
        if tenancy not in allowed_values:
            raise ValueError(
                "Invalid value for `tenancy` ({0}), must be one of {1}".format(  # noqa: E501
                    tenancy, allowed_values
                )
            )

        self._tenancy = tenancy

    @property
    def compute_location_id(self):
        """Gets the compute_location_id of this CloudEndureBlueprint.  # noqa: E501

        todo  # noqa: E501

        :return: The compute_location_id of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._compute_location_id

    @compute_location_id.setter
    def compute_location_id(self, compute_location_id):
        """Sets the compute_location_id of this CloudEndureBlueprint.

        todo  # noqa: E501

        :param compute_location_id: The compute_location_id of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._compute_location_id = compute_location_id

    @property
    def subnets_host_project(self):
        """Gets the subnets_host_project of this CloudEndureBlueprint.  # noqa: E501

        GCP only. Host project for cross project network subnet.  # noqa: E501

        :return: The subnets_host_project of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._subnets_host_project

    @subnets_host_project.setter
    def subnets_host_project(self, subnets_host_project):
        """Sets the subnets_host_project of this CloudEndureBlueprint.

        GCP only. Host project for cross project network subnet.  # noqa: E501

        :param subnets_host_project: The subnets_host_project of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._subnets_host_project = subnets_host_project

    @property
    def logical_location_id(self):
        """Gets the logical_location_id of this CloudEndureBlueprint.  # noqa: E501

        vcenter = vmFolder; relates to $ref LogicalLocation  # noqa: E501

        :return: The logical_location_id of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._logical_location_id

    @logical_location_id.setter
    def logical_location_id(self, logical_location_id):
        """Sets the logical_location_id of this CloudEndureBlueprint.

        vcenter = vmFolder; relates to $ref LogicalLocation  # noqa: E501

        :param logical_location_id: The logical_location_id of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._logical_location_id = logical_location_id

    @property
    def network_adapter_type(self):
        """Gets the network_adapter_type of this CloudEndureBlueprint.  # noqa: E501

        Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The network_adapter_type of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._network_adapter_type

    @network_adapter_type.setter
    def network_adapter_type(self, network_adapter_type):
        """Sets the network_adapter_type of this CloudEndureBlueprint.

        Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object.  # noqa: E501

        :param network_adapter_type: The network_adapter_type of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._network_adapter_type = network_adapter_type

    @property
    def byol_on_dedicated_instance(self):
        """Gets the byol_on_dedicated_instance of this CloudEndureBlueprint.  # noqa: E501

        specifies whether to use byol windows license if dedicated instance tenancy is selected.  # noqa: E501

        :return: The byol_on_dedicated_instance of this CloudEndureBlueprint.  # noqa: E501
        :rtype: bool
        """
        return self._byol_on_dedicated_instance

    @byol_on_dedicated_instance.setter
    def byol_on_dedicated_instance(self, byol_on_dedicated_instance):
        """Sets the byol_on_dedicated_instance of this CloudEndureBlueprint.

        specifies whether to use byol windows license if dedicated instance tenancy is selected.  # noqa: E501

        :param byol_on_dedicated_instance: The byol_on_dedicated_instance of this CloudEndureBlueprint.  # noqa: E501
        :type: bool
        """

        self._byol_on_dedicated_instance = byol_on_dedicated_instance

    @property
    def placement_group(self):
        """Gets the placement_group of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The placement_group of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this CloudEndureBlueprint.

        AWS only. Possible values can be fetched from the Region object.  # noqa: E501

        :param placement_group: The placement_group of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._placement_group = placement_group

    @property
    def machine_id(self):
        """Gets the machine_id of this CloudEndureBlueprint.  # noqa: E501


        :return: The machine_id of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this CloudEndureBlueprint.


        :param machine_id: The machine_id of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._machine_id = machine_id

    @property
    def region(self):
        """Gets the region of this CloudEndureBlueprint.  # noqa: E501


        :return: The region of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudEndureBlueprint.


        :param region: The region of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def disks(self):
        """Gets the disks of this CloudEndureBlueprint.  # noqa: E501

        AWS only. Target machine disk properties.  # noqa: E501

        :return: The disks of this CloudEndureBlueprint.  # noqa: E501
        :rtype: list[object]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this CloudEndureBlueprint.

        AWS only. Target machine disk properties.  # noqa: E501

        :param disks: The disks of this CloudEndureBlueprint.  # noqa: E501
        :type: list[object]
        """

        self._disks = disks

    @property
    def private_ip_action(self):
        """Gets the private_ip_action of this CloudEndureBlueprint.  # noqa: E501


        :return: The private_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._private_ip_action

    @private_ip_action.setter
    def private_ip_action(self, private_ip_action):
        """Sets the private_ip_action of this CloudEndureBlueprint.


        :param private_ip_action: The private_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "CREATE_NEW",
            "COPY_ORIGIN",
            "CUSTOM_IP",
            "USE_NETWORK_INTERFACE",
        ]  # noqa: E501
        if private_ip_action not in allowed_values:
            raise ValueError(
                "Invalid value for `private_ip_action` ({0}), must be one of {1}".format(  # noqa: E501
                    private_ip_action, allowed_values
                )
            )

        self._private_ip_action = private_ip_action

    @property
    def static_ip_action(self):
        """Gets the static_ip_action of this CloudEndureBlueprint.  # noqa: E501


        :return: The static_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._static_ip_action

    @static_ip_action.setter
    def static_ip_action(self, static_ip_action):
        """Sets the static_ip_action of this CloudEndureBlueprint.


        :param static_ip_action: The static_ip_action of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "EXISTING",
            "DONT_CREATE",
            "CREATE_NEW",
            "IF_IN_ORIGIN",
        ]  # noqa: E501
        if static_ip_action not in allowed_values:
            raise ValueError(
                "Invalid value for `static_ip_action` ({0}), must be one of {1}".format(  # noqa: E501
                    static_ip_action, allowed_values
                )
            )

        self._static_ip_action = static_ip_action

    @property
    def dedicated_host_identifier(self):
        """Gets the dedicated_host_identifier of this CloudEndureBlueprint.  # noqa: E501


        :return: The dedicated_host_identifier of this CloudEndureBlueprint.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_identifier

    @dedicated_host_identifier.setter
    def dedicated_host_identifier(self, dedicated_host_identifier):
        """Sets the dedicated_host_identifier of this CloudEndureBlueprint.


        :param dedicated_host_identifier: The dedicated_host_identifier of this CloudEndureBlueprint.  # noqa: E501
        :type: str
        """

        self._dedicated_host_identifier = dedicated_host_identifier

    @property
    def use_shared_ram(self):
        """Gets the use_shared_ram of this CloudEndureBlueprint.  # noqa: E501

        todo  # noqa: E501

        :return: The use_shared_ram of this CloudEndureBlueprint.  # noqa: E501
        :rtype: bool
        """
        return self._use_shared_ram

    @use_shared_ram.setter
    def use_shared_ram(self, use_shared_ram):
        """Sets the use_shared_ram of this CloudEndureBlueprint.

        todo  # noqa: E501

        :param use_shared_ram: The use_shared_ram of this CloudEndureBlueprint.  # noqa: E501
        :type: bool
        """

        self._use_shared_ram = use_shared_ram

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CloudEndureBlueprint, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudEndureBlueprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
