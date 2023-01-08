# Check MEV-Boost Relay Registration
Check MEV boost relay registration by executing:

```commandline
./check_mevboost_registration.py <your-validator-address>
```
e.g
```commandline
./check_mevboost_registration.py 0x8000a44457e18388c5be046e22e86aedae1a07638394df63adfcd32d29b4e86c030219e94782ebebe398c9a05a8a28e7

Validator '0x8000a44457e18388c5be046e22e86aedae1a07638394df63adfcd32d29b4e86c030219e94782ebebe398c9a05a8a28e7'
Relay: 'bloxroute.ethical.blxrbdn.com', ❌ not found
Relay: 'relay.edennetwork.io', ❌ not found
Relay: 'builder-relay-mainnet.blocknative.com', ✔️ registered
Relay: 'bloxroute.max-profit.blxrbdn.com', ✔️ registered
Relay: 'boost-relay.flashbots.net', ✔️ registered
Relay: 'bloxroute.regulated.blxrbdn.com', ❌ not found
Relay: 'builder-relay-mainnet.blocknative.com', ✔️ registered
Relay: 'relay.edennetwork.io', ❌ not found
Relay: 'mainnet-relay.securerpc.com', ✔️ registered
Relay: 'relayooor.wtf', ✔️ registered
Relay: 'relay.ultrasound.money', ✔️ registered
Relay: 'agnostic-relay.net', ✔️ registered
```

## Advanced Usage

```commandline
usage: check_mevboost_registration.py [-h] [--relays [RELAYS [RELAYS ...]]] [--exit-on-non-registered] validator_address

positional arguments:
  validator_address     Validator address e.g. 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

optional arguments:
  -h, --help            show this help message and exit
  --relays [RELAYS [RELAYS ...]]
                        Relays to check for registration e.g. bloxroute.ethical.blxrbdn.com relay.edennetwork.io
  --exit-on-non-registered
                        Exit with exitcode 1 when registration could not be found.
```
