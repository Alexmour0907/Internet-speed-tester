# Internet Speed Tester

This is a simple Python script that measures your internet speed using the `speedtest-cli` library.

## Features

- Measures download speed in Mbps.
- Measures upload speed in Mbps.
- Measures ping in ms.

## Requirements

- Python 3
- `speedtest-cli`

You can install the required library using pip:
```bash
pip install speedtest-cli
```

## Usage

To run the script, simply execute the following command in your terminal:
```bash
python internet-speed-tester.py
```

## Output
The script will print the internet speed details to the console, like this:
```
Testing speed...
Download Speed: 94.32 Mbps
Upload Speed: 90.45 Mbps
Ping: 12.34 ms
```