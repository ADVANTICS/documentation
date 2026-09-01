# TLS

A vehicle-side charge controller is the TLS **client**. This page applies to both vehicle
controllers — the ADM-CS-EVCC for CCS and the ADM-CS-MEVC for MCS — because they share the same TLS
implementation and the same configuration entries.

## When TLS is needed

| Protocol | TLS |
|---|---|
| **ISO 15118-20** — the only protocol an MCS session runs, and optional on CCS | **Required** by the standard, with TLS 1.3 |
| **ISO 15118-2** — CCS | Only for **Plug & Charge**. An EIM session does not use it |
| **DIN 70121** — CCS | Not used |

!!! warning "The controller ships with TLS disabled"
    Out of the box `[tls] enabled = false`, and the entries that tolerate a session without TLS are
    all set. This is deliberate: it lets you charge against the chargers that exist today, most of
    which do not offer TLS. Turning TLS on is something you do on purpose, once you have a PKI and a
    charger to test against — see [Enabling TLS](#enabling-tls).

Configuration is split across two sections, plus two entries in `[ccs]`:

| Section | Holds |
|---|---|
| `[tls]` | Whether TLS is used, and whether the charger's certificate is verified |
| `[tls:client]` | The certificate and key files, and the TLS version window |
| `[ccs]` | How tolerant the ISO 15118-20 stack is when TLS is *not* in use, and the Plug & Charge contract |

!!! note "Sub-sections are separated by a colon"
    `[tls:client]` is a *sub-section* of `[tls]`, not a section called `tls:client`. Write it exactly
    as shown.

!!! warning "A misspelled entry is silently ignored"
    The configuration is loaded non-strictly: an option the controller does not recognise is skipped
    without any error or log line, and the built-in default applies instead. If a setting appears to
    have no effect, check the spelling and the section before anything else. In particular,
    `min_version` and `max_version` belong in `[tls:client]` — placed directly under `[tls]` they do
    nothing.

## What ships on the controller

<figcaption>Relevant part of the default <code>config.cfg</code></figcaption>

    [ccs]
    allow_tls_1_2_for_iso_part20 = true
    allow_no_tls_for_iso_part20 = true

    [tls]
    enabled = false
    allow_no_cert = true
    allow_iso_20_without_tls = true

There is no `[tls:client]` section in the shipped file — the built-in file paths apply, and nothing
reads them while `enabled` is `false`.

## Enabling TLS

### 1. Provision the certificates

Copy the certificates onto the controller, into the directory that is bind-mounted into the
`ccs-evcc` container as `/app/certs`. Where that directory is
depends on which system the controller runs:

<div class="small-table compact-table" markdown="1">

| Controller | Directory on the controller |
|---|---|
| **ADM-CS-EVCC** | `/srv/certs` |
| **ADM-CS-MEVC** | `certs` under the Docker Compose profile in use — by default `/etc/advantics/default/certs` |

</div>

!!! note "The paths in the configuration file stay `/app/certs/...`"
    `config.cfg` is read by the application *inside* the container, so `ca_file`, `keyfile`,
    `client_certificate` and `client_certificate_chain` must all use the container path
    `/app/certs/<file>` — not the directory you copied the files into. The bind mount is what
    connects the two.

Provide these files:

- The **V2G Root CA**, in `pem` format.
- The **vehicle leaf certificate** and its **private key**, in `pem` format.
- The **vehicle certificate chain** — the two vehicle Sub CAs followed by the Root CA, which should
  be the V2G Root CA.

!!! warning "Everything must be PEM, including the key"
    All four files are loaded as PEM and nothing else is accepted — a DER or otherwise binary file
    will fail to load. For the private key, either PEM block type works: the traditional
    `-----BEGIN RSA PRIVATE KEY-----` / `-----BEGIN EC PRIVATE KEY-----`, or the PKCS#8
    `-----BEGIN PRIVATE KEY-----`. Convert a binary key first:

        openssl pkey -in key.der -inform DER -out key.pem -outform PEM

Order matters when building the chain from separate files:

    cat <VEHICLE_SUB_CA2.pem> <VEHICLE_SUB_CA1.pem> <V2G Root CA.pem> > vehicleCertChain.pem

### 2. Point the configuration at them

<figcaption>Standard-compliant ISO 15118-20 vehicle</figcaption>

    [ccs]
    allow_tls_1_2_for_iso_part20 = false
    allow_no_tls_for_iso_part20 = false

    [tls]
    enabled = true
    allow_no_cert = false
    allow_iso_20_without_tls = false

    [tls:client]
    ca_file = /app/certs/V2G Root CA.pem
    client_certificate = /app/certs/Vehicle Leaf cert.pem
    keyfile = /app/certs/Vehicle Leaf private key.pem
    client_certificate_chain = /app/certs/vehicleCertChain.pem
    min_version = 1.3
    max_version = 1.3

Restart the charging applications afterwards: the certificate files are read once at start-up.

Bring this up in two steps rather than one. Set `enabled = true` while leaving `allow_no_cert = true`
first — that gets an encrypted session working without your PKI having to be right yet. Only then set
`allow_no_cert = false`, which is the step that actually exercises certificate verification and is
where a wrong chain or an untrusted root shows up.

## `[tls]`

### enabled

<figcaption>Example</figcaption>

    enabled = true

Master switch. When `false` the controller announces plain TCP in the SDP exchange and creates no TLS
endpoint; when `true` it announces and requires TLS.

Default to false.

### allow_no_cert

<figcaption>Example</figcaption>

    allow_no_cert = false

When `true`, the charger's certificate is accepted **without being verified**. Useful while bringing
a bench up against a charger whose certificates are not from your PKI, but it removes the guarantee
that you are talking to the charger you think you are. Set it `false` in production.

Note that a Plug & Charge session on ISO 15118-2 is normally set up with `allow_no_cert = true`: what
is being authenticated there is the *contract*, not the charger.

Default to true.

### allow_iso_20_without_tls

<figcaption>Example</figcaption>

    allow_iso_20_without_tls = true

Whether an ISO 15118-20 session may proceed with no TLS at all. Shipped as `true`, which is what
makes the default configuration work against non-TLS chargers. Set it `false` once you require TLS,
so a charger that does not offer it is rejected rather than silently downgraded.

Default to true.

## `[tls:client]`

The files the vehicle presents and trusts. All of them are read once at start-up, so a change needs a
restart of the charging applications.

### ca_file

<figcaption>Example</figcaption>

    ca_file = /app/certs/V2G Root CA.pem

The CA against which the **charger's** certificate is verified — normally the V2G Root CA. Not used
while `allow_no_cert` is `true`.

Default to `/app/certs/CA.pem`.

### client_certificate

<figcaption>Example</figcaption>

    client_certificate = /app/certs/Vehicle Leaf cert.pem

The vehicle's own leaf certificate, presented to the charger.

Default to `/app/certs/client.pem`.

### keyfile

<figcaption>Example</figcaption>

    keyfile = /app/certs/Vehicle Leaf private key.pem

The private key belonging to `client_certificate`.

Default to `/app/certs/client.key`.

### client_certificate_chain

<figcaption>Example</figcaption>

    client_certificate_chain = /app/certs/vehicleCertChain.pem

The intermediate certificates between the vehicle leaf and the root, so the charger can build a
complete path. Leave empty only if the leaf is signed directly by a CA the charger already trusts.

Default to empty.

### keyfile_passphrase

<figcaption>Example</figcaption>

    keyfile_passphrase = my-passphrase

Only needed if the private key in `keyfile` is passphrase-protected.

Default to empty.

### min_version

<figcaption>Example</figcaption>

    min_version = 1.3

Lowest TLS version the vehicle will negotiate. ISO 15118-20 requires **TLS 1.3**, so set both this
and `max_version` to `1.3` for a compliant session. The default window is wider because the same
stack also serves ISO 15118-2, which uses TLS 1.2.

Default to 1.2.

### max_version

<figcaption>Example</figcaption>

    max_version = 1.3

Highest TLS version the vehicle will negotiate.

Default to 1.3.

## Related entries in `[ccs]`

### allow_no_tls_for_iso_part20

<figcaption>Example</figcaption>

    allow_no_tls_for_iso_part20 = true

Whether the ISO 15118-20 stack accepts running without TLS. Shipped as `true`. The standard prohibits
it; in practice you should not expect TLS to be widely deployed on chargers yet, which is why it is
the default. Set it `false` together with `[tls] enabled = true`.

### allow_tls_1_2_for_iso_part20

<figcaption>Example</figcaption>

    allow_tls_1_2_for_iso_part20 = true

Whether TLS 1.2 is acceptable for an ISO 15118-20 session. Shipped as `true`. The standard requires
TLS 1.3; leaving 1.2 permitted lets you interoperate with a charger that has not caught up. Set it
`false` for a compliant session.

## Plug & Charge

Plug & Charge is implemented for **ISO 15118-2 only**, so it is available on a CCS vehicle
(ADM-CS-EVCC) and not on an MCS one (ADM-CS-MEVC), which runs ISO 15118-20 and authorises by EIM.

The certificate set is different from the one above, and smaller. The vehicle presents no client
certificate of its own — what authenticates it is the **contract**, not the TLS handshake — so all it
needs is:

- The **V2G Root CA**, in `pem` format, to verify the charger.
- The **Plug & Charge contract and its certificate chain**, as a single **PKCS#12** file.

The PKCS#12 file is not usually supplied by the PKI in that form; you build it from the contract key,
its leaf certificate, and a chain of the two MO Sub CAs:

    cat <MO_SUB_CA2_CERTIFICATE.pem> <MO_SUB_CA1_CERTIFICATE.pem> > moSubCAs.pem

    openssl pkcs12 -export \
        -inkey <MO_CONTRACT_PRIVATE_KEY.pem> \
        -in <MO_CONTRACT_LEAF_CERTIFICATE.pem> \
        -name mo_cert \
        -certfile moSubCAs.pem \
        -passin "pass:" -passout "pass:" \
        -out moCertChain.p12

`moCertChain.p12` is the file you provision. Adjust `-passin` if the contract key is
password-protected, and `-passout` if you want the PKCS#12 itself protected — in which case set
`pnc_contract_p12_passphrase` to match. See `man openssl-passphrase-options` for ways of supplying a
password that do not put it on the command line.

<figcaption>Plug &amp; Charge over ISO 15118-2</figcaption>

    [ccs]
    enable_iso_part2 = true
    enable_pnc = true
    pnc_contract_p12 = /app/certs/moCertChain.p12
    # Only if the PKCS#12 file was built with a password
    pnc_contract_p12_passphrase = password

    [tls]
    enabled = true
    allow_no_cert = true

    [tls:client]
    ca_file = /app/certs/V2G Root CA.pem

For what these certificates are and how the roles relate, see the
[Plug'n'Charge primer](https://documentation.advantics.fr/adm-cs-spcc/charger-features/tls_pnc/pnc_primer.html).
