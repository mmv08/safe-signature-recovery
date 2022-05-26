from gnosis.safe.safe_signature import SafeSignature

signed_hash = "0x4a4a9d011a3a5b7e1907bbc78b68093b56199e44623faea9e4907ae1c1f22afc"
signature = "0x4ce97aada5ab174cffd630cd1734831a6b4db860288e3af4c347e779726437ef44b068202a5580785d9eb4e446583a0bd0bdf85332fac20e75c63edc0aea07e21c"

parsed_signatures = SafeSignature.parse_signature(signature, signed_hash)
for safe_signature in parsed_signatures:
    print(f"Recovered address: {safe_signature.owner}")


