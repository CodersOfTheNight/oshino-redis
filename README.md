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
