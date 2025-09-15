# Controllers configuration for TLS and Plug’n’Charge
## Introduction

This document describes how to configure TLS and Plug’n’Charge (PnC) for controllers implementing ISO 15118‑2 and ISO 15118‑20. It lists the certificates and private keys that must be provisioned, and provides example configuration snippets for both EVCC and SECC.

# For ISO 15118-2

## EVCC

### Certificates

You need to provision the following certificates and keys inside `/app/certs` volume of `ccs-evcc` application:

- [The V2G Root CA](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains), in `pem` format
- The PnC contract and its associated certificate chain, in `pkcs12` format
    <!-- - This is a single file that is usually not directly provided by the PKI, and therefore you need to build it yourself with the following command:
        
        `openssl pkcs12 -export -inkey <MO_CONTRACT_PRIVATE_KEY.pem> -in <MO_CONTRACT_LEAF_CERTIFICATE.pem> -name mo_cert -certfile <INTERMEDIATE_MO_SUB_CA_CERTIFICATES.pem> -passin "pass:" -passout "pass:" -out moCertChain.p12`
        
        - `MO_CONTRACT_PRIVATE_KEY.pem`: The actual [PnC contract](charge-controllers/tls_pnc/pnc_primer.md#mobility-operator) key. If protected by a password, don’t forget to customise the `-passin` argument (see `man openssl-passphrase-options` for more details about how to provide that password in a more confidential way).
        - `MO_CONTRACT_LEAF_CERTIFICATE.pem`: The leaf certificate associated with the above private key.
        - `INTERMEDIATE_MO_SUB_CA_CERTIFCATES.pem`: A certificate chain of the 2 MO Sub CAs certificate. If the PKI provided only separate certificate files, you can build it with the following command (order matters):
            
            `cat <MO_SUB_CA2_CERTIFICATE.pem> <MO_SUB_CA1_CERTIFICATE.pem> > <INTERMEDIATE_MO_SUB_CA_CERTIFICATES.pem>`
            
        - `moCertChain.p12` is the resulting file you have to provision on the controller. -->

### Config file
This configuration can be done using the [graphical user interface](charge-controllers/advantics_os/csm-web-ui.md) or by modifying directly the following sections of the config file:

```
[ccs]
enable_iso_part2 = true
enable_pnc = true
pnc_contract_p12 = /app/certs/.../moCertChain.p12
pnc_contract_p12_passphrase = password  # Only if you provided a non-empty password in the -passout parameter when building the PKCS12 file

[tls]
enabled = true
allow_no_cert = true

[tls:client]
ca_file = /app/certs/.../V2G Root CA.pem
```

## SECC

### Certificates

You need to provision the following certificates and keys inside `/app/certs` volume of `ccs-secc`:

- [The V2G Root CA](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains), in `pem` format
- The MO Root CA, if different from the V2G Root CA
- The [CPO EVSE leaf](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains) certificate, and its associated private key, in `pem` format (but private key can also be provided in `pkcs8` format directly)
- The CPO certificate chain of the 2 CPO Sub CAs plus the Root CA (which should be the V2G Root CA)
    <!-- - If the PKI provided only separate certificate files, you can build it with the following command (order matters):
        
        `cat <CPO_SUB_CA2_CERTIFICATE.pem> <CPO_SUB_CA1_CERTIFICATE.pem> <V2G Root CA.pem> > cpoCertChain.pem` -->
        

### Config file
This configuration can be done using the [graphical user interface](charge-controllers/advantics_os/csm-web-ui.md) or by modifying directly the following sections of the config file:

```
[pistol:CCS DC]
enable_iso_part2 = true
enable_eim = false
enable_pnc = true
mo_root_ca_pem = /app/certs/.../MO Root CA.pem

[tls]
enabled = true
allow_no_cert = true

[tls:server]
ca_file = /app/certs/.../V2G Root CA.pem
server_certificate = /app/certs/.../CPO EVSE Leaf cert.pem
keyfile = /app/certs/.../CPO EVSE private key.pem
# keyfile_passphase = ...  # If the provided private key is protected by a passphrase
server_certificate_chain = /app/certs/.../cpoCertChain.pem
```

# For ISO 15118-20

## EVCC

### Certificates

You need to provision the following certificates and keys inside `/app/certs` volume of `ccs-evcc`:

- [The V2G Root CA](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains), in `pem` format
- The vehicle leaf certificate, and its associated private key, in `pem` format (but private key can also be provided in `pkcs8` format directly)
- The vehicle certificate chain of the the 2 vehicle Sub CAs plus the Root CA (which should be the V2G Root CA)
    <!-- - If the PKI provided only separate certificate files, you can build it with the following command (order matters):
        
        `cat <VEHICLE_SUB_CA2_CERTIFICATE.pem> <VEHICLE_SUB_CA1_CERTIFICATE.pem> <V2G Root CA.pem> > vehicleCertChain.pem`
         -->

<aside>
👉

**NB: PnC is not yet implement for ISO 15118-20. The MO contract would be used for that**

</aside>

### Config file
This configuration can be done using the [graphical user interface](charge-controllers/advantics_os/csm-web-ui.md) or by modifying directly the following sections of the config file:

```
[ccs]
enable_iso_part20 = true
allow_tls_1_2_for_iso_part20 = false
allow_no_tls_for_iso_part20 = false

[tls]
enabled = true
allow_no_cert = false
min_version = 1.3
max_version = 1.3

[tls:client]
ca_file = /app/certs/.../V2G Root CA.pem
server_certificate = /app/certs/.../Vehicle Leaf cert.pem
keyfile = /app/certs/.../Vehicle Leaf private key.pem
# keyfile_passphase = ...  # If the provided private key is protected by a passphrase
server_certificate_chain = vehicleCertChain.pem
```

## SECC

### Certificates

You need to provision the following certificates and keys inside `/app/certs` volume of `ccs-secc`:

- [The V2G Root CA](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains), in `pem` format
- The [CSO EVSE leaf](charge-controllers/tls_pnc/pnc_primer.md#Certificates-and-certificate-chains) certificate, and its associated private key, in `pem` format (but private key can also be provided in `pkcs8` format directly)
- The CSO certificate chain of the the 2 CSO Sub CAs plus the Root CA (which should be the V2G Root CA)
    <!-- - If the PKI provided only separate certificate files, you can build it with the following command (order matters):
        
        `cat <CSO_SUB_CA2_CERTIFICATE.pem> <CSO_SUB_CA1_CERTIFICATE.pem> <V2G Root CA.pem> > csoCertChain.pem`
         -->

<aside>
ℹ️

CSO in ISO 15118-20 is equivalent to CPO in ISO 15118-2

</aside>

### Config file
This configuration can be done using the [graphical user interface](charge-controllers/advantics_os/csm-web-ui.md) or by modifying directly the following sections of the config file:

```
[pistol:CCS DC]
enable_iso_part20 = true
allow_tls_1_2_for_iso_part20 = false
allow_no_tls_for_iso_part20 = false

[tls]
enabled = true
allow_no_cert = false
min_version = 1.3
max_version = 1.3

[tls:server]
ca_file = /app/certs/.../V2G Root CA.pem
server_certificate = /app/certs/.../CSO EVSE Leaf cert.pem
keyfile = /app/certs/.../CSO EVSE private key.pem
# keyfile_passphase = ...  # If the provided private key is protected by a passphrase
server_certificate_chain = /app/certs/.../csoCertChain.pem
```

<!-- ### Config file (flexible)

```
[pistol:CCS DC]
enable_iso_part20 = true
allow_tls_1_2_for_iso_part20 = true  # Mildly flexible
allow_no_tls_for_iso_part20 = true  # Very flexible!

[tls]
enabled = true
allow_no_cert = true
min_version = 1.2
max_version = 1.3

[tls:server]
ca_file = /app/certs/.../V2G Root CA.pem
server_certificate = /app/certs/.../CSO EVSE Leaf cert.pem
keyfile = /app/certs/.../CSO EVSE private key.pem
# keyfile_passphase = ...  # If the provided private key is protected by a passphrase
server_certificate_chain = /app/certs/.../csoCertChain.pem
``` -->
