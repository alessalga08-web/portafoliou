import pygame
import random
import sys


# ==========================================
# INICIALIZAR PYGAME
# ==========================================

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load("arcade.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
except pygame.error:
    print(
        "Aviso: No se encontró 'arcade.mp3'. "
        "El juego iniciará en silencio."
    )


# ==========================================
# COLORES
# ==========================================

NEGRO = (0, 0, 0)
AMARILLO_PACMAN = (255, 255, 0)
ROJO_FANTASMA = (235, 51, 35)
AZUL_PARED = (17, 17, 219)
BLANCO_PUNTOS = (255, 184, 151)
TEXTO_COLOR = (255, 255, 255)


# ==========================================
# CONFIGURACIÓN INICIAL
# ==========================================

TAMANO_CELDA = 30

nivel = 1

ANCHO_COLS = 21
ALTO_FILAS = 15

ANCHO_VENTANA = ANCHO_COLS * TAMANO_CELDA
ALTO_VENTANA = ALTO_FILAS * TAMANO_CELDA + 50

ventana = pygame.display.set_mode(
    (ANCHO_VENTANA, ALTO_VENTANA)
)

pygame.display.set_caption(
    "Pac-Man Procedural Maze - Arcade Edition"
)

reloj = pygame.time.Clock()


# ==========================================
# GENERAR LABERINTO
# ==========================================

def generar_laberinto(cols, filas):
    laberinto = [
        [1 for _ in range(cols)]
        for _ in range(filas)
    ]

    def es_valido(r, c):
        return 0 <= r < filas and 0 <= c < cols

    stack = []

    inicio_r, inicio_c = 1, 1

    laberinto[inicio_r][inicio_c] = 0
    stack.append((inicio_r, inicio_c))

    while stack:
        r, c = stack[-1]

        direcciones = [
            (-2, 0),
            (0, 2),
            (2, 0),
            (0, -2)
        ]

        random.shuffle(direcciones)

        movimiento_encontrado = False

        for dr, dc in direcciones:
            vecino_r = r + dr
            vecino_c = c + dc

            if (
                es_valido(vecino_r, vecino_c)
                and laberinto[vecino_r][vecino_c] == 1
            ):
                laberinto[r + dr // 2][c + dc // 2] = 0
                laberinto[vecino_r][vecino_c] = 0

                stack.append((vecino_r, vecino_c))

                movimiento_encontrado = True
                break

        if not movimiento_encontrado:
            stack.pop()

    return laberinto


# ==========================================
# CONFIGURAR NIVEL
# ==========================================

def configurar_nivel():
    global laberinto
    global jugador_pos
    global rastro
    global meta_pos
    global movimientos
    global ANCHO_COLS
    global ALTO_FILAS
    global ANCHO_VENTANA
    global ALTO_VENTANA
    global ventana

    # A mayor nivel, mayor tamaño de cuadrícula
    ANCHO_COLS = 21 + (nivel - 1) * 2
    ALTO_FILAS = 15 + (nivel - 1) * 2

    # Límites máximos
    if ANCHO_COLS > 33:
        ANCHO_COLS = 33

    if ALTO_FILAS > 23:
        ALTO_FILAS = 23

    ANCHO_VENTANA = ANCHO_COLS * TAMANO_CELDA
    ALTO_VENTANA = ALTO_FILAS * TAMANO_CELDA + 50

    ventana = pygame.display.set_mode(
        (ANCHO_VENTANA, ALTO_VENTANA)
    )

    laberinto = generar_laberinto(
        ANCHO_COLS,
        ALTO_FILAS
    )

    jugador_pos = [1, 1]

    meta_pos = [
        ALTO_FILAS - 2,
        ANCHO_COLS - 2
    ]

    laberinto[1][1] = 0
    laberinto[meta_pos[0]][meta_pos[1]] = 0

    rastro = set()
    rastro.add(tuple(jugador_pos))

    movimientos = 0


# ==========================================
# VARIABLES DE ESTADO
# ==========================================

movimientos = 0

fuente = pygame.font.SysFont(
    "Arial",
    18,
    bold=True
)

configurar_nivel()


# ==========================================
# BUCLE PRINCIPAL
# ==========================================

ejecutando = True

while ejecutando:

    ventana.fill(NEGRO)

    # Manejo de eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.KEYDOWN:

            nuevo_r = jugador_pos[0]
            nuevo_c = jugador_pos[1]

            tecla_valida = False

            if (
                evento.key == pygame.K_UP
                or evento.key == pygame.K_w
            ):
                nuevo_r -= 1
                tecla_valida = True

            elif (
                evento.key == pygame.K_DOWN
                or evento.key == pygame.K_s
            ):
                nuevo_r += 1
                tecla_valida = True

            elif (
                evento.key == pygame.K_LEFT
                or evento.key == pygame.K_a
            ):
                nuevo_c -= 1
                tecla_valida = True

            elif (
                evento.key == pygame.K_RIGHT
                or evento.key == pygame.K_d
            ):
                nuevo_c += 1
                tecla_valida = True

            elif evento.key == pygame.K_r:
                configurar_nivel()

            # Conteo de pulsaciones válidas
            if tecla_valida:

                movimientos += 1

                if (
                    0 <= nuevo_r < ALTO_FILAS
                    and 0 <= nuevo_c < ANCHO_COLS
                ):

                    if laberinto[nuevo_r][nuevo_c] == 0:

                        jugador_pos = [
                            nuevo_r,
                            nuevo_c
                        ]

                        rastro.add(
                            tuple(jugador_pos)
                        )

                        # Llegada a la meta
                        if jugador_pos == meta_pos:

                            nivel += 1

                            configurar_nivel()


    # ==========================================
    # RENDERIZADO
    # ==========================================

    # Dibujar paredes y pasillos
    for r in range(ALTO_FILAS):

        for c in range(ANCHO_COLS):

            rect = pygame.Rect(
                c * TAMANO_CELDA,
                r * TAMANO_CELDA,
                TAMANO_CELDA,
                TAMANO_CELDA
            )

            if laberinto[r][c] == 1:

                pygame.draw.rect(
                    ventana,
                    AZUL_PARED,
                    rect,
                    border_radius=4
                )

            else:

                pygame.draw.rect(
                    ventana,
                    NEGRO,
                    rect
                )


    # Dibujar rastro
    for celda in rastro:

        r, c = celda

        if (
            [r, c] != jugador_pos
            and [r, c] != [1, 1]
        ):

            centro_x = (
                c * TAMANO_CELDA
                + TAMANO_CELDA // 2
            )

            centro_y = (
                r * TAMANO_CELDA
                + TAMANO_CELDA // 2
            )

            pygame.draw.circle(
                ventana,
                BLANCO_PUNTOS,
                (centro_x, centro_y),
                4
            )


    # Dibujar meta
    f_x = (
        meta_pos[1] * TAMANO_CELDA
        + TAMANO_CELDA // 2
    )

    f_y = (
        meta_pos[0] * TAMANO_CELDA
        + TAMANO_CELDA // 2
    )

    pygame.draw.circle(
        ventana,
        ROJO_FANTASMA,
        (f_x, f_y - 2),
        11
    )

    fantasma_cuerpo = pygame.Rect(
        f_x - 11,
        f_y - 2,
        22,
        13
    )

    pygame.draw.rect(
        ventana,
        ROJO_FANTASMA,
        fantasma_cuerpo
    )


    # Dibujar Pac-Man
    p_x = (
        jugador_pos[1] * TAMANO_CELDA
        + TAMANO_CELDA // 2
    )

    p_y = (
        jugador_pos[0] * TAMANO_CELDA
        + TAMANO_CELDA // 2
    )

    pygame.draw.circle(
        ventana,
        AMARILLO_PACMAN,
        (p_x, p_y),
        12
    )

    pygame.draw.circle(
        ventana,
        NEGRO,
        (p_x + 3, p_y - 4),
        2
    )


    # Panel de información
    panel_rect = pygame.Rect(
        0,
        ALTO_FILAS * TAMANO_CELDA,
        ANCHO_VENTANA,
        50
    )

    pygame.draw.rect(
        ventana,
        (10, 10, 15),
        panel_rect
    )

    texto_estado = fuente.render(
        f"Nivel: {nivel} | "
        f"Clics: {movimientos} | "
        f"W,A,S,D / Flechas",
        True,
        TEXTO_COLOR
    )

    ventana.blit(
        texto_estado,
        (
            15,
            ALTO_FILAS * TAMANO_CELDA + 15
        )
    )

    pygame.display.flip()

    reloj.tick(60)


pygame.quit()
sys.exit()