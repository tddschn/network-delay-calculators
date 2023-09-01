# End-to-end Network Delay Calculator

Based on https://github.com/ashxjain/End-To-EndDelayFinder

- [End-to-end Network Delay Calculator](#end-to-end-network-delay-calculator)
  - [SYNOPSIS](#synopsis)
  - [Features](#features)
  - [Examples](#examples)
  - [Note](#note)


## SYNOPSIS

* End-EndDelay2links.py is a python program to compute end-to-end transmission in a network connecting Host A to Host B via a router R using store and forward switching.
* End-EndDelay3links.py is a python program to compute end-to-end transmission in a network connecting Host A to Host B to Host C via two routers R1,R2 using store and forward switching.

## Features

- Removed legacy code (`getopt` & Python 2 syntax), added detailed help messages
- Allows specifying transmission and propagation delays directly
- Uses the `decimal` library for accurate floating point arithmetic
- Beautiful markdown table output
- Shows when which packet arrives at which hop, and the queueing delays

## Examples

```
$ ./End-EndDelay3links.py -h

usage: End-EndDelay3links.py [-h] [--t1 T1] [--t2 T2] [--t3 T3] [--T1 T1] [--T2 T2] [--T3 T3] [--d1 D1] [--d2 D2] [--d3 D3] [--D1 D1] [--D2 D2] [--D3 D3]
                             [-N N] [-M M] [-S S] [-p P]

Calculate network transmission and propagation delays.

options:
  -h, --help  show this help message and exit
  --t1 T1     Transmission Delay (link speed) at Link1 (value in Mbps) (default: 1)
  --t2 T2     Transmission Delay (link speed) at Link2 (value in Mbps) (default: 1)
  --t3 T3     Transmission Delay (link speed) at Link3 (value in Mbps) (default: 1)
  --T1 T1     Transmission Delay at Link1 (value in milliseconds) (default: None)
  --T2 T2     Transmission Delay at Link2 (value in milliseconds) (default: None)
  --T3 T3     Transmission Delay at Link3 (value in milliseconds) (default: None)
  --d1 D1     Distance of Link1 (value in KM) (default: 1)
  --d2 D2     Distance of Link2 (value in KM) (default: 1)
  --d3 D3     Distance of Link3 (value in KM) (default: 1)
  --D1 D1     Propagation Delay at Link1 (value in milliseconds) (default: None)
  --D2 D2     Propagation Delay at Link2 (value in milliseconds) (default: None)
  --D3 D3     Propagation Delay at Link3 (value in milliseconds) (default: None)
  -N N        Number of Packets (default: 1)
  -M M        Packet Size (value in Mbits) (default: 1)
  -S S        Propagation Speed (speed in 10^8m/s) (default: 1)
  -p P        Router Processing Time (processing time in milliseconds) (default: 0)
  ```

```
$ ./End-EndDelay3links.py --t1 10 --t2 1 --t3 1 --D1 10 --D2 90 --D3 100 -N 3 -M 0.05 -S 2

| Packet | A (ms) | R1 (ms) | R2 (ms) | B (ms) | Queue Delay1 (ms) | Queue Delay2 (ms) |
| :----- | -----: | ------: | ------: | -----: | ----------------: | ----------------: |
| P1     |      0 |      15 |     155 |    305 |                45 |                 0 |
| P2     |      5 |      20 |     205 |    355 |                90 |                 0 |
| P3     |     10 |      25 |     255 |    405 |               135 |                 0 |
```

## Note

Please attribute the original authors (Teddy Xinyuan Chen (@tddschn) and Ashish Jain (@ashxjain)) if you use this code in your (home)work.