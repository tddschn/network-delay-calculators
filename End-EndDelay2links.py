#!/usr/bin/env python3

import argparse
from decimal import Decimal, getcontext
from tabulate import tabulate

# Set precision
getcontext().prec = 28

def trans_delay(t, M):
    """Compute Transmission Delay."""
    return (M / t) * Decimal("1000")

def prop_delay(d, S):
    """Compute Propagation Delay."""
    return d / (S * Decimal("100"))

def get_args():
    """Get command line arguments."""
    parser = argparse.ArgumentParser(description="Calculate network transmission and propagation delays for A-R-B network.", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--t1', type=Decimal, default=1, help="Transmission Delay (link speed) at Link1 (value in Mbps)")
    parser.add_argument('--t2', type=Decimal, default=1, help="Transmission Delay (link speed) at Link2 (value in Mbps)")

    parser.add_argument('--T1', type=Decimal, help="Transmission Delay at Link1 (value in milliseconds)")
    parser.add_argument('--T2', type=Decimal, help="Transmission Delay at Link2 (value in milliseconds)")

    parser.add_argument('--d1', type=Decimal, default=1, help="Distance of Link1 (value in KM)")
    parser.add_argument('--d2', type=Decimal, default=1, help="Distance of Link2 (value in KM)")
    parser.add_argument('--D1', type=Decimal, help="Propagation Delay at Link1 (value in milliseconds)")
    parser.add_argument('--D2', type=Decimal, help="Propagation Delay at Link2 (value in milliseconds)")

    parser.add_argument('-N', type=Decimal, default=1, help="Number of Packets")
    parser.add_argument('-M', type=Decimal, default=1, help="Packet Size (value in Mbits)")
    parser.add_argument('-S', type=Decimal, default=1, help="Propagation Speed (speed in 10^8m/s)")
    parser.add_argument('-p', type=Decimal, default=0, help="Router Processing Time (processing time in milliseconds)")

    return parser.parse_args()

def get_delays(args):
    """Compute delays and return them."""
    data = []
    n, A, queue_delay1 = Decimal("1"), Decimal("0"), Decimal("0")

    while n <= args.N:
        td_t1 = args.T1 if args.T1 else trans_delay(args.t1, args.M)
        td_t2 = args.T2 if args.T2 else trans_delay(args.t2, args.M)

        R = A + td_t1 + (args.D1 if args.D1 else prop_delay(args.d1, args.S))
        B = R + queue_delay1 + args.p + td_t2 + (args.D2 if args.D2 else prop_delay(args.d2, args.S))
        
        data.append(["P" + str(n), A, R, B, queue_delay1])
        if R < td_t2:
            queue_delay1 += td_t2 - td_t1


        n, A = n + 1, A + td_t1

    return data

def main():
    """Main function."""
    args = get_args()
    delays = get_delays(args)

    headers = ["Packet", "A (ms)", "R (ms)", "B (ms)", "Queue Delay (ms)"]
    print(tabulate(delays, headers=headers, tablefmt='pipe'))

if __name__ == '__main__':
    main()
