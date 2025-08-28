> [!UPDATE] {docsify-updated}
# Troubleshooting

Avoid connecting other electronic equipment in parallel on the CCS signals (CP and PP), such as
generic IO controllers to monitor the CP and PP states. They would likely interfere with the normal
operation of the charge controller. Instead, use readouts reported on the CAN bus by the controller.
