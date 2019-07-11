# Web Server - Day 4

## TCP vs UDP

- TCP is the standard way to establish network connections
- UDP is an alternative to TCP, that's usually used for low-latency and loss-tolerating connections between apps on the internet.
  - UDP send a greater of packets and doesn't care reliability as much as TCP
  - UDP is usually used for network apps where latency is most important, like gaming, and voice/video communication.
- Downsides of UDP:
  - UDP does not guarantee that the data will arrive, that it won't be duplicated or that it will be in order.
