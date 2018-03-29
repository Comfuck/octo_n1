# coding:utf-8

import requests

url = "http://zzk.cnblogs.com/s/blogpost"  # 问号前面的
par = {
      "Keywords": "yoyoketang",
     }  # 问号后面的
h = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Cookie": "_ga=GA1.2.865342035.1503842097; __utma=226521935.865342035.1503842097.1511965730.1512395827.3; __utmz=226521935.1506156701.1.1.utmcsr=mamicode.com|utmccn=(referral)|utmcmd=referral|utmcct=/info-detail-1728757.html; __gads=ID=b4fc842c685a9b8f:T=1509190884:S=ALNI_MbEMu-56DkVeTQtVHtlZFnLlLWpcA; __utma=59123430.865342035.1503842097.1520163648.1520166296.5; __utmz=59123430.1519560648.3.2.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; .CNBlogsCookie=E3954454761B8601ABC025BCCF0DD91AF850D84D7CFF1D0A7D78D95DE2EBF22DBCC616599F070C63D31C43A6987615FAB4FF041E021C6001DCD951D7C31025D43A3480BD338A8C4776C8F673018F334395A7A2C9; .Cnblogs.AspNetCore.Cookies=CfDJ8N7AeFYNSk1Put6Iydpme2ZS5JmATIHGTsZRiV2U6JKNq8ISwKWfVTo30De3YQHr5Hm0EfkQAtv24mUChzN0fnGV4dHGnKRj1ovNlCSsyO0rbqU1BExUwsNNHT-4mgPcCikx8WF5p9EuTgKOur-wnO1K_7lY_G3kV4avxcoCXWZVsHPbCW9lCP49lfidV_HFws3oy6n8ftv9X9zksObkfcDik4IoGQZMLfsF8zuNdCiUyu8VYKwBhxXRcvQtkSirUci9MArkedsRRe_pDAiRx0muFVB9W6NkGahnrKtD4BVLLTytMJnZMax2xz6SYF-moQ; _gid=GA1.2.1564493124.1520080316; __utmc=59123430; __utmb=59123430.3.10.1520166296; __utmt=1"
}
r = requests.get(url, params=par, headers=h)
print(r.text)