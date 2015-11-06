# ionicio
Django module for ionic.io

```python
#settings.py

IONICPUSH_APP_ID = "xxxxxx"
IONICPUSH_PRIVATE_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```python
#another file in django

from ionicio import IonicPush

IonicPush.send(tokens, 'Message')
```

```python
#without django

from ionicio import IonicPush

IonicPush.config(IONICPUSH_APP_ID, IONICPUSH_PRIVATE_KEY)

IonicPush.send(tokens, 'Message')
```

Ionic Push Docs http://docs.ionic.io/docs/push-sending-push
