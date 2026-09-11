class Cuenta:
    def __init__(self, nro_cuenta, saldo):
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo

    def consultarSaldo(self):
        return self.saldo        