# -*- coding: utf-8 -*-
"""Define the CloudEndure reusable variables."""

from typing import Dict


def get_aws_regions() -> Dict[str, str]:
    """Return a hardcoded dictionary of AWS regions.

    Returns:
        dict: A mapping of AWS regions.

    """
    return {
        "US East (Ohio)": "us-east-2",
        "US East (N. Virginia)": "us-east-1",
        "US West (N. California)": "us-west-1",
        "US West (Oregon)": "us-west-2",
        "Asia Pacific (Hong Kong)": "ap-east-1",
        "Asia Pacific (Mumbai)": "ap-south-1",
        "Asia Pacific (Osaka-Local)": "ap-northeast-3",
        "Asia Pacific (Seoul)": "ap-northeast-2",
        "Asia Pacific (Singapore)": "ap-southeast-1",
        "Asia Pacific (Sydney)": "ap-southeast-2",
        "Asia Pacific (Tokyo)": "ap-northeast-1",
        "Canada (Central)": "ca-central-1",
        "China (Beijing)": "cn-north-1",
        "China (Ningxia)": "cn-northwest-1",
        "EU (Frankfurt)": "eu-central-1",
        "EU (Ireland)": "eu-west-1",
        "EU (London)": "eu-west-2",
        "EU (Paris)": "eu-west-3",
        "EU (Stockholm)": "eu-north-1",
        "Middle East (Bahrain)": "me-south-1",
        "South America (Sao Paulo)": "sa-east-1",
        "AWS GovCloud (US-East)": "us-gov-east-1",
        "AWS GovCloud (US-West)": "us-gov-west-1",
    }
