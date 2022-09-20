#!/usr/bin/env python3
import argparse
import json
import re
import urllib.request
from typing import Iterable, Optional
from urllib.error import HTTPError
from urllib.parse import urljoin

_REST_ENDPOINT = "/relay/v1/data/validator_registration?pubkey="

_RELAYS = {
    "boost-relay.flashbots.net",
    "bloxroute.max-profit.blxrbdn.com",
    "bloxroute.ethical.blxrbdn.com",
    "bloxroute.regulated.blxrbdn.com",
    "builder-relay-mainnet.blocknative.com",
    "relay.edennetwork.io",
}

# some user agent
_HEADERS = {"User-Agent": "Mozilla/5.0"}
_REGISTERED_MSG = "✔️ registered"
_NOT_FOUND_MSG = "❌ not found"

_ADDRESS_REGEX = re.compile(r"^0x[0-9a-f]{96}$")


def _check_registration(
    address: str,
    exit_on_non_registered: bool = False,
    relays: Optional[Iterable[str]] = None,
) -> None:
    if not _ADDRESS_REGEX.fullmatch(address.lower()):
        raise ValueError("Invalid validator address provided.")
    relay_status = {}
    endpoint = f"{_REST_ENDPOINT}{address}"
    not_registered = False
    relays = relays or _RELAYS
    for relay in relays:
        relay_status[relay] = _NOT_FOUND_MSG
        url = urljoin(f"https://{relay}", endpoint)
        try:
            req = urllib.request.Request(url=url, headers=_HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                result = response.read().decode()
        except HTTPError:
            not_registered = True
        else:
            result = json.loads(result)
            if result["message"]["pubkey"] == address:
                relay_status[relay] = _REGISTERED_MSG
            else:
                not_registered = True

    print(f"Validator '{address}'")
    for relay, status in relay_status.items():
        print(f"Relay: '{relay}', {status}")
    if exit_on_non_registered and not_registered:
        non_registered_relays = {relay for relay in relays if relay != _REGISTERED_MSG}
        exit(f"Relay registration failed for {non_registered_relays}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "validator_address",
        help="Validator address e.g. 0x0000000000000000000000000000000000000"
        "00000000000000000000000000000000000000000000000000000000000",
    )
    parser.add_argument(
        "--relays",
        nargs="*",
        type=str,
        default=None,
        required=False,
        help="Relays to check for registration e.g. bloxroute.ethical.blxrbdn.com relay.edennetwork.io",
    )
    parser.add_argument(
        "--exit-on-non-registered",
        action="store_true",
        help="Exit with exitcode 1" " when registration could not be found.",
    )
    args = parser.parse_args()
    _check_registration(
        args.validator_address, args.exit_on_non_registered, args.relays
    )

