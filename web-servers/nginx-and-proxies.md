# What is a proxy?

acting on behalf of someone/something else -> proxy server - intermediary server 
that forwards *client requests* to other servers

![forward_proxy_flow.png](../../../../Downloads/forward_proxy_flow.png)

![reverse_proxy_flow.png](../../../../Downloads/reverse_proxy_flow.png)

Reverse proxy -> re-routes traffic and does load balancing
- can enable HTTPS without needing certificates

reverse proxy -> show whats happening on port 3000 on port 80 (you can delete port 3000)
useful for caching , 

load balancing  - > proxies requests to many web servers
algorithms 
- least connections: routes traffic to the server with the fewest active connections
- round robin    : distributes requests in a sequential, cyclical manner to each server

Caching --> keep one copy e.g the file configured with images and got data from a db
once, then sent out that copy to anyone who requested it

one entrypoint : added security layer, all sensitive data can be stored on one server 
this server is fully secured nginx forwards an encrypted message, webserver decrypts it

nginx proxy can also be configured to compress the response, to reduce bandwidth and 
improve load times
segmentation - sending response in chunks e.g videos, sent bit by bit 

security group (firewall) -> inbound /outbound 
inbound -> all closed by default -> ip address (who will access the port)
out -> ur sever can communicate with things outside your local network
all open by default