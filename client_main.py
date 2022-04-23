#!/usr/bin/env python3

from server.reversi_client import ReversiClient

if __name__ == '__main__':
    client = ReversiClient()
    client.start_client()