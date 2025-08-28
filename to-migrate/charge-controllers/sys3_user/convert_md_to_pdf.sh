#!/bin/bash

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed. Please install pandoc first."
    exit 1
fi

# Check if an input file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 input.md [output.pdf]"
    exit 1
fi

input_file="$1"
output_file="${2:-output.pdf}"

# Convert Markdown to PDF using pandoc
pandoc --pdf-engine=wkhtmltopdf --pdf-engine-opt="--enable-local-file-access" "$input_file" -o "$output_file" --variable colorlinks=true

echo "Conversion complete. PDF saved to: $output_file"

