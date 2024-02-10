# Check MEV-Boost Relay Registration
Check MEV boost relay registration by executing:

```commandline
./check_mevboost_registration.py <your-validator-address>
```
e.g
```commandline
./check_mevboost_registration.py 0x8000a44457e18388c5be046e22e86aedae1a07638394df63adfcd32d29b4e86c030219e94782ebebe398c9a05a8a28e7

Validator '0x8000a44457e18388c5be046e22e86aedae1a07638394df63adfcd32d29b4e86c030219e94782ebebe398c9a05a8a28e7'
Relay: 'boost-relay.flashbots.net', ✔️ registered
Relay: 'bloxroute.max-profit.blxrbdn.com', ❌ not found
Relay: 'bloxroute.regulated.blxrbdn.com', ❌ not found
Relay: 'builder-relay-mainnet.blocknative.com', ❌ not found
Relay: 'relay.edennetwork.io', ❌ not found
Relay: 'mainnet-relay.securerpc.com', ❌ not found
Relay: 'relay.ultrasound.money', ✔️ registered
Relay: 'agnostic-relay.net', ✔️ registered
Relay: 'aestus.live', ✔️ registered
Relay: 'relay.wenmerge.com', ❌ not found
Relay: 'proof-relay.ponrelay.com', ❌ not found
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
  --json                Output relay registration status as json
```
