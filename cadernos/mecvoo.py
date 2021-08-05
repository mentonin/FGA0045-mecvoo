import sympy as sp


pi = sp.pi


def rad(ang):
    """
    Transforma um ângulo em graus para radianos com SymPy
    """
    return ang * pi / 180


def deg(ang):
    """
    Transforma um ângulo em radianos para graus com SymPy
    """
    return 180 * ang / pi


def math(latex_code: str):
    """
    Exibe uma string com código latex em ambiente matemático
    """
    from IPython.display import display, Math

    return display(Math(latex_code))


def text(latex_code: str):
    """
    Exibe uma string com código latex
    """
    from IPython.display import display, Latex

    return display(Latex(latex_code))


def vector(components, frame):
    """
    Constrói um vetor com componentes 'components' no sistema de referências 'frame'
    """
    return components[0] * frame.x + components[1] * frame.y + components[2] * frame.z
