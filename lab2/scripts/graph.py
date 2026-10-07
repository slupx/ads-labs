import math
import os
import matplotlib.pyplot as plt

X = 2.0
SQRT2 = math.sqrt(2)
EXACT = math.cos(math.pi * X / 4) - math.sin(math.pi * X / 4)  # = -1

N_VALUES = [1, 2, 3, 10, 20, 30, 50, 100]
N_PLOT = list(range(1, 101))


def ops_nested(n):
    return 7 + 9 * n + 5 * n * (n + 1) // 2

def ops_dynamic(n):
    return 8 + 9 * n

def compute_product(n):
    num = (1.0 + X) ** 2
    res = SQRT2
    s = 0.0
    for i in range(1, n + 1):
        s += 4.0 * i - 1.0
        res *= 1.0 - num / (4.0 * s)
    return res


ops1 = [ops_nested(n) for n in N_VALUES]
ops2 = [ops_dynamic(n) for n in N_VALUES]

ops1_plot = [ops_nested(n) for n in N_PLOT]
ops2_plot = [ops_dynamic(n) for n in N_PLOT]

errors = [abs(compute_product(n) - EXACT) for n in N_PLOT]

print("=" * 60)
print(f"Точне значення: {EXACT:.7f}")
print(f"√2 = {SQRT2:.7f}")
print()
print(f"{'n':>5} | {'Значення':>12} | {'Похибка':>14} | {'Ops1 (nested)':>14} | {'Ops2 (dp)':>10}")
print("-" * 70)
for n in N_VALUES:
    val = compute_product(n)
    err = abs(val - EXACT)
    o1 = ops_nested(n)
    o2 = ops_dynamic(n)
    print(f"{n:>5} | {val:>12.7f} | {err:>14.7f} | {o1:>14} | {o2:>10}")

print()
print("Таблиця кількості операцій:")
print(f"{'n':>5} | {'Спосіб 1 (вкладені)':>22} | {'Спосіб 2 (ДП)':>14}")
print("-" * 50)
for n, o1, o2 in zip(N_VALUES, ops1, ops2):
    print(f"{n:>5} | {o1:>22} | {o2:>14}")

lab_dir = os.path.join(os.path.dirname(__file__), "..")

# --- графік 1: кількість операцій ---
plt.figure(figsize=(9, 5))
plt.plot(N_PLOT, ops1_plot, color="red", label="Спосіб 1: вкладені цикли")
plt.plot(N_PLOT, ops2_plot, color="blue", label="Спосіб 2: динамічне програмування")
plt.scatter(N_VALUES, ops1, color="red", zorder=5)
plt.scatter(N_VALUES, ops2, color="blue", zorder=5)
plt.title("Залежність кількості операцій від n")
plt.xlabel("n")
plt.ylabel("Кількість операцій")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(lab_dir, "assets", "graph_operations.png"), dpi=150)
print(f"\nГрафік операцій збережено: {os.path.join(lab_dir, 'assets', 'graph_operations.png')}")

# --- графік 2: похибка ---
plt.figure(figsize=(9, 5))
plt.semilogy(N_PLOT, errors, color="green", label="Похибка |P_n - P_exact|")
plt.title("Залежність похибки від n (log-шкала)")
plt.xlabel("n")
plt.ylabel("|P_n - P_exact|")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(lab_dir, "assets", "graph_error.png"), dpi=150)
print(f"Графік похибки збережено:    {os.path.join(lab_dir, 'assets', 'graph_error.png')}")

plt.show()
