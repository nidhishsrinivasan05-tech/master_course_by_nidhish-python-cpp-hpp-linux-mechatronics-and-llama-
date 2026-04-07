## Data transmission demo for using gRPC in Python

When using gRPC in Python, there are four data transmission patterns. [Official guide](<https://grpc.io/docs/guides/concepts/#unary-rpc>)

- #### Unary mode

  In a single call, the client can send only one request to the server, and the server can return only one response.

  `client.py: simple_method`

  `server.py: SimpleMethod`

- #### Client streaming mode

  In a single call, the client can send data to the server multiple times, but the server can return only one response.

  `client.py: client_streaming_method `

  `server.py: ClientStreamingMethod`

- #### Server streaming mode

  In a single call, the client can send only one request to the server, but the server can return multiple responses.

  `client.py: server_streaming_method`

  `server.py: ServerStreamingMethod`

- #### Bidirectional streaming mode

  In a single call, both client and server can send and receive data from each other multiple times.

  `client.py: bidirectional_streaming_method`

  `server.py: BidirectionalStreamingMethod`

