# Server:
server-version TTPA-Alpha-1.2.0
min-access-level 600
shard-low-pop 50
shard-mid-pop 100

# DC File
dc-file config/toon.dc

#Resources
vfs-mount resources/phase_3 /phase_3
vfs-mount resources/phase_3.5 /phase_3.5
vfs-mount resources/phase_4 /phase_4
vfs-mount resources/phase_5 /phase_5
vfs-mount resources/phase_5.5 /phase_5.5
vfs-mount resources/phase_6 /phase_6
vfs-mount resources/phase_7 /phase_7
vfs-mount resources/phase_8 /phase_8
vfs-mount resources/phase_9 /phase_9
vfs-mount resources/phase_10 /phase_10
vfs-mount resources/phase_11 /phase_11
vfs-mount resources/phase_12 /phase_12
vfs-mount resources/phase_13 /phase_13
model-path resources

# Core features:
want-pets #t
want-parties #f
want-cogdominiums #t
want-achievements #f

# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Developer options:
want-dev #f