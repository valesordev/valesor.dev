# Valesor Development Application

The core application for Valesor Development is one that combines an automated mentor with a system for ingesting and 
processing external news feeds. This application is built with a test first and an observability first mindset.

## Testing

curl -X POST \
  http://bridge.dsdemo.valesordev.com/topics/events \
  -H 'content-type: application/vnd.kafka.json.v2+json' \
  -d '{
    "records": [
        {
            "key": "testrecord",
            "value": "test record value"
        }
    ]
}'

