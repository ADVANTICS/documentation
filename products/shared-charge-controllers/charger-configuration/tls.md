# TLS

A charger-side charge controller is the TLS **server**: the vehicle connects to it and verifies its
certificate. This page applies to both charger controllers, because they share the same TLS
implementation and the same configuration entries.

## When TLS is needed

| Protocol | TLS |
|---|---|
| **ISO 15118-20** — MCS, and optionally CCS | **Required** by the standard, with TLS 1.3 |
| **ISO 15118-2** — CCS | Only for **Plug & Charge**. An EIM session does not use it |
| **DIN 70121** — CCS | Not used (`allow_tls_for_din` is `false` and not exposed) |

!!! warning "The controller ships with TLS disabled"
    Out of the box `[tls] enabled = false`, and the entries that tolerate a session without TLS are
    all set. This is deliberate: it lets you charge the vehicles that exist today, most of which do
    not do TLS. Turning TLS on is something you do on purpose, once you have a PKI — see
    [Enabling TLS](#enabling-tls).

Configuration is spread over three places:

| Section | Holds |
|---|---|
| `[tls]` | Whether TLS is used, and whether the vehicle's certificate is verified |
| `[tls:server]` | The certificate and key files, and the TLS version window |
| `[pistol:<name>]` | Which protocols the pistol offers, and how tolerant ISO 15118-20 is without TLS |

!!! note "The protocol entries are per pistol, not global"
    Unlike the vehicle side — where they sit in one `[ccs]` section — `enable_iso_part2`,
    `enable_iso_part20` and `allow_no_tls_for_iso_part20` belong to the **pistol** section, e.g.
    `[pistol:CCS DC]` or `[pistol:MCS]`. A multi-pistol charger configures each one separately. The
    `[tls]` and `[tls:server]` sections, by contrast, are shared by every pistol: there is one
    server certificate for the controller, not one per connector.

!!! note "Sub-sections are separated by a colon"
    `[tls:server]` is a *sub-section* of `[tls]`, not a section called `tls:server`. Write it exactly
    as shown.

!!! warning "A misspelled entry is silently ignored"
    The configuration is loaded non-strictly: an option the controller does not recognise is skipped
    without any error or log line, and the built-in default applies instead. If a setting appears to
    have no effect, check the spelling and the section before anything else. In particular,
    `min_version` and `max_version` belong in `[tls:server]` — placed directly under `[tls]` they do
    nothing.

## What ships on the controller

<figcaption>Relevant part of the default <code>config.cfg</code></figcaption>

    [pistol:MCS]
    allow_tls_1_2_for_iso_part20 = true
    allow_no_tls_for_iso_part20 = true

    [tls]
    enabled = false
    allow_no_cert = true
    allow_iso_20_without_tls = true

There is no `[tls:server]` section in the shipped file — the built-in file paths apply, and nothing
reads them while `enabled` is `false`.

## Enabling TLS

### 1. Provision the certificates

Copy the certificates onto the controller, into the directory that is bind-mounted into the
`ccs-secc` container as `/app/certs`. Where that directory is
depends on which system the controller runs:

<div class="small-table compact-table" markdown="1">

| Controller | Directory on the controller |
|---|---|
| **ADM-CS-SECC** | `/srv/certs` |
| **ADM-CS-SPCC** | `certs` under the Docker Compose profile in use — by default `/etc/advantics/default/certs` |

</div>

!!! note "The paths in the configuration file stay `/app/certs/...`"
    `config.cfg` is read by the application *inside* the container, so `ca_file`, `keyfile`,
    `server_certificate` and `server_certificate_chain` must all use the container path
    `/app/certs/<file>` — not the directory you copied the files into. The bind mount is what
    connects the two.

Provide these files:

- The **V2G Root CA**, in `pem` format.
- The **EVSE leaf certificate** and its **private key**, in `pem` format. This is the **CPO** EVSE
  leaf for ISO 15118-2 and the **CSO** EVSE leaf for ISO 15118-20 — CSO in -20 is the same role CPO
  plays in -2.
- The **EVSE certificate chain** — the two CPO (or CSO) Sub CAs followed by the Root CA, which should
  be the V2G Root CA.
- For Plug & Charge only: the **MO Root CA**, if it is not the same as the V2G Root CA.

Order matters when building the chain from separate files:

    cat <CPO_SUB_CA2.pem> <CPO_SUB_CA1.pem> <V2G Root CA.pem> > cpoCertChain.pem

and for ISO 15118-20:

    cat <CSO_SUB_CA2.pem> <CSO_SUB_CA1.pem> <V2G Root CA.pem> > csoCertChain.pem

!!! warning "Everything must be PEM, including the key"
    All of these files are loaded as PEM and nothing else is accepted — a DER or otherwise binary
    file will fail to load. For the private key, either PEM block type works: the traditional
    `-----BEGIN RSA PRIVATE KEY-----` / `-----BEGIN EC PRIVATE KEY-----`, or the PKCS#8
    `-----BEGIN PRIVATE KEY-----`. Convert a binary key first:

        openssl pkey -in key.der -inform DER -out key.pem -outform PEM

### 2. Point the configuration at them

<figcaption>Standard-compliant ISO 15118-20 charger</figcaption>

    [pistol:MCS]
    enable_iso_part20 = true
    allow_tls_1_2_for_iso_part20 = false
    allow_no_tls_for_iso_part20 = false

    [tls]
    enabled = true
    allow_no_cert = false
    allow_iso_20_without_tls = false

    [tls:server]
    ca_file = /app/certs/V2G Root CA.pem
    server_certificate = /app/certs/CSO EVSE Leaf cert.pem
    keyfile = /app/certs/CSO EVSE private key.pem
    server_certificate_chain = /app/certs/csoCertChain.pem
    min_version = 1.3
    max_version = 1.3

Restart the charging applications afterwards: the certificate files are read once at start-up.

Bring this up in two steps rather than one. Set `enabled = true` while leaving `allow_no_cert = true`
first — that gets an encrypted session working without the vehicle's PKI having to be right yet. Only
then set `allow_no_cert = false`, which is the step that actually exercises certificate verification.

This configuration can also be applied from the
[Web UI](../advos-yocto-system/csm-web-ui.md) instead of editing the file, with the exception of the
Plug & Charge entries — see [Plug & Charge](#plug-charge).

## `[tls]`

### enabled

<figcaption>Example</figcaption>

    enabled = true

Master switch. When `false` the controller offers plain TCP in the SDP exchange and creates no TLS
endpoint; when `true` it offers TLS.

Default to false.

### allow_no_cert

<figcaption>Example</figcaption>

    allow_no_cert = false

When `true`, the vehicle's certificate is accepted **without being verified**. Useful while bringing
a bench up against a vehicle whose certificates are not from your PKI, but it removes the guarantee
that the vehicle is who it claims to be. Set it `false` in production.

An ISO 15118-2 Plug & Charge session is normally set up with `allow_no_cert = true`: what is being
authenticated there is the *contract* the vehicle presents, not the TLS client certificate.

Default to true.

### allow_iso_20_without_tls

<figcaption>Example</figcaption>

    allow_iso_20_without_tls = true

Whether an ISO 15118-20 session may proceed with no TLS at all. Shipped as `true`, which is what
makes the default configuration work with vehicles that do not do TLS. Set it `false` once you
require TLS, so a vehicle that does not offer it is rejected rather than silently downgraded.

Default to true.

## `[tls:server]`

The files the charger presents and trusts. All of them are read once at start-up, so a change needs a
restart of the charging applications.

### ca_file

<figcaption>Example</figcaption>

    ca_file = /app/certs/V2G Root CA.pem

The CA against which the **vehicle's** certificate is verified — normally the V2G Root CA. Not used
while `allow_no_cert` is `true`.

Default to `/app/certs/CA.pem`.

### server_certificate

<figcaption>Example</figcaption>

    server_certificate = /app/certs/CSO EVSE Leaf cert.pem

The charger's own leaf certificate, presented to the vehicle. The CPO EVSE leaf for ISO 15118-2, the
CSO EVSE leaf for ISO 15118-20.

Default to `/app/certs/server.pem`.

### keyfile

<figcaption>Example</figcaption>

    keyfile = /app/certs/CSO EVSE private key.pem

The private key belonging to `server_certificate`.

Default to `/app/certs/server.key`.

### server_certificate_chain

<figcaption>Example</figcaption>

    server_certificate_chain = /app/certs/csoCertChain.pem

The intermediate certificates between the EVSE leaf and the root, so the vehicle can build a
complete path. Leave empty only if the leaf is signed directly by a CA the vehicle already trusts.

Default to empty.

### keyfile_passphrase

<figcaption>Example</figcaption>

    keyfile_passphrase = my-passphrase

Only needed if the private key in `keyfile` is passphrase-protected.

Default to empty.

### min_version

<figcaption>Example</figcaption>

    min_version = 1.3

Lowest TLS version the charger will negotiate. ISO 15118-20 requires **TLS 1.3**, so set both this
and `max_version` to `1.3` for a compliant session. The default window is wider because the same
stack also serves ISO 15118-2, which uses TLS 1.2.

Default to 1.2.

### max_version

<figcaption>Example</figcaption>

    max_version = 1.3

Highest TLS version the charger will negotiate.

Default to 1.3.

## Per-pistol entries

These belong to the pistol's own section, e.g. `[pistol:CCS DC]` or `[pistol:MCS]`.

### allow_no_tls_for_iso_part20

<figcaption>Example</figcaption>

    allow_no_tls_for_iso_part20 = true

Whether this pistol's ISO 15118-20 stack accepts running without TLS. The standard prohibits it; in
practice you should not expect TLS to be widely deployed on vehicles yet, which is why the shipped
configuration enables it. Set it `false` together with `[tls] enabled = true`.

Default to false, but shipped as `true`.

### allow_tls_1_2_for_iso_part20

<figcaption>Example</figcaption>

    allow_tls_1_2_for_iso_part20 = true

Whether TLS 1.2 is acceptable for an ISO 15118-20 session on this pistol. The standard requires
TLS 1.3; leaving 1.2 permitted lets you interoperate with a vehicle that has not caught up. Set it
`false` for a compliant session. Not exposed in the Web UI.

Default to false, but shipped as `true`.

## Plug & Charge

Plug & Charge is an **ISO 15118-2** feature. Its entries are not exposed in the Web UI — they can only
be set by editing the configuration file.

<figcaption>Plug &amp; Charge over ISO 15118-2</figcaption>

    [pistol:CCS DC]
    enable_iso_part2 = true
    enable_eim = false
    enable_pnc = true
    mo_root_ca_pem = /app/certs/MO Root CA.pem

    [tls]
    enabled = true
    allow_no_cert = true

    [tls:server]
    ca_file = /app/certs/V2G Root CA.pem
    server_certificate = /app/certs/CPO EVSE Leaf cert.pem
    keyfile = /app/certs/CPO EVSE private key.pem
    server_certificate_chain = /app/certs/cpoCertChain.pem

`enable_eim = false` makes Plug & Charge the *only* authorisation method the pistol offers; leave it
`true` if you want a vehicle without a contract to still be able to charge by external
identification.

`mo_root_ca_pem` is only needed when the Mobility Operator root differs from the V2G Root CA. Two
further entries exist for contract handling — `enable_contract_installation` and
`enable_contract_update` — both off, and both file-only.

For what these certificates are and how the roles relate, see the
[Plug'n'Charge primer](../charger-features/tls_pnc/pnc_primer.md).
