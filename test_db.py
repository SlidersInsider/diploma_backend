# import pymysql
#
# host = "80.87.104.185"
# user = "test"
# password = "test"
# database = "diploma"
#
# try:
#     conn = pymysql.connect(host=host, user=user, password=password, database=database)
#     print("✅ Подключение успешно!")
#     conn.close()
# except Exception as e:
#     print("❌ Ошибка подключения:", e)


from Crypto.PublicKey import RSA

# Генерация ключа (2048 бит — рекомендуется для безопасности)
key = RSA.generate(2048)

# Приватный ключ
private_key = key.export_key().decode()  # Экспортируем как строку

# Публичный ключ
public_key = key.publickey().export_key().decode()  # Экспортируем как строку

print("🔑 Приватный ключ RSA:")
print(private_key)

print("\n🔓 Публичный ключ RSA:")
print(public_key)

#
# 🔑 Приватный ключ RSA:
# -----BEGIN RSA PRIVATE KEY-----
# MIIEowIBAAKCAQEAucrIn4fM3ANSMAJUnD64CHCwUFI1nIFE/SshMcU75xniuQQN
# 9AETz4kUPg4a0AL/i32AWCpJ1/KxsPd3wRPcbs2bDxmbbRC8pgrRzitzZLxGrRtv
# utl83TJq0Gx/0wxNv9JDPlmkPsqrVX9o6b64L67RqdMCWXHdiEY/aqNK8J9Pcyny
# 94eaW6pvl7pPz+U3DYuCH9QwwOIsY4EN/Mih6uQXPxCFcWv3XV3MA14YpQb7otwr
# u3A74RLuMYZYQE56d4FQRPcELxhr32/0Vm/EoNx8AnGe1ZXmsiuswHWK2v8kgeIb
# 4yyPnwe4qABCyIq5SJXdzhiXIVGOqYYPrHZOywIDAQABAoIBAACzJ2m7kBMfgl11
# EoEWcj+V4++OFpNSoC/mObCkBGgIJ8lTw7mwtRAcNBK+n22ElV+MkFPEsHA7OcuM
# R6cyh2IICM18nX3U0k7Nzeo45D+GCFBnwOiOsk5HkA0mpJ3CUq04lGOw4HalOn/8
# hAQUPPjMb8bhsk5IhBY/UhAd6MXIZHddnLZIhWT/qmGhj1ivoPtxw6U3sEt4Xi8c
# 37zR9TlC3GK4Cxuls6XX/Tx9Ogb4oBtGyTQyv/jIFJRNQvXyHaM9lWCdOaegk22y
# e+aSTCIb5rTalWxdjNYNsaZlB4qINlV5K9nymLAFABfr6Fr35J/3trUUtLpBEFeg
# ZXSNygECgYEAvxNChJKBGoqExD0kQJjmMgC87JXGw4aDXeuxwhgSb1V9Zolaq2R+
# vu2nP+aDI55qLr/qbKPxCb1rfj/rpRdkCoSg2Ik9sQ17oXn+JrOiYEnCAIKv2UWt
# VaLL87XFSGhIc/ulttk6XFY7dLpfWa8r0aDG/h6dB02LxK+U9jIj2a0CgYEA+Ov4
# iStzRyE7pUS4mew0/k6zFWj3Hhmu3mn4yPOLyCJZuSVD9Qm3btVsPfyr5zDmDZSv
# eHEGuSTI/S1TKxfMpac9dNyUmfNygrSlesN8XWZ5owMo5EgVivPceYrfb/CZWNm2
# R7r2lCCHaE44U78J/lGH85oqR2yU38dl506pSVcCgYA5d9J2yxV3ZRf/aaBAqXv6
# qAwqX/XTEt7p3ZyuEs1gnObFcyRJDkWsqQ+3gV4J1Xh8LQ6VtE0nr8fnxdPa6IkX
# PMKfvc9HNBXuACH3g+mfai+mNagsAe/bJMaQuyfl2i+IarRxpS4PXYQuXGuXLr9Q
# IjoXbh+udZ1G/8Qes//iVQKBgQDNbrncQv7NmlDGcbPEXJvTsZG8vrcLoXifWGgZ
# OF6JWkggM/Ak39MCZqMBeXFJySJj3O0AAo/g5sn1oJ19+BNON3rR4mXFtJQx6PKV
# IZaW4sbKUQZDeHZHCkFQEdubX76/BFaaVmPAFiSKYdu8yfJucE06L2ZrMeKf2Mly
# H4o42wKBgF8F9uO15vo2CzOhxiSvvdYhsL35nuPy3QziY98x/6SdP6MVIKN0hy6l
# cOPQtzRq2QEfPmhQb2S72zTxxm5PNl14JqPUonks/h/QaQq4SoaDlBd7iXsecrO2
# Jzcmu8/jItePdmt1TvTehvZ2dT2T2MAz9wx3Aa+nZ6T9QMvj3eGD
# -----END RSA PRIVATE KEY-----
#
# 🔓 Публичный ключ RSA:
# -----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAucrIn4fM3ANSMAJUnD64
# CHCwUFI1nIFE/SshMcU75xniuQQN9AETz4kUPg4a0AL/i32AWCpJ1/KxsPd3wRPc
# bs2bDxmbbRC8pgrRzitzZLxGrRtvutl83TJq0Gx/0wxNv9JDPlmkPsqrVX9o6b64
# L67RqdMCWXHdiEY/aqNK8J9Pcyny94eaW6pvl7pPz+U3DYuCH9QwwOIsY4EN/Mih
# 6uQXPxCFcWv3XV3MA14YpQb7otwru3A74RLuMYZYQE56d4FQRPcELxhr32/0Vm/E
# oNx8AnGe1ZXmsiuswHWK2v8kgeIb4yyPnwe4qABCyIq5SJXdzhiXIVGOqYYPrHZO
# ywIDAQAB
# -----END PUBLIC KEY-----