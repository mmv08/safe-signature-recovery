from gnosis.safe.safe_signature import SafeSignature

signed_hash = "0x2f6856dbd51836973c1e61852b64949556aa2e7f253d9e20e682f9a02d436791"
signature = "0x59ad836ca5a240812273a4ca2b9c560524775e7f0edd39d85d234a6e5100dec74540f151ce663a75f39a207552b44c316b793f7bb9f967c7406af5a083f43b451b"

parsed_signatures = SafeSignature.parse_signature(signature, signed_hash)
for safe_signature in parsed_signatures:
    print(f"Recovered address: {safe_signature.owner}")


