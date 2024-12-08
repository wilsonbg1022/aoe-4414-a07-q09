## Script Name: max_bitrate.py

## Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz

## Parameters:
# tx_w: P
# tx_gain_db: Gt
# freq_hz: lambda is frequency Hz
# dist_km: S
# rx_gain_db: Gr
# n0_j: N0
# bw_hz: bandwidth B

## Output: max bit data bit rate

## Written by Brett Wilson

## Importing Libraries
import math
import sys # argv

## Defining Constants
La = 1 # Line loss in atmosphere
Ll = 1 # Line loss factor

## Initialize Script Arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

## Parse Script Arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    sys.exit()

## Main Script
C = tx_w * Ll * tx_gain_db * (freq_hz / (4 * math.pi * dist_km))**2 * La * rx_gain_db
N = n0_j*bw_hz
r_max = bw_hz * math.log2(1 + C / N)/10e5

print(math.floor(r_max))