import os

class Color:
    primary = 0x3EE2B7
    transparent = 0x2F3136
    blurple_old = 0x7289DA
    blurple = 0x5865F2
    danger = 0xE92323
    warning = 0xE9B623
    success = 0x44E923

class Auth:
    discord_auth = {
        "debug":"MTAyODQwMjY1NzU5NDk3NDI3OQ.GEMstc.qmRkZ-uKtoCI8IRLN8yJp5eTWWdKfkjcAlq0Y4",
        "release": "MTAyODMzNDkzNTQ4NTk4MDcwMg.GPLN1q.ixB-tuyksju8l51C8etX0hSo1rsibs9V9ymF74"
    }
    mongo_auth = {
        "url":"main.opwrf.mongodb.net",
        "username":"ArtemBay",
        "auth":{
            "debug":"YZaKp6M4IR6aYka6",
            "release": "YZaKp6M4IR6aYka6"
        }
    }
    qiwi_auth = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Im4wNHd6dy0wMCIsInVzZXJfaWQiOiI3OTUwNjgyOTc0MyIsInNlY3JldCI6ImU0OTNiODFmMjc4MzY4MTQwZTI2M2I5NTJlZWIzNDg2M2MyYTFhY2MzZjA5NDFmMjIwM2RjYzk0NjEzYTkyNzcifX0="

class Other:
    shard_count = 1
    slash = None
    premium_cost = 50
    invoice_lifetime = 360 # в минутах
    p2p = None
    uptime = 0