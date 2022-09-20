# Check MEV-Boost Relay Registration
Check MEV boost relay registration by executing:

```commandline
./check_mevboost_registration.py <your-validator-address>
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
