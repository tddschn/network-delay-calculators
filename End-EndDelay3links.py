#!/usr/bin/env python3

import argparse
from tabulate import tabulate



# Transmission Delay
def trans_delay(t, M):
    return (float(M) / t) * 10**3

# Propagation Delay
def prop_delay(d, S):
    return d / (S * 100.0)

def main():
    parser = argparse.ArgumentParser(description="Calculate network transmission and propagation delays.", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--t1', type=float, default=1, help="Transmission Delay (link speed) at Link1 (value in Mbps)")
    parser.add_argument('--t2', type=float, default=1, help="Transmission Delay (link speed) at Link2 (value in Mbps)")
    parser.add_argument('--t3', type=float, default=1, help="Transmission Delay (link speed) at Link3 (value in Mbps)")
    
    parser.add_argument('--T1', type=float, help="Transmission Delay at Link1 (value in milliseconds)")
    parser.add_argument('--T2', type=float, help="Transmission Delay at Link2 (value in milliseconds)")
    parser.add_argument('--T3', type=float, help="Transmission Delay at Link3 (value in milliseconds)")

    parser.add_argument('--d1', type=float, default=1, help="Distance of Link1 (value in KM)")
    parser.add_argument('--d2', type=float, default=1, help="Distance of Link2 (value in KM)")
    parser.add_argument('--d3', type=float, default=1, help="Distance of Link3 (value in KM)")
    parser.add_argument('--D1', type=float, help="Propagation Delay at Link1 (value in milliseconds)")
    parser.add_argument('--D2', type=float, help="Propagation Delay at Link2 (value in milliseconds)")
    parser.add_argument('--D3', type=float, help="Propagation Delay at Link3 (value in milliseconds)")

    parser.add_argument('-N', type=float, default=1, help="Number of Packets")
    parser.add_argument('-M', type=float, default=1, help="Packet Size (value in Mbits)")
    parser.add_argument('-S', type=float, default=1, help="Propagation Speed (speed in 10^8m/s)")
    parser.add_argument('-p', type=float, default=0, help="Router Processing Time (processing time in milliseconds)")

    args = parser.parse_args()
    data = []

    n, A, queue_delay1, queue_delay2 = 1, 0, 0, 0
    while n <= args.N:
        R1 = A + (args.T1 if args.T1 else trans_delay(args.t1, args.M)) + (args.D1 if args.D1 else prop_delay(args.d1, args.S))
        R2 = R1 + queue_delay1 + args.p + (args.T2 if args.T2 else trans_delay(args.t2, args.M)) + (args.D2 if args.D2 else prop_delay(args.d2, args.S))
        B = R2 + queue_delay2 + args.p + (args.T3 if args.T3 else trans_delay(args.t3, args.M)) + (args.D3 if args.D3 else prop_delay(args.d3, args.S))
        
        
        td_t1 = args.T1 if args.T1 else trans_delay(args.t1, args.M)
        td_t2 = args.T2 if args.T2 else trans_delay(args.t2, args.M)
        td_t3 = args.T3 if args.T3 else trans_delay(args.t3, args.M)

        if R1 < td_t2:
            queue_delay1 += td_t2 - td_t1
        if R2 < td_t3:
            queue_delay2 += td_t3 - td_t2

        data.append(("P" + str(n), A, R1, R2, B))

        # print(f'{"P" + str(n):<10}{"":<5}{A:9.3f}{"":<20}{R1:9.3f}{"":<20}{R2:9.3f}{"":<20}{B:9.3f}')
        n, A = n + 1, A + td_t1

    # print()
    # print("-----------------------------------------------------------------------------------------------------------------")
    headers = ["Packet", "A (ms)", "R1 (ms)", "R2 (ms)", "B (ms)"]
    # cSpell:disable
    print(tabulate(data, headers=headers, floatfmt=".3f"))
    # cSpell:enable


if __name__ == '__main__':
    main()
