"""Suite basica autocontenida del ejercicio Empresa de Transporte.
Uso:
    pytest tests/test_empresa_autocontenido.py -v
    python  tests/test_empresa_autocontenido.py
"""

# Existen dos tests que instancian una clase abstracta y pasan un tipo invalido a
# proposito para comprobar que el error se produce en tiempo de ejecucion; no
# hay forma de tipar esos llamados sin dejar de probar ese comportamiento.
# pyright: reportAbstractUsage=false
# pyright: reportArgumentType=false

import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Bootstrap: agrega la raiz del proyecto (la carpeta Empresa) al sys.path para
# que los modulos se importen igual que lo hace main.py.
# ---------------------------------------------------------------------------


def _raiz_proyecto() -> Path:
    """Busca hacia arriba la carpeta que contiene los modulos del ejercicio."""
    for carpeta in [Path(__file__).resolve().parent, *Path(__file__).resolve().parents]:
        if (carpeta / "camion.py").is_file() and (carpeta / "carga.py").is_file():
            return carpeta
    raise RuntimeError(
        "No se encontro la raiz del proyecto (camion.py / carga.py) "
        f"partiendo de {Path(__file__).resolve()}"
    )


RAIZ_PROYECTO: Path = _raiz_proyecto()
if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROYECTO))

import main
from Bidon import Bidon
from Caja import Caja
from Camion import Camion
from Carga import Carga
from Packing import Packing

# ---------------------------------------------------------------------------
# Fixtures (equivalentes a las de tests/conftest.py)
# ---------------------------------------------------------------------------


@pytest.fixture
def una_caja() -> Caja:
    return Caja("Yogur", 4.0)


@pytest.fixture
def un_packing() -> Packing:
    return Packing("Cerveza en pack", 4.0, 4, 2.0)


@pytest.fixture
def un_bidon() -> Bidon:
    return Bidon("Aceite de oliva", 5.0, 1.34)


@pytest.fixture
def un_camion() -> Camion:
    return Camion("AA001AA", 100.0)


def caja(contenido: str, peso: float) -> Caja:
    """Caja de prueba."""
    return Caja(contenido, peso)


def bidon(contenido: str, capacidad: float, densidad: float) -> Bidon:
    """Bidon de prueba."""
    return Bidon(contenido, capacidad, densidad)


def camion(patente: str, carga_maxima: float) -> Camion:
    """Camion de prueba."""
    return Camion(patente, carga_maxima)


# ---------------------------------------------------------------------------
# Caja: constructor, acceso, modificacion, toString y peso
# ---------------------------------------------------------------------------


class TestCaja:
    def test_constructor_registra_los_datos_de_la_caja(self) -> None:
        una_caja = Caja("Yogur", 4.0)

        assert una_caja.contenido == "Yogur"
        assert una_caja.peso() == 4.0

    def test_es_una_carga(self) -> None:
        assert issubclass(Caja, Carga)

    def test_carga_es_abstracta(self) -> None:
        with pytest.raises(TypeError):
            Carga("Yogur")

    def test_modificacion_del_contenido(self, una_caja: Caja) -> None:
        una_caja.contenido = "Pollo"

        assert una_caja.contenido == "Pollo"

    def test_to_string_incluye_contenido_y_peso(self, una_caja: Caja) -> None:
        cadena: str = str(una_caja)

        assert "Yogur" in cadena
        assert "4.00" in cadena


# ---------------------------------------------------------------------------
# Packing: constructor, acceso, modificacion, toString y peso
# ---------------------------------------------------------------------------


class TestPacking:
    def test_constructor_registra_los_datos_del_packing(self) -> None:
        un_packing = Packing("Cerveza en pack", 4.0, 4, 2.0)

        assert un_packing.contenido == "Cerveza en pack"
        assert un_packing.peso_por_caja == 4.0
        assert un_packing.cantidad == 4
        assert un_packing.peso_estructura == 2.0

    def test_es_una_carga(self) -> None:
        assert issubclass(Packing, Carga)

    def test_peso_es_peso_por_caja_por_cantidad_mas_estructura(self) -> None:
        un_packing = Packing("Cerveza en pack", 4.0, 4, 2.0)

        assert un_packing.peso() == pytest.approx(18.0)

    def test_modificacion_de_los_datos(self, un_packing: Packing) -> None:
        un_packing.contenido = "Latas de conservas en pack"
        un_packing.peso_por_caja = 2.0
        un_packing.cantidad = 10
        un_packing.peso_estructura = 3.0

        assert un_packing.contenido == "Latas de conservas en pack"
        assert un_packing.peso_por_caja == 2.0
        assert un_packing.cantidad == 10
        assert un_packing.peso_estructura == 3.0
        assert un_packing.peso() == pytest.approx(23.0)

    def test_to_string_incluye_contenido_y_peso(self, un_packing: Packing) -> None:
        cadena: str = str(un_packing)

        assert "Cerveza en pack" in cadena
        assert "18.00" in cadena


# ---------------------------------------------------------------------------
# Bidon: constructor, acceso, modificacion, toString y peso
# ---------------------------------------------------------------------------


class TestBidon:
    def test_constructor_registra_los_datos_del_bidon(self) -> None:
        un_bidon = Bidon("Aceite de oliva", 5.0, 1.34)

        assert un_bidon.contenido == "Aceite de oliva"
        assert un_bidon.capacidad == 5.0
        assert un_bidon.densidad == 1.34

    def test_es_una_carga(self) -> None:
        assert issubclass(Bidon, Carga)

    def test_peso_es_capacidad_por_densidad(self) -> None:
        un_bidon = Bidon("Aceite de oliva", 5.0, 2.0)

        assert un_bidon.peso() == pytest.approx(10.0)

    def test_modificacion_de_los_datos(self, un_bidon: Bidon) -> None:
        un_bidon.contenido = "Vino tinto"
        un_bidon.capacidad = 4.0
        un_bidon.densidad = 1.24

        assert un_bidon.contenido == "Vino tinto"
        assert un_bidon.capacidad == 4.0
        assert un_bidon.densidad == 1.24

    def test_to_string_incluye_contenido_y_peso(self, un_bidon: Bidon) -> None:
        cadena: str = str(un_bidon)

        assert "Aceite de oliva" in cadena
        assert "6.70" in cadena


# ---------------------------------------------------------------------------
# Camion: coleccion de cargas, estados y metodos del enunciado
# ---------------------------------------------------------------------------


class TestCamion:
    def test_constructor_registra_patente_estado_y_coleccion_vacia(self) -> None:
        un_camion = Camion("AA001AA", 100.0)

        assert un_camion.patente == "AA001AA"
        assert un_camion.carga_maxima == 100.0
        assert un_camion.estado == Camion.DISPONIBLE
        assert un_camion.cargas == []

    def test_subir_carga_agrega_a_la_coleccion(
        self, un_camion: Camion, una_caja: Caja
    ) -> None:
        un_camion.subir_carga(una_caja)

        assert un_camion.cargas == [una_caja]

    def test_subir_carga_con_tipo_invalido_es_rechazada(
        self, un_camion: Camion
    ) -> None:
        with pytest.raises(TypeError):
            un_camion.subir_carga("no es una carga")

    def test_subir_carga_que_supera_la_carga_maxima_lanza_error(self) -> None:
        un_camion = camion("AA001AA", 10.0)

        with pytest.raises(ValueError):
            un_camion.subir_carga(caja("Yogur", 20.0))

    def test_bajar_carga_quita_de_la_coleccion(
        self, un_camion: Camion, una_caja: Caja
    ) -> None:
        un_camion.subir_carga(una_caja)
        un_camion.bajar_carga(una_caja)

        assert un_camion.cargas == []

    def test_bajar_carga_con_el_camion_no_disponible_lanza_error(
        self, un_camion: Camion, una_caja: Caja
    ) -> None:
        un_camion.subir_carga(una_caja)
        un_camion.a_reparacion()

        with pytest.raises(ValueError):
            un_camion.bajar_carga(una_caja)

    def test_bajar_carga_no_presente_lanza_error(
        self, un_camion: Camion, una_caja: Caja
    ) -> None:
        with pytest.raises(ValueError):
            un_camion.bajar_carga(una_caja)

    def test_cantidad_cargas_y_peso_cargas(self, un_camion: Camion) -> None:
        un_camion.subir_carga(caja("Yogur", 4.0))
        un_camion.subir_carga(caja("Pollo", 6.0))

        assert un_camion.cantidad_cargas() == 2
        assert un_camion.peso_cargas() == pytest.approx(10.0)

    def test_a_reparacion_y_sale_reparado_cambian_el_estado(
        self, un_camion: Camion
    ) -> None:
        un_camion.a_reparacion()
        assert un_camion.estado == Camion.REPARACION

        un_camion.sale_reparado()
        assert un_camion.estado == Camion.DISPONIBLE

    def test_en_viaje_y_de_regreso_cambian_el_estado(self, un_camion: Camion) -> None:
        un_camion.en_viaje()
        assert un_camion.estado == Camion.VIAJE

        un_camion.de_regreso()
        assert un_camion.estado == Camion.DISPONIBLE

    def test_listo_para_salir_cuando_alcanza_el_75_por_ciento(self) -> None:
        un_camion = camion("AA001AA", 100.0)
        un_camion.subir_carga(caja("Yogur", 75.0))

        assert un_camion.listo_para_salir() is True

    def test_no_listo_para_salir_si_no_alcanza_el_75_por_ciento(self) -> None:
        un_camion = camion("AA001AA", 100.0)
        un_camion.subir_carga(caja("Yogur", 50.0))

        assert un_camion.listo_para_salir() is False

    def test_no_listo_para_salir_si_no_esta_disponible(self, un_camion: Camion) -> None:
        un_camion.subir_carga(caja("Yogur", 90.0))
        un_camion.en_viaje()

        assert un_camion.listo_para_salir() is False

    def test_cargas_en_orden_incluye_las_cargas_cargadas(
        self, un_camion: Camion, una_caja: Caja
    ) -> None:
        un_camion.subir_carga(una_caja)

        assert "Yogur" in un_camion.cargas_en_orden()

    def test_to_string_incluye_patente_y_estado(self, un_camion: Camion) -> None:
        cadena: str = str(un_camion)

        assert "AA001AA" in cadena
        assert "disponible" in cadena


# ---------------------------------------------------------------------------
# main.py: carga de los archivos CSV de data/
# ---------------------------------------------------------------------------


class TestCargaCsv:
    def test_se_cargan_20_bidones(self) -> None:
        bidones: list[Bidon] = main.cargar_bidones()

        assert len(bidones) == 20
        assert all(isinstance(un_bidon, Bidon) for un_bidon in bidones)

    def test_se_cargan_20_cajas(self) -> None:
        cajas: list[Caja] = main.cargar_cajas()

        assert len(cajas) == 20
        assert all(isinstance(una_caja, Caja) for una_caja in cajas)

    def test_se_cargan_10_packings(self) -> None:
        packings: list[Packing] = main.cargar_packings()

        assert len(packings) == 10
        assert all(isinstance(un_packing, Packing) for un_packing in packings)

    def test_se_cargan_50_cargas_en_total(self) -> None:
        cargas: list[Carga] = main.cargar_todas_las_cargas()

        assert len(cargas) == 50

    def test_crear_camiones_devuelve_camiones_disponibles_y_sin_cargas(self) -> None:
        camiones: list[Camion] = main.crear_camiones()

        assert len(camiones) == 3
        assert all(un_camion.estado == Camion.DISPONIBLE for un_camion in camiones)
        assert all(un_camion.cantidad_cargas() == 0 for un_camion in camiones)

    def test_distribuir_cargas_no_supera_la_carga_maxima_de_ningun_camion(
        self,
    ) -> None:
        camiones: list[Camion] = main.crear_camiones()
        cargas: list[Carga] = main.cargar_todas_las_cargas()
        main.distribuir_cargas(camiones, cargas)

        assert all(
            un_camion.peso_cargas() <= un_camion.carga_maxima for un_camion in camiones
        )


# ---------------------------------------------------------------------------
# Permite ejecutar el archivo directamente: python test_empresa_autocontenido.py
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-p", "no:cacheprovider"]))
