import pandas as pd, glob
cols=["Row ID","Date Created","Status Detail","Service Category","Service Description","Interaction Channel","Service Area","Referral Type"]
out=[]
for f in sorted(glob.glob('/mnt/project-files/311_Requests_20261107-part-*.csv')):
    for ch in pd.read_csv(f,usecols=cols,dtype=str,chunksize=500000):
        ch=ch[(ch["Interaction Channel"]=="Phone Call")&(ch["Referral Type"]=="Referral")]
        ch["yr"]=ch["Date Created"].str.extract(r', (\d{4})')[0].astype(int)
        out.append(ch[ch.yr>=2025])
df=pd.concat(out).drop_duplicates("Row ID")
df["code"]=df["Service Area"]+" | "+df["Service Category"]+" | "+df["Service Description"]
df.to_pickle('p.pkl'); print(df.groupby('yr').size())
