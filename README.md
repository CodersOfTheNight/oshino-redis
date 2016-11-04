oshino-redis
=====================
Agent for retrieving redis stats

For more info, refer to parent project [Oshino](https://github.com/CodersOfTheNight/oshino)

Installing
==========
`pip install oshino-redis`

Add agent to configuration:
```yaml
module: oshino_redis.agent.RedisAgent
```

Agent config
============
`host` - host of redis (default: localhost)
`port` - port of redis (default: 6379)
`password` - password of redis (default: no auth)
`selected` - list of selected metrics (default: select all)

Example config
==============
```yaml
---
interval: 10
loglevel: DEBUG
riemann:
  host: localhost
  port: 5555
agents:
  - name: consul
    module: oshino_consul.agent.ConsulAgent
    host: localhost
    port: 6379
    tag: db
```
