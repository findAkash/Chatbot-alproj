# Endpoint

http://localhost:5005/webhooks/rest/webhook

### test

```
curl --request POST \
     --url http://localhost:5005/webhooks/rest/webhook \
     --header 'Content-Type: application/json' \
     --data '{
            "sender": "test_user",
            "message": "Hi there!",
            "metadata": {}
          }'
```
