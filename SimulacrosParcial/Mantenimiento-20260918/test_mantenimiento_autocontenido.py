"""Suite basica autocontenida del ejercicio Mantenimiento.
Uso:
    pytest tests/test_mantenimiento_autocontenido.py -v
    python  tests/test_mantenimiento_autocontenido.py
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
# Bootstrap: agrega la raiz del proyecto (la carpeta Mantenimiento) al sys.path
# para que los modulos se importen igual que lo hace main.py.
# ---------------------------------------------------------------------------


def _raiz_proyecto() -> Path:
    """Busca hacia arriba la carpeta que contiene los modulos del ejercicio."""
    for carpeta in [Path(__file__).resolve().parent, *Path(__file__).resolve().parents]:
        if (carpeta / "maquina.py").is_file() and (
            carpeta / "mantenimiento.py"
        ).is_file():
            return carpeta
    raise RuntimeError(
        "No se encontro la raiz del proyecto (maquina.py / mantenimiento.py) "
        f"partiendo de {Path(__file__).resolve()}"
    )


RAIZ_PROYECTO: Path = _raiz_proyecto()
if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROYECTO))

import main
from Correctivo import Correctivo
from Mantenimiento import Mantenimiento
from Maquina import Maquina
from Preventivo import Preventivo

# ---------------------------------------------------------------------------
# Valores numericos del enunciado (antes eran enums)
# ---------------------------------------------------------------------------

FUNCIONA_CORRECTAMENTE, REVISION_RECOMENDADA, ROTURA = 1, 2, 3

# ---------------------------------------------------------------------------
# Fixtures (equivalentes a las de tests/conftest.py)
# ---------------------------------------------------------------------------


@pytest.fixture
def maquina_vacia() -> Maquina:
    return Maquina("Maquina Manufacturera")


@pytest.fixture
def un_preventivo() -> Preventivo:
    return Preventivo("Juan Perez", "4/7", 1000.0, 500.0, FUNCIONA_CORRECTAMENTE)


@pytest.fixture
def un_correctivo() -> Correctivo:
    return Correctivo("Ana Diaz", "8/1", 1000.0, 5, 2000.0)


def preventivo(
    fecha: str,
    importe_repuestos: float,
    importe_insumos: float,
    resultado: int = FUNCIONA_CORRECTAMENTE,
) -> Preventivo:
    """Mantenimiento preventivo de prueba."""
    return Preventivo(
        "Juan Perez", fecha, importe_repuestos, importe_insumos, resultado
    )


def correctivo(
    fecha: str, importe_repuestos: float, horas_parada: int, importe_tecnico: float
) -> Correctivo:
    """Mantenimiento correctivo de prueba."""
    return Correctivo(
        "Ana Diaz", fecha, importe_repuestos, horas_parada, importe_tecnico
    )


# ---------------------------------------------------------------------------
# Preventivo: constructor, acceso, modificacion y toString
# ---------------------------------------------------------------------------


class TestPreventivo:
    def test_constructor_registra_los_datos_del_mantenimiento(self) -> None:
        mantenimiento = Preventivo("Juan Perez", "4/7", 1000.0, 500.0, ROTURA)

        assert mantenimiento.operario == "Juan Perez"
        assert mantenimiento.fecha == "4/7"
        assert mantenimiento.importe_repuestos == 1000.0
        assert mantenimiento.importe_insumos == 500.0
        assert mantenimiento.resultado == ROTURA

    def test_es_un_mantenimiento(self) -> None:
        assert issubclass(Preventivo, Mantenimiento)

    def test_mantenimiento_es_abstracto(self) -> None:
        with pytest.raises(TypeError):
            Mantenimiento("Juan Perez", "4/7", 1000.0)

    @pytest.mark.parametrize(
        "resultado", [FUNCIONA_CORRECTAMENTE, REVISION_RECOMENDADA, ROTURA]
    )
    def test_los_resultados_del_enunciado_son_validos(self, resultado: int) -> None:
        mantenimiento = Preventivo("Juan Perez", "4/7", 1000.0, 500.0, resultado)

        assert mantenimiento.resultado == resultado

    @pytest.mark.parametrize("resultado", [0, 4])
    def test_un_resultado_entero_fuera_del_enunciado_es_rechazado(
        self, resultado: int
    ) -> None:
        with pytest.raises(ValueError):
            Preventivo("Juan Perez", "4/7", 1000.0, 500.0, resultado)

    def test_un_resultado_que_no_es_entero_es_rechazado(self) -> None:
        with pytest.raises(TypeError):
            Preventivo("Juan Perez", "4/7", 1000.0, 500.0, "rotura")

    def test_gasto_total_suma_repuestos_e_insumos(self) -> None:
        mantenimiento = Preventivo(
            "Juan Perez", "4/7", 1000.0, 500.0, FUNCIONA_CORRECTAMENTE
        )

        assert mantenimiento.gasto_total() == pytest.approx(1500.0)

    def test_modificacion_de_los_datos(self, un_preventivo: Preventivo) -> None:
        un_preventivo.operario = "Marta Gomez"
        un_preventivo.fecha = "1/1"
        un_preventivo.importe_repuestos = 2000.0
        un_preventivo.importe_insumos = 800.0
        un_preventivo.resultado = ROTURA

        assert un_preventivo.operario == "Marta Gomez"
        assert un_preventivo.fecha == "1/1"
        assert un_preventivo.importe_repuestos == 2000.0
        assert un_preventivo.importe_insumos == 800.0
        assert un_preventivo.resultado == ROTURA

    def test_to_string_incluye_operario_y_gasto_total(
        self, un_preventivo: Preventivo
    ) -> None:
        cadena: str = str(un_preventivo)

        assert "Juan Perez" in cadena
        assert "1500.0" in cadena


# ---------------------------------------------------------------------------
# Correctivo: constructor, acceso, modificacion y toString
# ---------------------------------------------------------------------------


class TestCorrectivo:
    def test_constructor_registra_los_datos_del_mantenimiento(self) -> None:
        mantenimiento = Correctivo("Ana Diaz", "8/1", 1000.0, 5, 2000.0)

        assert mantenimiento.operario == "Ana Diaz"
        assert mantenimiento.fecha == "8/1"
        assert mantenimiento.importe_repuestos == 1000.0
        assert mantenimiento.horas_parada == 5
        assert mantenimiento.importe_tecnico == 2000.0

    def test_es_un_mantenimiento(self) -> None:
        assert issubclass(Correctivo, Mantenimiento)

    def test_gasto_total_suma_repuestos_y_tecnico(self) -> None:
        mantenimiento = Correctivo("Ana Diaz", "8/1", 1000.0, 5, 2000.0)

        assert mantenimiento.gasto_total() == pytest.approx(3000.0)

    def test_modificacion_de_los_datos(self, un_correctivo: Correctivo) -> None:
        un_correctivo.operario = "Marta Gomez"
        un_correctivo.fecha = "1/1"
        un_correctivo.importe_repuestos = 2000.0
        un_correctivo.horas_parada = 10
        un_correctivo.importe_tecnico = 3000.0

        assert un_correctivo.operario == "Marta Gomez"
        assert un_correctivo.fecha == "1/1"
        assert un_correctivo.importe_repuestos == 2000.0
        assert un_correctivo.horas_parada == 10
        assert un_correctivo.importe_tecnico == 3000.0

    def test_to_string_incluye_operario_y_gasto_total(
        self, un_correctivo: Correctivo
    ) -> None:
        cadena: str = str(un_correctivo)

        assert "Ana Diaz" in cadena
        assert "3000.00" in cadena


# ---------------------------------------------------------------------------
# Maquina: coleccion de mantenimientos y metodos del enunciado
# ---------------------------------------------------------------------------


class TestMaquina:
    def test_constructor_registra_nombre_y_coleccion_vacia(self) -> None:
        maquina = Maquina("Maquina Manufacturera")

        assert maquina.nombre == "Maquina Manufacturera"
        assert maquina.mantenimientos == []

    def test_add_mantenimiento_agrega_a_la_coleccion(
        self,
        maquina_vacia: Maquina,
        un_preventivo: Preventivo,
        un_correctivo: Correctivo,
    ) -> None:
        maquina_vacia.add_mantenimiento(un_preventivo)
        maquina_vacia.add_mantenimiento(un_correctivo)

        assert maquina_vacia.mantenimientos == [un_preventivo, un_correctivo]

    def test_suma_gastos_suma_el_gasto_total_de_todos_los_mantenimientos(
        self, maquina_vacia: Maquina
    ) -> None:
        maquina_vacia.add_mantenimiento(preventivo("4/7", 1000.0, 500.0))
        maquina_vacia.add_mantenimiento(correctivo("8/1", 1000.0, 5, 2000.0))

        assert maquina_vacia.suma_gastos() == pytest.approx(4500.0)

    def test_suma_gastos_sin_mantenimientos_es_cero(
        self, maquina_vacia: Maquina
    ) -> None:
        assert maquina_vacia.suma_gastos() == pytest.approx(0.0)

    def test_cantidad_mantenimientos_caros_cuenta_los_que_superan_10000(
        self, maquina_vacia: Maquina
    ) -> None:
        maquina_vacia.add_mantenimiento(preventivo("4/7", 6000.0, 5000.0))  # 11000 caro
        maquina_vacia.add_mantenimiento(
            preventivo("8/1", 1000.0, 500.0)
        )  # 1500 no caro
        maquina_vacia.add_mantenimiento(
            correctivo("6/9", 8000.0, 5, 3000.0)
        )  # 11000 caro

        assert maquina_vacia.cantidad_mantenimientos_caros() == 2

    def test_cantidad_mantenimientos_caros_sin_mantenimientos_es_cero(
        self, maquina_vacia: Maquina
    ) -> None:
        assert maquina_vacia.cantidad_mantenimientos_caros() == 0

    def test_rotura_mas_larga_devuelve_el_correctivo_de_mas_horas(
        self, maquina_vacia: Maquina
    ) -> None:
        maquina_vacia.add_mantenimiento(preventivo("4/7", 1000.0, 500.0))
        maquina_vacia.add_mantenimiento(correctivo("8/1", 1000.0, 5, 2000.0))
        mas_larga: Correctivo = correctivo("21/1", 500.0, 20, 3000.0)
        maquina_vacia.add_mantenimiento(mas_larga)
        maquina_vacia.add_mantenimiento(correctivo("6/9", 900.0, 10, 1000.0))

        assert maquina_vacia.rotura_mas_larga() is mas_larga

    def test_rotura_mas_larga_sin_correctivos_devuelve_none(
        self, maquina_vacia: Maquina
    ) -> None:
        maquina_vacia.add_mantenimiento(preventivo("4/7", 1000.0, 500.0))

        assert maquina_vacia.rotura_mas_larga() is None

    def test_rotura_mas_larga_sin_mantenimientos_devuelve_none(
        self, maquina_vacia: Maquina
    ) -> None:
        assert maquina_vacia.rotura_mas_larga() is None

    def test_to_string_incluye_el_nombre_y_los_mantenimientos(
        self, maquina_vacia: Maquina, un_preventivo: Preventivo
    ) -> None:
        maquina_vacia.add_mantenimiento(un_preventivo)
        cadena: str = str(maquina_vacia)

        assert "Maquina Manufacturera" in cadena
        assert "Juan Perez" in cadena


# ---------------------------------------------------------------------------
# main.py: carga del archivo CSV de data/
# ---------------------------------------------------------------------------


class TestCargaCsv:
    def test_se_cargan_99_mantenimientos(self) -> None:
        mantenimientos: list[Mantenimiento] = main.cargar_mantenimientos()

        assert len(mantenimientos) == 99
        assert all(
            isinstance(mantenimiento, Mantenimiento) for mantenimiento in mantenimientos
        )

    def test_la_maquina_queda_cargada_con_los_99_mantenimientos(self) -> None:
        maquina: Maquina = main.cargar_maquina()

        assert len(maquina.mantenimientos) == 99

    def test_crear_mantenimiento_preventivo_desde_una_fila(self) -> None:
        fila: list[str] = ["1", "4/7", "MARIA ROSARIO", "15300", "2", "4700"]
        mantenimiento: Mantenimiento = main.crear_mantenimiento(fila)

        assert isinstance(mantenimiento, Preventivo)
        assert mantenimiento.operario == "MARIA ROSARIO"
        assert mantenimiento.resultado == REVISION_RECOMENDADA
        assert mantenimiento.importe_insumos == 4700.0

    def test_crear_mantenimiento_correctivo_desde_una_fila(self) -> None:
        fila: list[str] = ["2", "21/1", "ANA BELEN", "400", "7", "15300"]
        mantenimiento: Mantenimiento = main.crear_mantenimiento(fila)

        assert isinstance(mantenimiento, Correctivo)
        assert mantenimiento.operario == "ANA BELEN"
        assert mantenimiento.horas_parada == 7
        assert mantenimiento.importe_tecnico == 15300.0

    def test_crear_mantenimiento_con_tipo_invalido_lanza_error(self) -> None:
        fila: list[str] = ["3", "4/7", "MARIA ROSARIO", "15300", "2", "4700"]

        with pytest.raises(ValueError):
            main.crear_mantenimiento(fila)


# ---------------------------------------------------------------------------
# Permite ejecutar el archivo directamente: python test_mantenimiento_autocontenido.py
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-p", "no:cacheprovider"]))
