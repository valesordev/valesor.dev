#!/usr/bin/env sh

curl -X POST \
  http://bridge.dsdemo.valesordev.com/topics/events \
  -H 'content-type: application/vnd.kafka.json.v2+json' \
  -d '{
    "records": [
        {
            "value": "test record value"
        }
    ]
}'

