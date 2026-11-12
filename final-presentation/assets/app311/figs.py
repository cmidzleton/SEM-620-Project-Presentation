"""Every figure the Referral Check deck prints, computed from the team's six-part export of the City's 311 Requests open data.
Duplicate-type closures are left out of the wasted set (Curtis, Nov 11 2026): the three "Duplicate Request" labels and "File Already under Investigation".
Usage: F = figures(cut=0.20, red=0.30)   # cut = amber line (flag), red = red line
Denominators are all phone referrals; the 4,013 (2026) with no service code stay in the totals and can never be flagged."""
import pandas as pd, numpy as np
from scipy.stats import norm

PKL = "/tmp/claude-0/sc/nd/p.pkl"; PKL24 = "/tmp/claude-0/sc/nd/p24.pkl"
HIST = "/tmp/claude-0/sc/hist/empty_visit_backtest_2017_2026.csv"
VISIT = ["Does Not Meet Bylaw Offence Standards", "Assessed-No Action Required", "Unable to Locate Animal", "Location Not Found", "Unable to Contact Complainant"]
DUP = ["Duplicate Request Exists", "Duplicate Request", "Duplicate Request - See Related Ticket in Details", "File Already under Investigation"]
DESK = ["311 Redirecting to Other Business Area", "Non-City Service or Location", "Reported on same day - must submit after 10pm"]
ANN = 12 / 10.2
NICE = {"Complaint Registered - Untidy Property": "Untidy Property complaint", "CSPO Complaint Registered": "Peace Officer complaint", "Parking - Private Property": "Parking on private property",
        "Weed Complaint Registered": "Weed complaint", "Snow on Walk Complaint": "Snow on walk complaint", "Register Noise Complaint": "Noise complaint",
        "Business Licence-Confirmation/Complaint": "Business licence complaint", "Snow Blocked": "Snow blocked (road)", "Complaint Registered - Dog at Large": "Dog at large",
        "Zoning Complaint Registered": "Zoning complaint", "SNOW:Sidewalk Windrow": "Snow: sidewalk windrow", "Nuisance Odour Complaints": "Nuisance odour complaint",
        "Pothole: Arterial Road": "Pothole: arterial road", "Trip/displacement - residential sidewalk": "Sidewalk trip hazard", "Subsidence - Residential Road": "Subsidence: residential road",
        "Ponding - residential sidewalk": "Ponding: residential sidewalk", "Update Existing Complaint": "Update existing complaint", "Subsidence - Arterial Road": "Subsidence: arterial road",
        "Parking: Without Required Permit": "Parking without permit", "General Comments Roadway Maintenance": "Roadway general comment"}
AREA = {"Community Standards - Muni. Enforcement": "Community Standards - Municipal Enforcement"}
PILOT = ["Community Standards - Muni. Enforcement", "Community Standards - Peace Officers", "Parking Enforcement"]


def mc(FV, FD, FL, visit_scale=1.0, ask_fixed=None, desk_in=True, avoid_fixed=None, draws=False):
    rng = np.random.default_rng(20261110); N = 50000
    tri = lambda a, m, b: rng.triangular(a, m, b, N)
    visit = tri(22, 84, 280) * visit_scale; desk = tri(5, 10, 20) / 60 * tri(36.93, 41.99, 52.09)
    avoid = tri(0.2, 0.35, 0.5); ask = tri(0.30, 1.02, 1.02)
    if avoid_fixed is not None: avoid = np.full(N, avoid_fixed)
    if ask_fixed is not None: ask = np.full(N, ask_fixed)
    field = FV * avoid * (visit + desk); deskv = FD * avoid * (desk + 16.29 * 0.25) * (1 if desk_in else 0)
    sav = field + deskv; cost = FL * ask; net = sav - cost
    be = np.mean(cost) / np.mean(FV * (visit + desk) + (FD * (desk + 16.29 * 0.25) if desk_in else 0))
    out = dict(net=net.mean(), p10=np.percentile(net, 10), p50=np.percentile(net, 50), p90=np.percentile(net, 90), gross=sav.mean(), cost=cost.mean(), field=field.mean(), desk=deskv.mean(),
               pneg=float((net < 0).mean()), be=be, unit_visit=float((visit + desk).mean()), unit_desk=float((desk + 16.29 * 0.25).mean()), ask=float(ask.mean()),
               visits_avoided=float((FV * avoid).mean()), desk_avoided=float((FD * avoid).mean()))
    if draws: out["draws"] = net
    return out


def K(x):
    return f"${x / 1e3:,.0f}K"


def one_in(pct):
    return round(100 / pct)


WORDS = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "11", 12: "12"}


def figures(cut=0.20, red=0.30):
    p = pd.read_pickle(PKL); p["sd"] = p["Status Detail"]
    p["wv"] = p.sd.isin(VISIT).astype(int); p["wd"] = p.sd.isin(DESK).astype(int); p["dup"] = p.sd.isin(DUP).astype(int)
    df = p.groupby(["yr", "code"], dropna=False).agg(n=("wv", "size"), wv=("wv", "sum"), wd=("wd", "sum"), area=("Service Area", "first"), desc=("Service Description", "first")).reset_index()
    tr = df[df.yr == 2025].set_index("code"); te = df[df.yr == 2026].set_index("code").copy()
    mus = {}
    for col in ("wv", "wd"):
        mu = tr[col].sum() / tr.n.sum(); mus[col] = mu
        rate = (tr[col] + mu * 10) / (tr.n + 10)
        te["s_" + col] = [rate.get(c, mu) if isinstance(c, str) else mu for c in te.index]
    te["s"] = te.s_wv + te.s_wd; te["w"] = te.wv + te.wd
    N26, WV26, WD26 = int(te.n.sum()), int(te.wv.sum()), int(te.wd.sum())
    N25, WV25, WD25 = int(tr.n.sum()), int(tr.wv.sum()), int(tr.wd.sum())
    F = dict(cut=cut, red=red, cut_pct=f"{cut:.0%}", red_pct=f"{red:.0%}", N26=N26, WV26=WV26, WD26=WD26, N25=N25, WV25=WV25, WD25=WD25,
             dup25=int(p[p.yr == 2025].dup.sum()), dup26=int(p[p.yr == 2026].dup.sum()),
             wv_rate26=100 * WV26 / N26, wd_rate26=100 * WD26 / N26, any_rate26=100 * (WV26 + WD26) / N26, any_rate25=100 * (WV25 + WD25) / N25,
             prior_wv=100 * mus["wv"], prior_wd=100 * mus["wd"], wv_year=WV26 * ANN)
    F["any_one_in"] = round(N26 / (WV26 + WD26)); F["wv_one_in"] = round(N26 / WV26)
    # curve
    curve = []
    for th in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]:
        f = te[te.s > th]
        curve.append(dict(th=th, codes=len(f), flag=100 * f.n.sum() / N26, caught=100 * f.wv.sum() / WV26, desk=100 * f.wd.sum() / WD26, prec=100 * f.w.sum() / max(f.n.sum(), 1), p1=100 * f.wv.sum() / max(f.n.sum(), 1), n=int(f.n.sum()), wv=int(f.wv.sum())))
    F["curve"] = curve
    f = te[te.s > cut]; r_ = te[te.s > red]; a_ = te[(te.s > cut) & (te.s <= red)]; g_ = te[te.s <= cut]
    F.update(codes=len(f), n_flag=int(f.n.sum()), wv_flag=int(f.wv.sum()), wd_flag=int(f.wd.sum()), flag=100 * f.n.sum() / N26, caught=100 * f.wv.sum() / WV26,
             prec=100 * f.w.sum() / f.n.sum(), p1=100 * f.wv.sum() / f.n.sum(), desk_caught=100 * f.wd.sum() / WD26)
    F["FL"] = f.n.sum() * ANN; F["FV"] = f.wv.sum() * ANN; F["FD"] = f.wd.sum() * ANN; F["per_month"] = f.n.sum() / 10.2
    F["green_share"] = 100 * g_.n.sum() / N26; F["amber_share"] = 100 * a_.n.sum() / N26; F["red_share"] = 100 * r_.n.sum() / N26
    F["green_wv"] = 100 * g_.wv.sum() / WV26; F["amber_wv"] = 100 * a_.wv.sum() / WV26; F["red_wv"] = 100 * r_.wv.sum() / WV26
    F["red_codes"] = len(r_); F["amber_codes"] = len(a_); F["red_prec"] = 100 * r_.w.sum() / r_.n.sum(); F["red_p1"] = 100 * r_.wv.sum() / r_.n.sum()
    m = mc(F["FV"], F["FD"], F["FL"], draws=True); F["draws"] = m.pop("draws"); F["mc"] = m
    F["sens_halve"] = mc(F["FV"], F["FD"], F["FL"], visit_scale=0.5)["net"]; F["sens_ask102"] = mc(F["FV"], F["FD"], F["FL"], ask_fixed=1.02)["net"]
    F["sens_nodesk"] = mc(F["FV"], F["FD"], F["FL"], desk_in=False)["net"]
    F["net20"] = mc(F["FV"], F["FD"], F["FL"], avoid_fixed=0.2)["net"]; F["net35"] = mc(F["FV"], F["FD"], F["FL"], avoid_fixed=0.35)["net"]; F["net50"] = mc(F["FV"], F["FD"], F["FL"], avoid_fixed=0.5)["net"]
    F["be_visit"] = (m["cost"] - F["FD"] * 0.35 * m["unit_desk"]) / (F["FV"] * 0.35)          # total cost per avoided visit at which net = 0
    F["mc_red"] = mc(r_.wv.sum() * ANN, r_.wd.sum() * ANN, r_.n.sum() * ANN)
    # pilot power
    z = norm.ppf(.975) + norm.ppf(.8)
    def power(g, rel):
        p1 = g.wv.sum() / g.n.sum(); p2 = p1 * (1 - rel)
        n = z ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / (p1 - p2) ** 2
        return dict(p1=100 * p1, p2=100 * p2, n=n, months=n / (g.n.sum() / 10.2 / 2))
    F["pw20"] = power(f, 0.2); F["pw35"] = power(f, 0.35); F["pw_red20"] = power(r_, 0.2)
    F["gate"] = [F["p1"], F["p1"] * 0.8, F["p1"] * 0.65, F["p1"] * 0.5]
    F["weeks_readout"] = F["pw20"]["months"] * 4.345 + 3          # flagged calls per arm, plus about three weeks for visits to close
    # areas and codes
    a = f.groupby("area")[["n", "wv"]].sum().sort_values("wv", ascending=False); a["share"] = 100 * a.wv / a.wv.sum()
    rows = [(AREA.get(i, i), int(r.n), int(r.wv), r.share) for i, r in a.head(6).iterrows()]
    rows.append(("All other", int(a.n.iloc[6:].sum()), int(a.wv.iloc[6:].sum()), 100 * a.wv.iloc[6:].sum() / a.wv.sum()))
    F["areas"] = rows; F["pilot_share"] = float(a.loc[[x for x in PILOT if x in a.index], "share"].sum())
    top = f.sort_values("wv", ascending=False).head(10)
    F["top"] = [(NICE.get(r.desc, r.desc), int(r.n), int(r.wv), AREA.get(r.area, r.area)) for _, r in top.iterrows()]
    F["top10_share"] = 100 * top.wv.sum() / f.wv.sum()
    ut = te[te.desc == "Complaint Registered - Untidy Property"].iloc[0]
    F["untidy_s"] = 100 * ut.s; F["untidy_tier"] = "RED" if ut.s > red else ("AMBER" if ut.s > cut else "GREEN"); F["untidy_n"] = int(ut.n); F["untidy_wv"] = int(ut.wv)
    # year-to-year stability of the per-code rate under this definition
    p24 = pd.read_pickle(PKL24); labs = VISIT + DESK
    a24 = p24.assign(w=p24["Status Detail"].isin(labs).astype(int)).groupby("code").agg(n=("w", "size"), w=("w", "sum"))
    a25 = p[p.yr == 2025].assign(w2=lambda d: d.sd.isin(labs).astype(int)).groupby("code").agg(n=("w2", "size"), w=("w2", "sum"))
    j = a24.join(a25, lsuffix="24", rsuffix="25", how="inner"); j = j[(j.n24 >= 30) & (j.n25 >= 30)]
    F["r"] = float(np.corrcoef(j.w24 / j.n24, j.w25 / j.n25)[0, 1]); F["r_codes"] = len(j)
    # the 90-day data set
    F["ds_logged"] = 2 * F["per_month"]; F["ds_closed"] = 0.75 * F["ds_logged"]; F["ds_empty"] = F["ds_closed"] * F["p1"] / 100
    F["one_in_flag"] = WORDS.get(one_in(F["flag"]), str(one_in(F["flag"])))
    # the card for the Caller 7 code shows last year's rate
    u25 = tr[tr.desc == "Complaint Registered - Untidy Property"].iloc[0]
    F["untidy25_n"] = int(u25.n); F["untidy25_wv"] = int(u25.wv); F["untidy25_rate"] = 100 * u25.wv / u25.n
    # what the flag cannot reach
    blank = te[[not isinstance(c, str) for c in te.index]]
    F["blank_n"] = int(blank.n.sum()); F["blank_wv"] = int(blank.wv.sum())
    newc = te[[isinstance(c, str) and c not in tr.index for c in te.index]]
    F["new_codes"] = len(newc); F["new_n"] = int(newc.n.sum()); F["new_wv"] = int(newc.wv.sum()); F["new_wv_share"] = 100 * newc.wv.sum() / WV26
    band = te[(te.s > 0.15) & (te.s <= cut)]
    F["band_codes"] = len(band); F["band_wv_share"] = 100 * band.wv.sum() / WV26
    # labels: two of the five do not prove an officer attended
    NOPROOF = ["Unable to Contact Complainant", "Location Not Found"]
    F["noproof25"] = int(p[(p.yr == 2025) & p.sd.isin(NOPROOF)].shape[0]); F["noproof26"] = int(p[(p.yr == 2026) & p.sd.isin(NOPROOF)].shape[0])
    fl = p[(p.yr == 2026) & p.code.isin([c for c in f.index if isinstance(c, str)])]
    F["flag_noproof"] = int(fl.sd.isin(NOPROOF).sum())
    F["flag_labels"] = fl[fl.sd.isin(VISIT)].sd.value_counts().to_dict()
    # ten-year out-of-time check of the same score (hist.py)
    try:
        F["hist"] = pd.read_csv(HIST).to_dict("records")
    except Exception:
        F["hist"] = []
    return F


_CACHE = {}


def cached(cut=0.20, red=0.30):
    """figures() once per process (the build and the charts both ask for it)."""
    if (cut, red) not in _CACHE:
        _CACHE[(cut, red)] = figures(cut, red)
    return _CACHE[(cut, red)]


if __name__ == "__main__":
    import sys
    cut = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20; red = float(sys.argv[2]) if len(sys.argv) > 2 else 0.30
    F = figures(cut, red); m = F["mc"]
    print(f"cut {F['cut_pct']} red {F['red_pct']}: {F['codes']} codes; flagged {F['flag']:.1f}% ({F['n_flag']:,}); empty visits caught {F['caught']:.1f}% ({F['wv_flag']:,} of {F['WV26']:,}); precision {F['prec']:.1f}%; p1 {F['p1']:.1f}%")
    print(f"per year: FL {F['FL']:,.0f} FV {F['FV']:,.0f} FD {F['FD']:,.0f}; per month {F['per_month']:,.0f}")
    print(f"net {K(m['net'])} median {K(m['p50'])} P10-P90 {K(m['p10'])}-{K(m['p90'])}; gross {K(m['gross'])} = field {K(m['field'])} + desk {K(m['desk'])}; cost {K(m['cost'])}; break-even {100 * m['be']:.1f}%; pneg {m['pneg']}")
    print(f"visits avoided {m['visits_avoided']:,.0f} x ${m['unit_visit']:.2f}; desk avoided {m['desk_avoided']:,.0f} x ${m['unit_desk']:.2f}; be_visit ${F['be_visit']:.2f}")
    print(f"sens halve {K(F['sens_halve'])}; ask $1.02 {K(F['sens_ask102'])}; no desk {K(F['sens_nodesk'])}; avoid 20/35/50 {K(F['net20'])}/{K(F['net35'])}/{K(F['net50'])}; red only {K(F['mc_red']['net'])} ({K(F['mc_red']['p10'])}-{K(F['mc_red']['p90'])})")
    print(f"tiers green {F['green_share']:.1f}% ({F['green_wv']:.1f}% of visits) amber {F['amber_share']:.1f}% ({F['amber_wv']:.1f}%) red {F['red_share']:.1f}% ({F['red_wv']:.1f}%); red codes {F['red_codes']} amber codes {F['amber_codes']}; red precision {F['red_prec']:.1f}% p1 {F['red_p1']:.1f}%")
    print("power", {k: (round(v['p1'], 1), round(v['p2'], 1), round(v['n']), round(v['months'], 2)) for k, v in (('20', F['pw20']), ('35', F['pw35']), ('red20', F['pw_red20']))}, "weeks", round(F['weeks_readout'], 1))
    print("gate", [round(x, 1) for x in F['gate']], "pilot areas share", round(F['pilot_share'], 1), "top10 share", round(F['top10_share'], 1))
    print("areas", [(a, n, w, round(s_)) for a, n, w, s_ in F['areas']])
    print("top", F['top'])
    print(f"untidy score {F['untidy_s']:.1f}% tier {F['untidy_tier']}; r {F['r']:.3f} over {F['r_codes']}; data set {F['ds_logged']:,.0f} / {F['ds_closed']:,.0f} / {F['ds_empty']:,.0f}; one call in {F['one_in_flag']}")
    print(f"base: 2026 any {F['any_rate26']:.2f}% (1 in {F['any_one_in']}), field {F['wv_rate26']:.2f}% (1 in {F['wv_one_in']}), desk {F['wd_rate26']:.2f}% ({F['WD26']:,}); 2025 field {F['WV25']:,} desk {F['WD25']:,}; priors {F['prior_wv']:.1f}% / {F['prior_wd']:.1f}%; dups 2025 {F['dup25']:,} 2026 {F['dup26']:,}")
    print("curve", [(c['th'], c['codes'], round(c['flag'], 1), round(c['caught'], 1), round(c['desk'], 1), round(c['prec'], 1)) for c in F['curve']])
    print(f"untidy 2025 {F['untidy25_wv']:,} of {F['untidy25_n']:,} = {F['untidy25_rate']:.1f}%; blank-code tickets {F['blank_n']:,} with {F['blank_wv']:,} empty; new codes {F['new_codes']} n {F['new_n']:,} wv {F['new_wv']} ({F['new_wv_share']:.1f}%); 15%-cut band {F['band_codes']} codes {F['band_wv_share']:.1f}% of empty visits")
    print(f"no-proof labels 2025 {F['noproof25']:,} 2026 {F['noproof26']:,}; in flagged set {F['flag_noproof']:,}; flagged labels {F['flag_labels']}")
    print("hist", [(h['year'], h['auc_deck_score_visits'], h['flag'], h['caught'], h['codes']) for h in F['hist']])
