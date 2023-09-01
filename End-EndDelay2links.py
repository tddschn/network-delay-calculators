#!/usr/bin/env python3
import argparse

# Transmission Delay
def trans_delay(t, M):
    return (M / t) * 10**3

# Propagation Delay
def prop_delay(d, S):
    return d / (S * 100)

def main():
    parser = argparse.ArgumentParser(description="Calculate network transmission and propagation delays.")
    parser.add_argument('--t1', type=float, default=1, help="Transmission Delay at Link1 (value in Mbps)")
    parser.add_argument('--t2', type=float, default=1, help="Transmission Delay at Link2 (value in Mbps)")
    parser.add_argument('--d1', type=float, default=1, help="Distance of Link1 (value in KM)")
    parser.add_argument('--d2', type=float, default=1, help="Distance of Link2 (value in KM)")
    parser.add_argument('-N', type=float, default=1, help="Number of Packets")
    parser.add_argument('-M', type=float, default=1, help="Packet Size (value in Mbits)")
    parser.add_argument('-S', type=float, default=1, help="Propagation Speed (speed in 10^8m/s)")
    parser.add_argument('-p', type=float, default=1, help="Router Processing Time (processing time in milliseconds)")

    args = parser.parse_args()

    n, A, B, queue_delay = 1, 0, 0, 0
    while n <= args.N:
        R = A + trans_delay(args.t1, args.M) + prop_delay(args.d1, args.S)
        B = R + queue_delay + args.p + trans_delay(args.t2, args.M) + prop_delay(args.d2, args.S)
        
        if R < trans_delay(args.t2, args.M):
            queue_delay += trans_delay(args.t2, args.M) - trans_delay(args.t1, args.M)
        
        print(f'{"P" + str(n):<10}{"":<2}{A:9.3f} ms{"":<17}{R:9.3f} ms{"":<17}{B:9.3f} ms')
        n, A = n + 1, A + trans_delay(args.t1, args.M)

    print(f"\nEnd to End transmission delay = {B:9.3f} ms\n")

if __name__ == '__main__':
    main()
