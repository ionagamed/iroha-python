from iroha import Iroha, IrohaCrypto, IrohaGrpc, IrohaTlsOptions

iroha = Iroha("admin@test")
net = IrohaGrpc("localhost:50052", enable_tls=True,
                tls_options=IrohaTlsOptions.from_files(
                    "/opt/iroha/example/torii_tls/server.crt"))

# this is a sample private key from hyperledger/iroha repo
admin_private_key = "f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70"
admin_qry = iroha.query("GetAccount", account_id="admin@test")
IrohaCrypto.sign_query(admin_qry, admin_private_key)

response = net.send_query(admin_qry)

print(response)
