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

    def analyze(self) -> None:
        """Provede analýzu základních vlastností grafu."""
        is_directed = False
        is_weighted = False
        has_loops = False
        edges_count = 0

        # 1. Analýza orientace, ohodnocení a smyček
        for i in range(self.n):
            if self.matrix[i][i] != 0:
                has_loops = True
            for j in range(self.n):
                if self.matrix[i][j] > 0:
                    edges_count += 1
                if self.matrix[i][j] not in (0, 1):
                    is_weighted = True
                if self.matrix[i][j] != self.matrix[j][i]:
                    is_directed = True

        # Úprava počtu hran pro neorientovaný graf
        if not is_directed:
            edges_count //= 2

        # 2. Test planárnosti (Heuristika přes Eulerovu větu: E <= 3V - 6)
        is_planar = True
        if self.n >= 3 and edges_count > 3 * self.n - 6:
            is_planar = False

        # 3. Výpočet chromatického čísla
        chromatic_number = self._get_chromatic_number()

        # Výpis výsledků
        print("\n--- Analýza grafu ---")
        print(f"Počet vrcholů (|V|): {self.n}")
        print(f"Počet hran (|E|): {edges_count}")
        print(f"Orientovaný: {'Ano' if is_directed else 'Ne'}")
        print(f"Ohodnocený: {'Ano' if is_weighted else 'Ne'}")
        print(f"Obsahuje smyčky: {'Ano' if has_loops else 'Ne'}")
        print(f"Planární (podle nutné podmínky): {'Pravděpodobně Ano' if is_planar else 'Ne (porušuje E <= 3V - 6)'}")
        print(f"Chromatické číslo: {chromatic_number}")
        print("---------------------\n")

    def _get_chromatic_number(self) -> int:
        """Pomocná metoda pro výpočet chromatického čísla pomocí backtrackingu."""
        # Převod na neorientovaný graf bez smyček pro barvení
        adj = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i != j and (self.matrix[i][j] > 0 or self.matrix[j][i] > 0):
                    if j not in adj[i]:
                        adj[i].append(j)

        def is_safe(v: int, color: list, c: int) -> bool:
            for neighbor in adj[v]:
                if color[neighbor] == c:
                    return False
            return True

        def graph_coloring(m: int, color: list, v: int) -> bool:
            if v == self.n:
                return True
            for c in range(1, m + 1):
                if is_safe(v, color, c):
                    color[v] = c
                    if graph_coloring(m, color, v + 1):
                        return True
                    color[v] = 0
            return False

        # Hledání nejmenšího možného počtu barev (1 až N)
        for m in range(1, self.n + 1):
            color = [0] * self.n
            if graph_coloring(m, color, 0):
                return m
        return self.n


# ==============================================================================
# Vytvoření grafu a testování
# ==============================================================================
if __name__ == "__main__":
    g = Graph(4)

    # Řádek 1: hrany do 0 a 2
    g.add_edge(1, 0)
    g.add_edge(1, 2)

    # Řádek 2: hrana do 0
    g.add_edge(2, 0)

    # Řádek 3: hrany do 1 a 2
    g.add_edge(3, 1)
    g.add_edge(3, 2)

    print("Matice sousednosti:")
    g.print_matrix()

    # Spuštění nové analytické metody
    g.analyze()