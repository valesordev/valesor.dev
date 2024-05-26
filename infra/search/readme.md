Loki has been configured with a gateway (nginx) to support reads and writes from a single component.

You can send logs from inside the cluster using the cluster DNS:

http://search-loki-gateway.search.svc.cluster.local/loki/api/v1/push

You can test to send data from outside the cluster by port-forwarding the gateway to your local machine:

  kubectl port-forward --namespace search svc/search-loki-gateway 3100:80 &

Or you can add the hostname `loki.dsdemo.valesordev.com` to your `/etc/hosts` and use the nginx ingress

And then using http://127.0.0.1:3100/loki/api/v1/push URL as shown below:

```
curl -H "Content-Type: application/json" -XPOST -s "http://loki.dsdemo.valesordev.com/loki/api/v1/push"  \
--data-raw "{\"streams\": [{\"stream\": {\"job\": \"test\"}, \"values\": [[\"$(date +%s)000000000\", \"fizzbuzz\"]]}]}"
```

Then verify that Loki did received the data using the following command:

```
curl "http://loki.dsdemo.valesordev.com/loki/api/v1/query_range" --data-urlencode 'query={job="test"}' | jq .data.result
```