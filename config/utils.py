import requests


def get_ec2_private_ip():
    """
    Get EC2 private IP (if running on AWS EC2)
    Useful when performing SSL termination at a load balancer,
    which requires private IP to be added to ALLOWED_HOSTS to pass health checks
    Adapted from https://gist.github.com/dryan/8271687
    :return: str, ip address
    """
    ec2_private_ip = None
    try:
        ec2_private_ip = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
    except requests.exceptions.RequestException:
        pass
    return ec2_private_ip
