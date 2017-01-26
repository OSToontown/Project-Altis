# Art assets:
model-path ../resources

# Server:
server-version TTPA-Alpha-1.2.4
min-access-level 600
accountdb-type local
shard-low-pop 50
shard-mid-pop 100

# RPC:
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/

# DClass file:
dc-file astron/dclass/toon.dc

# Core features:
want-pets #t
want-parties #f
want-cogdominiums #f
want-achievements #f

# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Developer options:
show-population #t
show-total-population #t
force-skip-tutorial #t
want-instant-parties #t

# Weather
weather-cycle-duration 100