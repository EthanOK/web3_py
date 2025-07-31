from web3_py.utils.beacon_proxy import get_beacon_proxy_implementation


def main():
    beaco_proxy_address = "0x7436750e80bB956C6488A879D573cA417D6712A2"
    implementation = get_beacon_proxy_implementation(beaco_proxy_address)
    print(f"Implementation地址: {implementation}")


if __name__ == "__main__":
    main()
