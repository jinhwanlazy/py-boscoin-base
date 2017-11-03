# encoding:utf-8
from .utils import xdr_hash

NETWORKS = {'PUBLIC': 'BOS Token Network ; October 2017',
            'TESTNET': 'Test SDF Network ; September 2015',
            'STELLAR': 'Public Global Stellar Network ; September 2015'
            }


class Network(object):
    def __init__(self, passphrase=None):
        if passphrase is None:
            self.passphrase = NETWORKS['TESTNET']
        else:
            self.passphrase = passphrase

    def network_id(self):
        return xdr_hash(self.passphrase.encode())


def test_network():
    return Network(NETWORKS['TESTNET'])


def live_network():
    return Network(NETWORKS['PUBLIC'])
