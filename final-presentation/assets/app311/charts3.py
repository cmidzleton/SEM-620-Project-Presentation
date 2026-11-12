"""Charts for the Referral Check deck. Every series comes from figs.figures(), so the pictures and the slide text cannot drift apart."""
import sys
sys.path.insert(0, "/tmp/claude-0/sc/build")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, os, glob
from matplotlib import font_manager
from figs import cached
for _f in glob.glob("/root/.fonts/qs/*.ttf"):
    font_manager.fontManager.addfont(_f)

CUT = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20; REDL = float(sys.argv[2]) if len(sys.argv) > 2 else 0.30
F = cached(CUT, REDL)
OUT = "/tmp/claude-0/sc/build/img3/"; os.makedirs(OUT, exist_ok=True)
BG1 = "#1C1F24"; LINE = "#2E333B"; TXT = "#F5F5F5"; MUT = "#9AA0A8"; DIM = "#555B63"
AMBER = "#F2A900"; CYAN = "#5AA9FF"; GREEN = "#3DBE7A"; RED = "#E5484D"; ORANGE = "#F2873C"
plt.rcParams.update({"font.family": "Quattrocento Sans", "text.color": TXT, "axes.labelcolor": MUT, "xtick.color": MUT, "ytick.color": MUT,
                     "axes.edgecolor": LINE, "axes.facecolor": BG1, "figure.facecolor": BG1, "savefig.facecolor": BG1,
                     "axes.grid": True, "grid.color": LINE, "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 9.5})

# ---- 1. coverage curve (2025 score on the 2026 test set) ----
cv = F["curve"]; flag = [c["flag"] for c in cv]; caught = [c["caught"] for c in cv]
pt = {round(c["th"], 2): c for c in cv}
fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)
ax.plot([0, 100], [0, 100], color=DIM, lw=0.8, ls="--")
_x = [0] + flag[::-1] + [100]; _y = [0] + caught[::-1] + [100]      # ascending, so no line doubles back from the last cut-off to (100, 100)
ax.plot(_x, _y, color=CYAN, lw=2.2, zorder=3)
ax.plot(flag, caught, color=CYAN, lw=0, marker="o", ms=4, mfc=BG1, mew=1.6, zorder=4)
a_, r_ = pt[round(CUT, 2)], pt[round(REDL, 2)]
labels = [(a_["flag"], a_["caught"], f"> {CUT:.0%} risk (amber and red): {a_['flag']:.0f}% of calls\nflagged, {a_['caught']:.0f}% of empty visits caught", AMBER, (50, 36)),
          (r_["flag"], r_["caught"], f"> {REDL:.0%} risk (red only): {r_['flag']:.0f}% of calls,\n{r_['caught']:.0f}% of empty visits", RED, (50, 13))]
for f, c, t, col, xy in labels:
    ax.scatter([f], [c], s=70, color=col, zorder=5)
    ax.annotate(t, (f, c), xytext=xy, fontsize=8.5, color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.8, shrinkB=5), fontfamily="Quattrocento Sans", va="center")
ax.text(99, 104.5, "flag everything", fontsize=7.5, color=MUT, ha="right", va="center")
ax.text(78, 64, "random pick", fontsize=7.5, color=MUT)
ax.set_xlabel("Share of 2026 phone referrals that get a check (%)")
ax.set_ylabel("Share of empty visits caught (%)")
ax.set_xlim(0, 100); ax.set_ylim(0, 109); ax.set_yticks([0, 20, 40, 60, 80, 100])
fig.tight_layout(); fig.savefig(OUT + "coverage.png"); plt.close(fig)

# ---- 2. ten-year stability of the same score on the same outcome (empty visits) ----
H = F["hist"]; yrs = [h["year"] for h in H]; auc = [h["auc_deck_score_visits"] for h in H]
fig, ax = plt.subplots(figsize=(5.2, 2.6), dpi=220)
ax.bar([str(y) for y in yrs], auc, color=[CYAN] * (len(yrs) - 1) + [AMBER], width=0.62)
ax.axhline(0.5, color=DIM, lw=0.8, ls="--"); ax.set_xlim(-0.6, len(yrs) + 0.55); ax.text(len(yrs) - 0.55, 0.52, "coin flip", fontsize=7.5, color=MUT, ha="left")
for i, v in enumerate(auc): ax.text(i, v + 0.012, f"{v:.2f}", ha="center", fontsize=7.5, color=TXT, fontfamily="Quattrocento Sans")
ax.set_ylim(0.4, 1.0); ax.set_ylabel("AUC on empty visits"); ax.grid(axis="x", visible=False)
ax.set_xlabel("Year tested, each scored with the year before (2026 to Nov 6)", color=MUT)
fig.tight_layout(); fig.savefig(OUT + "auc.png"); plt.close(fig)

# ---- 3. Monte Carlo net value distribution ----
net = F["draws"]; m = F["mc"]
fig, ax = plt.subplots(figsize=(5.0, 2.5), dpi=220)
ax.hist(net / 1e3, bins=80, color=CYAN, alpha=0.9)
_ym = ax.get_ylim()[1]; ax.set_ylim(0, _ym * 1.2)
for v, lab, col in [(m["p10"], "P10", MUT), (m["net"], "mean", AMBER), (m["p90"], "P90", MUT)]:
    ax.axvline(v / 1e3, color=col, lw=1.2, ls="--" if lab != "mean" else "-")
    ax.text(v / 1e3 + (-9 if lab == "P10" else 9), _ym * 1.08, f"{lab} ${v/1e3:,.0f}K", color=col, fontsize=8, ha="right" if lab == "P10" else "left", fontfamily="Quattrocento Sans")
ax.set_xlabel("Net capacity freed, $K a year (50,000 draws)"); ax.set_yticks([]); ax.grid(axis="y", visible=False)
ax.axvline(0, color=RED, lw=1)
fig.tight_layout(); fig.savefig(OUT + "mc.png"); plt.close(fig)

# ---- 4. top flagged codes bars ----
codes = F["top"]
fig, ax = plt.subplots(figsize=(6.0, 3.5), dpi=220)
names = [c[0] for c in codes][::-1]; n = [c[1] for c in codes][::-1]; wv = [c[2] for c in codes][::-1]
ax.barh(names, n, color="#2E333B", height=0.66, label="phone referrals, 2026 to Nov 6")
ax.barh(names, wv, color=AMBER, height=0.66, label="ended with nothing to act on in the field")
for i, (a, b) in enumerate(zip(n, wv)):
    ax.text(a + 60, i, f"{b/a:.0%}", va="center", fontsize=7.5, color=AMBER, fontfamily="Quattrocento Sans")
ax.grid(axis="y", visible=False); ax.set_xlabel("Tickets, Jan to Nov 6, 2026"); ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.tick_params(axis="y", labelsize=8)
fig.tight_layout(); fig.savefig(OUT + "topcodes.png"); plt.close(fig)

# ---- 5. base case vs with action ----
fig, ax = plt.subplots(figsize=(4.6, 2.4), dpi=220)
cats = ["Today", "Pilot gate\n(20% drop)", "Expected\n(35% drop)", "Upside\n(50% drop)"]
vals = F["gate"]
ax.bar(cats, vals, color=[RED, MUT, CYAN, GREEN], width=0.58)
for i, v in enumerate(vals): ax.text(i, v + 0.6, f"{v:.1f}%", ha="center", fontsize=8, color=TXT, fontfamily="Quattrocento Sans")
ax.set_ylabel("Flagged referrals ending in\nan empty visit (%)"); ax.grid(axis="x", visible=False); ax.set_ylim(0, max(vals) * 1.22)
fig.tight_layout(); fig.savefig(OUT + "gate.png"); plt.close(fig)
print("charts done", {k: round(v / 1e3) for k, v in m.items() if k in ("net", "p10", "p50", "p90", "gross", "cost")})
