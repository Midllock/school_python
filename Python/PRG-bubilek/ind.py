class Graph:
    def __init__(self, n: int) -> None:
        """Inicializace matice sousednosti n x n vyplněné nulami."""
        self.n: int = n
        self.matrix: list[list[int]] = [[0] * n for _ in range(n)]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Nastaví orientovanou hranu z uzlu u do uzlu v s danou vahou."""
        if 0 <= u < self.n and 0 <= v < self.n:
            self.matrix[u][v] = weight
        else:
            print(f"Chyba: Neplatný index uzlu ({u} nebo {v})!")

    def remove_edge(self, u: int, v: int) -> None:
        """Odstraní hranu u -> v (nastaví váhu zpět na 0)."""
        self.add_edge(u, v, weight=0)

    def get_edge(self, u: int, v: int) -> int:
        """Vrátí váhu hrany u -> v (nebo 0, pokud neexistuje)."""
        if 0 <= u < self.n and 0 <= v < self.n:
            return self.matrix[u][v]
        return 0

    def has_edge(self, u: int, v: int) -> bool:
        """Vrátí True, pokud hrana u -> v existuje (váha > 0)."""
        if 0 <= u < self.n and 0 <= v < self.n:
            return self.matrix[u][v] > 0
        return False

    # Metody pro práci se stupni (degrees)
    def out_degree(self, u: int) -> int:
        """Výstupní stupeň: součet v řádku u (kolik hran vede ven)."""
        return sum(1 for v in range(self.n) if self.matrix[u][v] > 0)

    def in_degree(self, v: int) -> int:
        """Vstupní stupeň: součet ve sloupci v (kolik hran vede dovnitř)."""
        return sum(1 for u in range(self.n) if self.matrix[u][v] > 0)

    def print_matrix(self) -> None:
        """Vytiskne matici sousednosti do konzole."""
        print("  " + " ".join(str(i) for i in range(self.n)))
        for i, row in enumerate(self.matrix):
            print(f"{i} " + " ".join(str(val) for val in row))


# ==============================================================================
# Vytvoření grafu přesně podle zadání z tabule
# ==============================================================================
if __name__ == "__main__":
    g = Graph(4)

    # Hrany podle matice:
    # Řádek 1: hrany do 0 a 2
    g.add_edge(1, 0)
    g.add_edge(1, 2)

    # Řádek 2: hrana do 0
    g.add_edge(2, 0)

    # Řádek 3: hrany do 1 a 2
    g.add_edge(3, 1)
    g.add_edge(3, 2)

    # Výpis a testy
    print("Matice sousednosti:")
    g.print_matrix()
    print("-" * 30)

    print(f"Existuje hrana 3 -> 1? {g.has_edge(3, 1)}")  # True
    print(f"Existuje hrana 0 -> 1? {g.has_edge(0, 1)}")  # False
    print("-" * 30)

    for node in range(g.n):
        out_deg: int = g.out_degree(node)
        in_deg: int = g.in_degree(node)
        print(f"Vrchol {node}: in-degree = {in_deg}, out-degree = {out_deg}, celkem = {in_deg + out_deg}")