import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, os, pandas as pd

OUT = "/tmp/claude-0/sc/build/img/"; os.makedirs(OUT, exist_ok=True)
BG1 = "#121720"; LINE = "#2B3444"; TXT = "#EEF2F7"; MUT = "#9AA6B8"; DIM = "#66728A"
AMBER = "#FFB224"; CYAN = "#41D4F0"; GREEN = "#3ED598"; RED = "#FF5A5F"; ORANGE = "#F2873C"
plt.rcParams.update({"font.family": "Inter", "text.color": TXT, "axes.labelcolor": MUT, "xtick.color": MUT, "ytick.color": MUT,
                     "axes.edgecolor": LINE, "axes.facecolor": BG1, "figure.facecolor": BG1, "savefig.facecolor": BG1,
                     "axes.grid": True, "grid.color": LINE, "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 9})
MONO = {"family": "JetBrains Mono"}

# ---- 1. coverage curve (from rc2.py output; 2026 test set) ----
th = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
flag = [51.4, 35.9, 26.5, 18.1, 13.6, 11.5, 9.0, 4.1]
caught = [97.5, 83.5, 76.1, 64.9, 53.6, 47.4, 43.0, 18.9]
fig, ax = plt.subplots(figsize=(5.6, 3.6), dpi=300)
ax.plot([0, 100], [0, 100], color=DIM, lw=0.8, ls="--")
ax.plot(flag + [100], caught + [100], color=CYAN, lw=2.2, marker="o", ms=4, mfc=BG1, mew=1.6)
for f, c, t, col in [(18.1, 64.9, "> 20% risk\n18% of calls flagged\n65% of empty visits", AMBER), (11.5, 47.4, "> 30% risk\n12% of calls\n47% of visits", ORANGE)]:
    ax.scatter([f], [c], s=70, color=col, zorder=5)
    ax.annotate(t, (f, c), xytext=(f + 10, c - 30) if f > 15 else (f + 22, c - 44), fontsize=7.5, color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.8), fontfamily="JetBrains Mono")
ax.annotate("flag everything", (100, 100), xytext=(60, 92), fontsize=7, color=DIM)
ax.annotate("random pick", (50, 50), xytext=(55, 38), fontsize=7, color=DIM, rotation=0)
ax.set_xlabel("Share of 2026 phone referrals that get a check (%)")
ax.set_ylabel("Share of empty field visits caught (%)")
ax.set_xlim(0, 100); ax.set_ylim(0, 102)
fig.tight_layout(); fig.savefig(OUT + "coverage.png"); plt.close(fig)

# ---- 2. ten-year stability (bounce score AUC) ----
yrs = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
auc = [0.861, 0.907, 0.902, 0.903, 0.92, 0.911, 0.932, 0.932, 0.895, 0.818]
fig, ax = plt.subplots(figsize=(5.2, 2.6), dpi=300)
ax.bar([str(y) for y in yrs], auc, color=[CYAN] * 9 + [AMBER], width=0.62)
ax.axhline(0.5, color=DIM, lw=0.8, ls="--"); ax.text(9.4, 0.515, "coin flip", fontsize=6.5, color=DIM, ha="right")
for i, v in enumerate(auc): ax.text(i, v + 0.012, f"{v:.2f}", ha="center", fontsize=6.5, color=TXT, fontfamily="JetBrains Mono")
ax.set_ylim(0.4, 1.0); ax.set_ylabel("AUC, trained on the year before"); ax.grid(axis="x", visible=False)
ax.set_xlabel("Year tested (2026: eight more areas began recording bounces)", color=MUT)
fig.tight_layout(); fig.savefig(OUT + "auc.png"); plt.close(fig)

# ---- 3. Monte Carlo net value distribution ----
rng = np.random.default_rng(20261110); N = 50000
tri = lambda a, m, b: rng.triangular(a, m, b, N)
ann = 12 / 10.2
FL = 32508 * ann; FV = 6885 * ann; FD = 2902 * ann
visit = tri(22, 84, 280); desk = tri(5, 10, 20) / 60 * tri(36.93, 41.99, 52.09)
avoid = tri(0.2, 0.35, 0.5); ask = tri(0.30, 1.02, 1.02)
sav = FV * avoid * (visit + desk) + FD * avoid * (desk + 16.29 * 0.25); cost = FL * ask; net = sav - cost
p10, p50, p90, mean = np.percentile(net, 10), np.percentile(net, 50), np.percentile(net, 90), net.mean()
print("MC", round(mean / 1e3), round(p10 / 1e3), round(p50 / 1e3), round(p90 / 1e3), "gross", round(sav.mean() / 1e3), "cost", round(cost.mean() / 1e3), "P(net<0)", (net < 0).mean())
print("visits avoided mean", (FV * avoid).mean(), "FV", FV, "FD", FD, "FL", FL)
fig, ax = plt.subplots(figsize=(5.0, 2.5), dpi=300)
ax.hist(net / 1e3, bins=80, color=CYAN, alpha=0.9)
for v, lab, col in [(p10, "P10", MUT), (mean, "mean", AMBER), (p90, "P90", MUT)]:
    ax.axvline(v / 1e3, color=col, lw=1.2, ls="--" if lab != "mean" else "-")
    ax.text(v / 1e3, ax.get_ylim()[1] * 0.92, f"{lab} ${v/1e3:,.0f}K", color=col, fontsize=7, ha="center", fontfamily="JetBrains Mono")
ax.set_xlabel("Net capacity freed, $K a year (50,000 draws)"); ax.set_yticks([]); ax.grid(axis="y", visible=False)
ax.axvline(0, color=RED, lw=1)
fig.tight_layout(); fig.savefig(OUT + "mc.png"); plt.close(fig)

# ---- 4. top flagged codes bars ----
codes = [("Untidy Property complaint", 4877, 1350, "Municipal Enforcement"), ("Peace Officer complaint", 2291, 978, "Peace Officers"),
         ("Parking on private property", 1448, 550, "Parking Enforcement"), ("Weed complaint", 2020, 442, "Municipal Enforcement"),
         ("Snow on walk complaint", 2716, 313, "Municipal Enforcement"), ("Noise complaint", 491, 304, "Peace Officers"),
         ("Business licence complaint", 402, 303, "Municipal Enforcement"), ("Snow blocked (road)", 1319, 265, "Roadway Maintenance"),
         ("Dog at large", 1398, 187, "Animal Control"), ("Zoning complaint", 464, 182, "Municipal Enforcement")]
fig, ax = plt.subplots(figsize=(6.0, 3.5), dpi=300)
names = [c[0] for c in codes][::-1]; n = [c[1] for c in codes][::-1]; wv = [c[2] for c in codes][::-1]
ax.barh(names, n, color="#222B3B", height=0.66, label="phone referrals, 2026 to Nov 6")
ax.barh(names, wv, color=AMBER, height=0.66, label="ended in a visit with nothing to act on")
for i, (a, b) in enumerate(zip(n, wv)):
    ax.text(a + 60, i, f"{b/a:.0%}", va="center", fontsize=7, color=AMBER, fontfamily="JetBrains Mono")
ax.grid(axis="y", visible=False); ax.set_xlabel("Tickets, Jan to Nov 6, 2026"); ax.legend(frameon=False, fontsize=7, loc="lower right")
ax.tick_params(axis="y", labelsize=7.5)
fig.tight_layout(); fig.savefig(OUT + "topcodes.png"); plt.close(fig)

# ---- 5. base case vs with action (simple) ----
fig, ax = plt.subplots(figsize=(4.6, 2.4), dpi=300)
cats = ["Today", "Pilot gate\n(20% drop)", "Expected\n(35% drop)", "Upside\n(50% drop)"]
vals = [21.2, 21.2 * 0.8, 21.2 * 0.65, 21.2 * 0.5]
ax.bar(cats, vals, color=[RED, MUT, CYAN, GREEN], width=0.58)
for i, v in enumerate(vals): ax.text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=7.5, color=TXT, fontfamily="JetBrains Mono")
ax.set_ylabel("Flagged referrals ending in\nan empty visit (%)"); ax.grid(axis="x", visible=False); ax.set_ylim(0, 26)
fig.tight_layout(); fig.savefig(OUT + "gate.png"); plt.close(fig)
print("done")
