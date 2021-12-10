> [!UPDATE] {docsify-updated}
# Current deviation

## current_deviation_a

<figcaption>Example</figcaption>

    current_deviation_a = 10

Current deviation limit threshold, in Amps. If charger is doing more or less current than this
value, Advantics controller will consider it enters in current deviation error. This error will have
to persist for a certain time (see [current_deviation_t](#current_deviation_t)) to actually trigger a charge stop.

Default to 10 A.

## current_deviation_t

<figcaption>Example</figcaption>

    current_deviation_t = 10

Current deviation offending time before cut-off, in seconds. If charger is doing more or less
current than `current_deviation_a` for this amount of time, the current deviation error will be
confirmed and a charge stop will be triggered.

Default to 10 s.

## current_deviation_accept_less

<figcaption>Example</figcaption>

    current_deviation_accept_less = true

If charger is doing less current than requested, we can accept it and not consider it to be a
current deviation error.

Default to true.
