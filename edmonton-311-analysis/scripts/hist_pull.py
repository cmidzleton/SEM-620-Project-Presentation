import subprocess, json, urllib.parse, sys, os
IDS = {2016: "bcsz-zu8a", 2017: "xq32-itvg", 2018: "t4rn-2nng", 2019: "rb8e-6i3k", 2020: "ri59-3ugc", 2021: "6mnu-u5jr", 2022: "2x69-33yr"}
for y, i in IDS.items():
    q = {"$select": "year,service_area,service_category,service_description,status_detail,count(distinct row_id) as n,count(*) as nrows",
         "$where": "interaction_channel='Phone Call' AND referral_type='Referral'",
         "$group": "year,service_area,service_category,service_description,status_detail", "$limit": "500000"}
    url = f"https://data.edmonton.ca/resource/{i}.json?" + urllib.parse.urlencode(q)
    out = f"/tmp/claude-0/sc/hist/agg_{y}.json"
    r = subprocess.run(["curl", "-sS", "-m", "170", "-o", out, "-w", "%{http_code}", url], capture_output=True, text=True)
    try:
        j = json.load(open(out)); n = sum(int(x["n"]) for x in j); nr = sum(int(x["nrows"]) for x in j)
        yrs = {}
        for x in j: yrs[x.get("year")] = yrs.get(x.get("year"), 0) + int(x["n"])
        print(y, i, r.stdout, "groups", len(j), "distinct", n, "rows", nr, "by year", yrs, flush=True)
    except Exception as e:
        print(y, i, r.stdout, "ERR", e, open(out).read()[:300], flush=True)
