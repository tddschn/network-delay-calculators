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
    parser.add_argument('--t1', type=float, default=1, help="Transmission Rate at Link1 (value in Mbps)")
    parser.add_argument('--t2', type=float, default=1, help="Transmission Rate at Link2 (value in Mbps)")
    parser.add_argument('--T1', type=float, help="Transmission Delay at Link1 (value in milliseconds)")
    parser.add_argument('--T2', type=float, help="Transmission Delay at Link2 (value in milliseconds)")
    parser.add_argument('--d1', type=float, default=1, help="Distance of Link1 (value in KM)")
    parser.add_argument('--d2', type=float, default=1, help="Distance of Link2 (value in KM)")
    parser.add_argument('--D1', type=float, help="Propagation Delay at Link1 (value in milliseconds)")
    parser.add_argument('--D2', type=float, help="Propagation Delay at Link2 (value in milliseconds)")
    parser.add_argument('-N', type=float, default=1, help="Number of Packets")
    parser.add_argument('-M', type=float, default=1, help="Packet Size (value in Mbits)")
    parser.add_argument('-S', type=float, default=1, help="Propagation Speed (speed in 10^8m/s)")
    parser.add_argument('-p', type=float, default=0, help="Router Processing Time (processing time in milliseconds)")

    args = parser.parse_args()

    n, A, B, queue_delay = 1, 0, 0, 0
    while n <= args.N:
        R = A + (args.T1 if args.T1 else trans_delay(args.t1, args.M)) + (args.D1 if args.D1 else prop_delay(args.d1, args.S))
        B = R + queue_delay + args.p + (args.T2 if args.T2 else trans_delay(args.t2, args.M)) + (args.D2 if args.D2 else prop_delay(args.d2, args.S))
        
        td_t1 = args.T1 if args.T1 else trans_delay(args.t1, args.M)
        td_t2 = args.T2 if args.T2 else trans_delay(args.t2, args.M)

        if R < td_t2:
            queue_delay += td_t2 - td_t1
        
        print(f'{"P" + str(n):<10}{"":<2}{A:9.3f} ms{"":<17}{R:9.3f} ms{"":<17}{B:9.3f} ms')
        n, A = n + 1, A + td_t1

    print(f"\nEnd to End transmission delay = {B:9.3f} ms\n")

if __name__ == '__main__':
    main()
