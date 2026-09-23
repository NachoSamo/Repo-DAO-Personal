import pytest

from solucion import Envio, EnvioComun, EnvioExpress


def test_envio_comun_conserva_costo_base():
    envio = EnvioComun(
        1,
        "Cordoba",
        5.0,
        10000.0
    )

    assert isinstance(envio, Envio)
    assert envio.importe_final() == pytest.approx(10000.0)


def test_envio_express_aplica_recargo_del_30_por_ciento():
    envio = EnvioExpress(
        2,
        "Rosario",
        8.0,
        10000.0
    )

    assert isinstance(envio, Envio)
    assert envio.importe_final() == pytest.approx(13000.0)