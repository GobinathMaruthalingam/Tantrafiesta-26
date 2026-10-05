from icons import ic
CSS = open('style.css').read()
FONTS = '<link rel="stylesheet" href="fonts/fonts.css">'

VINE = '''<svg viewBox="0 0 210 24" preserveAspectRatio="none">
<defs><linearGradient id="lf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8DB238"/><stop offset="1" stop-color="#2F5A14"/></linearGradient></defs>
<path d="M48.4 20.4 C54 20.4 56 10.6 64 10.2 C77 9.6 87 11.4 100 10.4 C114 9.4 126 9.7 136 11.0 C139.5 11.5 141.5 11.8 143.2 11.75" fill="none" stroke="#7E9112" stroke-width="0.45" stroke-linecap="round"/>
<path d="M48.4 20.4 C54 20.4 56 10.6 64 10.2 C77 9.6 87 11.4 100 10.4 C114 9.4 126 9.7 136 11.0 C139.5 11.5 141.5 11.8 143.2 11.75" fill="none" stroke="#B9C93A" stroke-width="0.12" stroke-dasharray="0.25 0.5" stroke-linecap="round"/>
<g transform="translate(78 10.3) rotate(-24)"><path d="M0 0 C1.6 -1.9 4.2 -2 5.8 0 C4.2 1.2 1.6 1.2 0 0Z" fill="url(#lf)"/></g>
<g transform="translate(113 9.7) rotate(-150) scale(1 -1)"><path d="M0 0 C1.6 -1.9 4.2 -2 5.8 0 C4.2 1.2 1.6 1.2 0 0Z" fill="url(#lf)"/></g>
<g transform="translate(127 10.2) rotate(-28)"><path d="M0 0 C1.3 -1.5 3.4 -1.6 4.6 0 C3.4 1 1.3 1 0 0Z" fill="url(#lf)"/></g>
</svg>'''

def footer(n):
    return f'''<div class="ft">{VINE}<img class="lot" src="a/ft_lotus.png"><img class="leaf" src="a/ft_leaf.png">
<div class="tag">EDGE CASE '26 × KEEP ALIVE '26</div><div class="pno">{n:02d}</div></div>'''

def frame(n, body, corners=True, foot=True):
    c = ''
    if corners: c += '<img class="corner-l" src="a/corner.png"><img class="corner-r" src="a/corner.png">'
    if foot: c += footer(n)
    return f'<section class="page">{c}{body}</section>'

LOCKUP = '''<div class="lockup"><img src="a/gdg_logo.png"><div><div class="l1">Google Developer Groups</div>
<div class="l2"><b>On Campus</b> · Indian Institute of Information Technology Nagpur</div></div></div>'''

pages = []

# ---------------- 1 COVER ----------------
pages.append(frame(1, f'''
<style>
.cv-top{{position:absolute;top:9mm;left:12mm;right:11mm;display:flex;justify-content:space-between;align-items:center;z-index:20}}
.cv-top .lockup{{gap:3.4mm}} .cv-top .lockup img{{height:13.2mm}} .cv-top .lockup .l1{{font-size:14.2pt}} .cv-top .lockup .l2{{font-size:8.9pt;margin-top:.5mm}}
.cv-fest{{position:absolute;top:31mm;left:0;right:0;text-align:center;z-index:20;font:800 15pt 'Poppins';letter-spacing:.04em;color:#fff;line-height:1.25}}
.cv-art{{position:absolute;top:47mm;left:50%;transform:translateX(-50%);width:172mm;z-index:10}}
.cv-art img{{width:100%;display:block}}
.screen{{position:absolute;left:28.2%;width:43.8%;top:19.6%;height:29.6%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.screen .pre{{font:700 5.6pt 'Poppins';letter-spacing:.22em;color:var(--gold2);margin-bottom:1.6mm}}
.screen .ev{{font-size:22.5pt}}
.screen .x{{font:800 11pt 'Unbounded';color:var(--gold);margin:.8mm 0}}
.cv-title{{position:absolute;bottom:17mm;left:0;right:0;text-align:center;z-index:20}}
.cv-title .t{{font:900 31pt 'Unbounded';color:var(--gold);letter-spacing:.09em;line-height:1.08;text-shadow:0 1mm 0 #4B0B33}}
.cv-title .s{{font:600 9.2pt 'Poppins';color:#fff;letter-spacing:.2em;margin-top:3mm;text-transform:uppercase}}
</style>
<div class="cv-top"><img src="a/gdg_logo.png" style="height:17.5mm"><img src="a/tf_logo26.png" style="height:24mm"></div>
<div class="cv-fest">IIIT NAGPUR'S<br>ANNUAL TECHNICAL FEST</div>
<div class="cv-art"><img src="a/cover_art.png">
  <div class="screen"><div class="pre">GDG ON CAMPUS IIIT NAGPUR PRESENTS</div>
   <div class="ev">EDGE CASE <span style="color:var(--gold2)">'26</span></div><div class="x">×</div>
   <div class="ev">KEEP ALIVE <span style="color:var(--gold2)">'26</span></div></div></div>
<div class="cv-title"><div class="t">SPONSORSHIP<br>BROCHURE</div>
<div class="s">Two national championships · Tantrafiesta 2026</div></div>
''', corners=False, foot=False))

# ---------------- 2 INDEX ----------------
idx = [("About IIIT Nagpur &amp; Tantrafiesta","03"),("About GDG on Campus","04"),("EDGE CASE '26","05"),("KEEP ALIVE '26","06"),
       ("Why Sponsor Us?","07"),("Your Reach in Nagpur","08"),("EDGE CASE Sponsor Tiers","09"),("KEEP ALIVE Tiers &amp; Bundles","10"),
       ("Nagpur Local Partners","11"),("Deliverables","12"),("How to Partner","13"),("Past Partners","14"),("Contact Us","15")]
rows = ''.join(f'<div class="ix"><span class="nm">{a}</span><span class="dots"></span><span class="pg">{b}</span></div>' for a,b in idx)
pages.append(frame(2, f'''
<style>
.ix-hd{{position:absolute;top:0;left:0;width:210mm;z-index:4}}
.ix-h{{position:absolute;top:30mm;left:0;right:0;z-index:8}}
.ix-list{{position:absolute;top:91mm;left:32mm;right:32mm;z-index:10}}
.ix{{display:flex;align-items:baseline;gap:3mm;margin-bottom:5.6mm}}
.ix .nm{{font:600 13pt 'Poppins';color:#fff;white-space:nowrap}}
.ix .dots{{flex:1;border-bottom:.55mm dotted rgba(245,174,26,.5);transform:translateY(-1.3mm)}}
.ix .pg{{font:400 16pt 'Lilita One';color:var(--gold)}}
</style>
<img class="ix-hd" src="a/tf_index_header.png">
<div class="ix-list">{rows}</div>
''', corners=False))

# ---------------- 3 ABOUT IIITN + TF (v1 content, re-spaced) ----------------
eds = [(2000,"2,000+","Life in<br>Future"),(4000,"4,000+","Greener<br>Tomorrow"),(10000,"10,000+","Genesis<br>Unleashed"),(20000,"20,000+","Digital<br>Big Bang"),(24000,"24,000+","Dark Matter<br>Eclipse"),(30000,"30,000+","The<br>Maximalism")]
bars=''
for v,lab,th in eds:
    h=max(3, 17*v/30000)
    bars+=f'<div class="jc"><div class="jv">{lab}</div><div class="jb" style="height:{h:.1f}mm"></div><div class="jt">{th}</div></div>'
bars+='<div class="jc now"><div class="jv">2026</div><div class="jb" style="height:20mm"><span>✦</span></div><div class="jt">ANANTA</div></div>'
pages.append(frame(3, f'''
<style>
.p3 .jb2{{text-align:justify;hyphens:auto;-webkit-hyphens:auto;line-height:1.65;font-size:10.4pt}}
.p3 .ph{{display:flex;justify-content:center;gap:12mm;margin-top:5mm}}
.p3 .ph img{{width:63mm;height:auto;display:block}}
.p3 .stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;margin-top:6mm}}
.p3 .stat{{text-align:center;padding:3.6mm 2mm}}
.p3 .stat .n{{font:400 28pt 'Lilita One';color:var(--gold);line-height:1}}
.p3 .stat .l{{font:600 8.8pt 'Poppins';color:#fff;margin-top:1.6mm}}
.jr{{margin-top:6mm;padding:4mm 6mm 3.5mm}}
.jr .hd{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3mm}}
.jr .hd .k{{font:700 8.2pt 'Poppins';letter-spacing:.24em;color:var(--gold2)}}
.jr .hd .s{{font:500 7.4pt 'Poppins';color:#CFC9F2;letter-spacing:.04em}}
.jg{{display:grid;grid-template-columns:repeat(7,1fr);gap:3mm;align-items:end;height:37mm;position:relative}}
.jg::after{{content:'';position:absolute;left:0;right:0;bottom:9.6mm;height:.6mm;border-radius:1mm;background:linear-gradient(90deg,var(--gb),var(--gr),var(--gy),var(--gg))}}
.jc{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end}}
.jv{{font:400 11.5pt 'Lilita One';color:var(--gold);margin-bottom:1.4mm;white-space:nowrap}}
.jb{{width:72%;border-radius:2.2mm 2.2mm 0 0;background:linear-gradient(180deg,#FFD36B,#E0A62B 55%,#B97A12);box-shadow:inset 0 0 0 .35mm rgba(255,255,255,.25)}}
.jt{{height:8mm;margin-top:1.6mm;width:120%;display:flex;align-items:flex-start;justify-content:center;text-align:center;font:600 6.6pt 'Poppins';color:#E6E1FF;line-height:1.2}}
.jc.now .jv{{color:var(--pink)}}
.jc.now .jb{{background:linear-gradient(180deg,rgba(247,163,204,.35),rgba(232,25,127,.15));border:.5mm dashed var(--pink);border-bottom:0;display:flex;align-items:flex-start;justify-content:center}}
.jc.now .jb span{{color:var(--pink);font-size:12pt;margin-top:2mm}}
.jc.now .jt{{color:var(--pink);font-weight:800;letter-spacing:.06em}}
</style>
<div class="content p3" style="top:23mm">
 <h1 class="h lg">ABOUT <span class="pink">IIIT NAGPUR</span></h1>
 <p class="body jb2" style="margin-top:5mm">The Indian Institute of Information Technology, Nagpur was established by the Ministry of Education, Government of India, under the Public-Private Partnership scheme, and is declared an <b>“Institution of National Importance”</b> under the IIIT (PPP) Act, 2017. In its short journey, IIITN has carved a niche for itself in education, research and community outreach.</p>
 <div class="ph"><img src="a/photo1.png"><img src="a/photo2.png"></div>
 <h1 class="h lg" style="margin-top:8mm">ABOUT <span class="pink">TANTRAFIESTA</span></h1>
 <p class="body jb2" style="margin-top:5mm">Tantrafiesta is the national-level annual technical fest of IIIT Nagpur and one of Central India's largest student-driven tech fests. This year's theme, <b>ANANTA: Surpassing the Possible</b>, celebrates technology's boundless potential through <b>Indian Maximalism</b>: vibrant, layered, distinctly Indian and unmistakably futuristic.</p>
 <div class="stats">
  <div class="stat panel"><div class="n">30K+</div><div class="l">Footfall</div></div>
  <div class="stat panel"><div class="n">2K+</div><div class="l">Participants Competing</div></div>
  <div class="stat panel"><div class="n">15M+</div><div class="l">Digital Impressions</div></div></div>
 <div class="panel jr">
  <div class="hd"><span class="k">THE JOURNEY SO FAR</span><span class="s">Footfall by edition</span></div>
  <div class="jg">{bars}</div>
 </div>
</div>
'''))

# ---------------- 4 GDG ON CAMPUS (v2 layout, updated hero text) ----------------
why = [("building","var(--gb)","Google-backed credibility","Your brand stands next to an official Google for Developers program."),
       ("rocket","var(--gr)","Builders, not just attendees","Our members ship real projects in AI/ML, hardware, cloud and web."),
       ("globe","var(--gy)","On Google's own platform","Our events are listed on gdg.community.dev, Google's developer community platform."),
       ("clock","var(--gg)","Reach all year round","Workshops, hackathons and tech talks run through the year, not just at the fest.")]
wy = ''.join(f'<div class="wy panel"><div class="wi" style="background:{c}">{ic(i,"#fff","6.5mm",2)}</div><div><div class="wt">{t}</div><div class="wd">{d}</div></div></div>' for i,c,t,d in why)
pages.append(frame(4, f'''
<style>
.gdg-hero{{display:flex;align-items:center;gap:7mm;margin-top:10mm}}
.gdg-hero img{{width:44mm}}
.big3{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:11mm}}
.big3 .b{{padding:7mm 3mm;text-align:center}}
.big3 .n{{font:400 27pt 'Lilita One';line-height:1}}
.big3 .l{{font:600 8.6pt 'Poppins';color:#fff;margin-top:1.6mm;line-height:1.35}}
.wys{{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:6mm}}
.wy{{display:flex;gap:3.5mm;align-items:flex-start;padding:6.5mm 5.5mm}}
.wi{{flex:none;width:11mm;height:11mm;border-radius:3.5mm;display:flex;align-items:center;justify-content:center}}
.wt{{font:400 12.5pt 'Lilita One';color:#fff}}
.wd{{font:500 8.6pt 'Poppins';color:#DDD8F8;line-height:1.45;margin-top:.8mm}}
</style>
<div class="content">
 <h1 class="h lg">GDG <span class="pink">ON CAMPUS</span></h1>
 <div class="kicker" style="margin-top:4mm">A GOOGLE FOR DEVELOPERS PROGRAM</div>
 <div class="gdg-hero"><img src="a/gdg_logo.png">
  <p class="body">Google Developer Groups on Campus is <b>Google's official university developer community program</b>, run by <b>Google for Developers</b> across 2,000+ campuses in 100+ countries. Our chapter at IIIT Nagpur brings students together to learn, build and ship, through workshops, hackathons, speaker sessions and flagship events like <b>EDGE CASE</b> and <b>KEEP ALIVE</b>.</p></div>
 <div class="big3">
  <div class="b panel"><div class="n" style="color:var(--gb)">1,658+</div><div class="l">members in our<br>GDG chapter</div></div>
  <div class="b panel"><div class="n" style="color:var(--gy)">2,000+</div><div class="l">GDG on Campus<br>chapters worldwide</div></div>
  <div class="b panel"><div class="n" style="color:var(--gg)">100+</div><div class="l">countries in the<br>Google network</div></div>
 </div>
 <div class="kicker tfk" style="margin-top:14mm"><img src="a/line_l.png"><span>WHY PARTNER WITH A GOOGLE DEVELOPER COMMUNITY</span><img class="r" src="a/line_l.png"></div>
 <div class="wys">{wy}</div>
 <p style="font:400 7pt 'Poppins';color:#B9B3DE;text-align:center;margin-top:9mm">GDG on Campus chapters are student-led and supported by Google for Developers.</p>
</div>
'''))

# ---------------- 5 EDGE CASE ----------------
tracks = [("Guardian","shield","var(--gb)","Safety &amp; health"),("Terra","leaf","var(--gg)","Sustainability &amp; agriculture"),("Forge","factory","var(--gy)","Industry 4.0"),("Wildcard","spark","var(--gr)","Anything bold")]
tk = ''.join(f'<div class="trk"><div class="ti" style="background:{c}">{ic(i,"#fff","7mm",2)}</div><div class="tn">{n}</div><div class="td">{d}</div></div>' for n,i,c,d in tracks)
steps = [("Sense","sensor","var(--gb)","Read real-world sensor data"),("Think","chip","var(--gy)","Decide with an on-device AI model"),("Act","gear","var(--gg)","Act physically on the world")]
st = ''
for k,(n,i,c,d) in enumerate(steps):
    st += f'<div class="sta"><div class="si" style="border-color:{c}">{ic(i,c,"10mm",1.7)}</div><div class="sn" style="color:{c}">{n.upper()}.</div><div class="sd">{d}</div></div>'
    if k<2: st += '<div class="arr"><svg viewBox="0 0 60 12" width="15mm" height="3mm"><path d="M0 6h52" stroke="#E0A62B" stroke-width="2" stroke-dasharray="4 3"/><path d="M50 1l9 5-9 5z" fill="#E0A62B"/></svg></div>'
EVCSS = '''<style>
.flow{display:flex;align-items:flex-start;justify-content:center;gap:1mm;margin-top:11mm}
.sta{width:44mm;text-align:center}
.si{width:21mm;height:21mm;border-radius:50%;border:1mm solid;margin:0 auto;display:flex;align-items:center;justify-content:center;background:rgba(20,15,66,.85)}
.sn{font:400 16pt 'Lilita One';margin-top:2.2mm}
.sd{font:500 8.6pt 'Poppins';color:#E8E4FF;line-height:1.4;margin-top:.5mm}
.arr{padding-top:9mm}
.trks{display:grid;grid-template-columns:repeat(4,1fr);gap:3.5mm;margin-top:4mm}
.trk{text-align:center;padding:5mm 2mm;background:rgba(20,15,66,.8);border-radius:4mm;border:.4mm solid rgba(224,166,43,.6)}
.ti{width:12mm;height:12mm;border-radius:3.5mm;display:flex;align-items:center;justify-content:center;margin:0 auto 2mm}
.tn{font:400 13pt 'Lilita One';color:#fff}
.td{font:500 7.8pt 'Poppins';color:#D8D3F6;line-height:1.35;margin-top:.5mm}
.fmt{display:grid;grid-template-columns:1.2fr 1fr;gap:4mm;margin-top:12mm}
.tlv{padding:6.5mm 6mm}
.tlv .r{display:flex;gap:3mm;align-items:flex-start;margin-bottom:3.6mm}
.tlv .r:last-child{margin-bottom:0}
.tlv .k{flex:none;width:19mm;font:700 7.8pt 'JetBrains Mono';color:var(--gold);padding-top:.5mm;letter-spacing:.04em}
.tlv .v{font:500 8.9pt 'Poppins';color:#F0ECFF;line-height:1.45}
.prz{padding:5.5mm;display:flex;flex-direction:column;justify-content:center;text-align:center}
.prz .big{font:400 36pt 'Lilita One';color:var(--gold);line-height:1;margin-top:2mm}
.prz .sub{font:500 8.6pt 'Poppins';color:#DDD8F8;line-height:1.45;margin-top:3mm}
</style>'''
pages.append(frame(5, EVCSS + f'''
<div class="content" style="top:24mm">
 <div class="kicker">NATIONAL PHYSICAL-AI HARDWARE HACKATHON</div>
 <div class="ev center" style="margin-top:3.5mm;font-size:44pt">EDGE CASE <span style="color:var(--gold2)">'26</span></div>
 <p class="body center" style="margin-top:6mm">A national <b><span class=nw>24-hour</span> Physical AI hackathon</b>. Student teams build real devices that read sensor data, decide with an <b>on-device AI model</b> and act on the world, live on campus at Tantrafiesta '26.</p>
 <div class="flow">{st}</div>
 <div class="kicker tfk" style="margin-top:12mm"><img src="a/line_l.png"><span>FOUR TRACKS</span><img class="r" src="a/line_l.png"></div>
 <div class="trks">{tk}</div>
 <div class="fmt">
  <div class="panel tlv">
   <div class="kicker" style="text-align:left;margin-bottom:4mm">HOW IT RUNS</div>
   <div class="r"><div class="k">REACH</div><div class="v">Free registration on Unstop, with <b>200–300 teams</b> targeted from across India</div></div>
   <div class="r"><div class="k">ROUND 1</div><div class="v">Online idea round</div></div>
   <div class="r"><div class="k">SHORTLIST</div><div class="v">Top <b>40</b> teams shortlisted; top <b>25</b> build on campus</div></div>
   <div class="r"><div class="k">FINALE</div><div class="v"><b><span class=nw>24-hour</span> on-site build</b>, demos and judging at Tantrafiesta '26</div></div>
  </div>
  <div class="panel prz">
   <div class="kicker">PRIZE POOL</div>
   <div class="big">₹50,000+</div>
   <div class="sub">Podium prizes plus special awards, including Best On-Device AI and Best PCB Design</div>
  </div>
 </div>
</div>
'''))

# ---------------- 6 KEEP ALIVE ----------------
log = [("19:42:07","ALERT","#EA4335","checkout-svc · p99 latency &gt; 2s"),("19:42:31","ACK","#FBBC04","team-07 is on-call"),("19:43:50","TRACE","#4285F4","cart-svc → redis: connection refused"),("19:44:58","FIX","#4285F4","rollback checkout-svc → v1.4.2"),("19:45:10","OK","#34A853","SLO restored · error budget safe")]
lg = ''.join(f'<div class="ln"><span class="tm">[{t}]</span><span class="lv" style="color:{c}">{l}</span><span class="ms">{m}</span></div>' for t,l,c,m in log)
pages.append(frame(6, EVCSS + f'''
<style>
.term{{background:#0B0F14;border:.6mm solid #34A853;border-radius:4mm;overflow:hidden;margin-top:10mm}}
.term .bar{{display:flex;gap:1.5mm;align-items:center;padding:2.2mm 3.5mm;background:#161B22;border-bottom:.3mm solid #263040}}
.term .bar i{{width:2.6mm;height:2.6mm;border-radius:50%;display:block}}
.term .bar span{{font:600 7pt 'JetBrains Mono';color:#8B949E;margin-left:2mm}}
.term .bd{{padding:3.5mm 5mm 2.5mm}}
.ln{{font:500 8.8pt 'JetBrains Mono';color:#C9D1D9;margin-bottom:2mm;white-space:nowrap}}
.ln .tm{{color:#6E7681;margin-right:3mm}} .ln .lv{{display:inline-block;width:14mm;font-weight:800}}
.hb{{display:block;width:100%;height:13mm}}
.ka3{{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm;margin-top:10mm}}
.ka3 .c{{padding:6.5mm 3mm;text-align:center}}
.ka3 .c .t{{font:400 13pt 'Lilita One';color:#fff;margin-top:2mm}}
.ka3 .c .d{{font:500 8.2pt 'Poppins';color:#D8D3F6;line-height:1.4;margin-top:1mm}}
</style>
<div class="content" style="top:24mm">
 <div class="kicker">NATIONAL INCIDENT RESPONSE (SRE) CHAMPIONSHIP</div>
 <div class="ev center" style="margin-top:3.5mm;font-size:44pt">KEEP ALIVE <span style="color:var(--gold2)">'26</span></div>
 <p class="body center" style="margin-top:6mm">Student teams <b>run on-call for a live cloud application</b> while faults are injected in real time. The top 15 teams keep a live Kubernetes system running on campus, then defend a <b>blameless postmortem</b>.</p>
 <div class="term"><div class="bar"><i style="background:#EA4335"></i><i style="background:#FBBC04"></i><i style="background:#34A853"></i><span>keep-alive@tantrafiesta:~$ tail -f incidents.log</span></div>
  <svg class="hb" viewBox="0 0 400 40" preserveAspectRatio="none"><path d="M0 22 H120 L130 22 L138 8 L146 34 L154 22 H210 L222 22 L230 2 L240 38 L250 22 H400" fill="none" stroke="#34A853" stroke-width="2.2"/><path d="M222 22 L230 2 L240 38 L250 22" fill="none" stroke="#EA4335" stroke-width="2.4"/></svg>
  <div class="bd">{lg}</div></div>
 <div class="ka3">
  <div class="c panel">{ic("eye","#4285F4","9mm")}<div class="t">Observe</div><div class="d">Metrics, logs and traces to find the fault fast</div></div>
  <div class="c panel">{ic("server","#FBBC04","9mm")}<div class="t">Recover</div><div class="d">Restore a live Kubernetes system under pressure</div></div>
  <div class="c panel">{ic("book","#34A853","9mm")}<div class="t">Postmortem</div><div class="d">Defend a blameless postmortem before the judges</div></div>
 </div>
 <div class="fmt">
  <div class="panel tlv">
   <div class="kicker" style="text-align:left;margin-bottom:4mm">HOW IT RUNS</div>
   <div class="r"><div class="k">ROUND 1</div><div class="v">Online triage round, open to colleges across India</div></div>
   <div class="r"><div class="k">FINALE</div><div class="v">Top <b>15 teams</b> go on-call on campus at Tantrafiesta '26</div></div>
   <div class="r"><div class="k">FOR</div><div class="v">Students with about a year of hands-on DevOps or cloud</div></div>
  </div>
  <div class="panel prz">
   <div class="kicker">PRIZE POOL</div>
   <div class="big">₹25,000+</div>
   <div class="sub">Prize and award partners can grow the pool further</div>
  </div>
 </div>
</div>
'''))

# ---------------- 7 WHY SPONSOR ----------------
reasons = [("users","var(--gb)","National talent","Teams from colleges across India compete, with the finals held live in Nagpur."),
           ("rocket","var(--gr)","Skills in demand","Edge-AI hardware and DevOps / SRE, the skills recruiters are hunting for."),
           ("building","var(--gy)","Credible hosts","An Institution of National Importance and a Google Developer Groups chapter."),
           ("stage","var(--gg)","Your brand on stage","Named awards, judge seats and stage time in front of the finalists and the fest crowd."),
           ("brief","var(--gb)","Hire early","Meet the top teams for internship interviews, entirely at your discretion."),
           ("receipt","var(--gr)","CSR &amp; tax benefits","IIIT Nagpur is CSR-registered, and payments are eligible for 80(G) deduction.")]
rs = ''.join(f'<div class="rs panel"><div class="ri" style="background:{c}">{ic(i,"#fff","6.5mm",2)}</div><div><div class="rt">{t}</div><div class="rd">{d}</div></div></div>' for i,c,t,d in reasons)
pages.append(frame(7, f'''
<style>
.ws2{{display:flex;align-items:center;justify-content:space-around;margin-top:11mm}}
.ws2 .s{{text-align:center;width:48mm}}
.ws2 .ti{{height:13mm;display:block;margin:0 auto}}
.ws2 .n{{font:400 36pt 'Lilita One';color:var(--gold);line-height:1;margin-top:3mm}}
.ws2 .l{{font:600 9.6pt 'Poppins';color:#fff;margin-top:2mm}}
.ws2 .vd{{height:38mm;width:auto}}
.ws .s{{text-align:center;padding:8mm 2mm}}
.ws .s .n{{font:400 36pt 'Lilita One';color:var(--gold);line-height:1;margin-top:2mm}}
.ws .s .l{{font:600 9.2pt 'Poppins';color:#fff;margin-top:1.8mm}}
.rsg{{display:grid;grid-template-columns:1fr 1fr;gap:5.5mm;margin-top:9mm}}
.rs{{display:flex;gap:3.5mm;align-items:flex-start;padding:7mm 5.5mm}}
.ri{{flex:none;width:11mm;height:11mm;border-radius:3.5mm;display:flex;align-items:center;justify-content:center}}
.rt{{font:400 12.5pt 'Lilita One';color:#fff}}
.rd{{font:500 8.6pt 'Poppins';color:#DDD8F8;line-height:1.45;margin-top:.8mm}}
</style>
<div class="content">
 <h1 class="h lg">WHY <span class="pink">SPONSOR US?</span></h1>
 <p class="body center" style="margin-top:6mm">Partner with one of <b>Central India's largest student-driven tech fests</b>, through two championships built around the skills India is hiring for.</p>
 <div class="ws2">
  <div class="s"><img class="ti" src="a/ic_people.png"><div class="n">30K+</div><div class="l">Footfall</div></div>
  <img class="vd" src="a/vdiv.png">
  <div class="s"><img class="ti" src="a/ic_trophy.png"><div class="n">2K+</div><div class="l">Participants Competing</div></div>
  <img class="vd" src="a/vdiv.png">
  <div class="s"><img class="ti" src="a/ic_eye.png"><div class="n">15M+</div><div class="l">Digital Impressions</div></div>
 </div>
 <img src="a/orn_div.png" style="display:block;width:118mm;margin:9mm auto 0">
 <div class="rsg">{rs}</div>
</div>
'''))

# ---------------- 8 NAGPUR REACH ----------------
chan_l = [("insta","Instagram","Reels and posts by Tantrafiesta and GDG IIITN"),("mega","WhatsApp","Shoutouts across Nagpur college communities"),("handshake","Collab posts","With Nagpur college clubs and GDG chapters")]
chan_r = [("users","Ambassadors","Sharing across campuses all over Nagpur"),("pin","On-ground","Branding in front of 30K+ fest footfall"),("globe","Unstop &amp; email","Listing views and mails to every registrant")]
def chan(lst, side):
    return ''.join(f'<div class="ch {side}"><div class="chi">{ic(i,"#1E1858","5.5mm",2)}</div><div class="chx"><div class="cht">{t}</div><div class="chd">{d}</div></div></div>' for i,t,d in lst)
gets = [("eye","Your logo on posters and our Nagpur Partners post"),("insta","Instagram shoutouts to students across Nagpur"),
        ("gift","Your flyer or offer in every participant kit"),("stage","A stall or sampling spot at the fest"),
        ("trophy","An “Official Partner” certificate for your counter")]
gt = ''.join(f'<div class="gt">{ic(i,"#F5AE1A","5.5mm",2)}<span>{t}</span></div>' for i,t in gets)
pages.append(frame(8, f'''
<style>
.nr{{display:grid;grid-template-columns:1fr 60mm 1fr;align-items:center;gap:4mm;margin-top:12mm}}
.nr .col{{display:flex;flex-direction:column;gap:5mm}}
.ch{{display:flex;align-items:center;gap:2.8mm;height:17mm;background:rgba(20,15,66,.86);border:.4mm solid rgba(224,166,43,.7);border-radius:3.5mm;padding:0 3.4mm}}
.ch.l{{flex-direction:row-reverse;text-align:right}}
.chx{{flex:1;min-width:0}}
.chi{{flex:none;width:9mm;height:9mm;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center}}
.cht{{font:700 9pt 'Poppins';color:#fff;line-height:1.25;white-space:nowrap}}
.chd{{font:500 7.1pt 'Poppins';color:#CFC9F2;line-height:1.35;margin-top:.5mm}}
.core{{width:60mm;height:60mm;border-radius:50%;margin:0 auto;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 background:radial-gradient(circle at 50% 40%, #3A2C93, #191352 70%);border:1.4mm solid var(--gold);box-shadow:0 0 0 2.2mm rgba(232,25,127,.55),0 0 0 4.4mm rgba(66,133,244,.35)}}
.core .n{{font:400 36pt 'Lilita One';color:var(--gold);line-height:.95;-webkit-text-stroke:1.2mm var(--mag);paint-order:stroke fill}}
.core .t{{font:700 8.6pt 'Poppins';color:#fff;line-height:1.3;margin-top:2mm;padding:0 7mm}}
.gts{{display:grid;grid-template-columns:1fr 1fr;gap:4.5mm 6mm;margin-top:4.5mm}}
.gt{{display:flex;gap:2.6mm;align-items:center;font:500 9pt 'Poppins';color:#F0ECFF;line-height:1.4}}
</style>
<div class="content">
 <div class="kicker">FOR NAGPUR BUSINESSES</div>
 <h1 class="h lg" style="margin-top:3mm">YOUR REACH <span class="pink">IN NAGPUR</span></h1>
 <p class="body center" style="margin-top:6mm">We take your brand to <b>students all over Nagpur</b>, the city's most social, most loyal customers, before, during and after the fest.</p>
 <div class="nr"><div class="col">{chan(chan_l,"l")}</div>
  <div class="core"><div class="n">2 LAKH+</div><div class="t">impressions from students all over Nagpur</div></div>
  <div class="col">{chan(chan_r,"r")}</div></div>
 <div class="panel" style="padding:7mm 6.5mm;margin-top:13mm">
  <div class="kicker tfk" style="margin-bottom:2mm"><img src="a/line_l.png"><span>WHAT YOU GET BACK</span><img class="r" src="a/line_l.png"></div>
  <div class="gts">{gt}</div>
 </div>
 <div class="band" style="margin-top:11mm">{ic("heart","#1E1858","7mm",2.2)}<div><b>Students are Nagpur's most social customers.</b> Every reel shared and every stall visit brings their friends to your door.</div></div>
</div>
'''))

# ---------------- tier card helper ----------------
TCSS = '''<style>
.tr{padding:5.5mm 6.5mm 4.5mm;margin-top:5mm}
.tl1{display:flex;align-items:center;gap:4.5mm}
.tl1 img{width:15.5mm}
.tnm{font:400 21pt 'Lilita One';color:#fff;line-height:1}
.trl{font:700 8.8pt 'Poppins';letter-spacing:.14em;text-transform:uppercase;margin-top:1.4mm}
.tsl{font:600 7.6pt 'JetBrains Mono';color:#CFC9F2;margin-top:1.2mm}
.tpr{margin-left:auto;text-align:right}
.tpr .price{font-size:28pt}
ul.tick.tcols{columns:2;column-gap:7mm;margin-top:4.5mm;padding-top:4mm;border-top:.3mm solid rgba(224,166,43,.35)}
ul.tick.tcols li{break-inside:avoid;margin-bottom:1.9mm}
</style>'''
def tier(badge, name, sub, role, slots, price, bullets, accent):
    bl = ''.join(f'<li>{b}</li>' for b in bullets)
    return f'''<div class="card tr" style="border-color:{accent}">
 <div class="tl1"><img src="a/{badge}"><div><div class="tnm">{name}{sub}</div><div class="trl" style="color:{accent}">{role}</div><div class="tsl">{slots}</div></div>
 <div class="tpr"><div class="price">{price}</div></div></div>
 <ul class="tick tcols">{bl}</ul></div>'''

# ---------------- 9 EDGE CASE TIERS ----------------
pages.append(frame(9, TCSS + f'''
<div class="content" style="top:21mm">
 <div class="kicker">EDGE CASE '26 · SPONSOR TIERS</div>
 <h1 class="h lg" style="margin-top:3mm">POWER <span class="pink">THE BUILD</span></h1>
 {tier("b_diamond.png","ACTUATOR","","Title Partner","1 slot","₹25,000",[
   "<b>“EDGE CASE '26 powered by You”</b> on every creative and on stage",
   "Logo at the top of posters, banners and certificates",
   "2 dedicated reels + 2 dedicated posts",
   "Judge seat, and present the winners' trophy",
   "Standee or stall at the <span class=nw>24-hour</span> build hall",
   "Meet the top teams for internship interviews"],"#F7A3CC")}
 {tier("b_plat.png","PROCESSOR","","Track Partner","4 slots · Guardian · Terra · Forge · Wildcard","₹15,000",[
   "Your name on a track: <b>“Guardian Track by You”</b>",
   "Track judge seat and co-branded winner certificates",
   "1 dedicated reel + 1 dedicated post",
   "Logo on posters, banners and the Unstop listing",
   "Standee at the build hall",
   "Meet your track's top teams"],"#9FD0FF")}
 {tier("b_gold.png","SENSOR","","Award Partner","6 slots · Special Awards","₹5,000",[
   "Name a special award, e.g. <b>“Best On-Device AI by You”</b>",
   "Present your award on stage",
   "1 dedicated post + logo on event creatives",
   "Your brand on the award winners' certificates"],"#FFD36B")}
 <div class="card" style="border-style:dashed;display:flex;align-items:center;gap:4.5mm;padding:4.5mm 6mm;margin-top:5mm">{ic("cpu","#F5AE1A","11mm",1.8)}
  <div><div style="font:400 14pt 'Lilita One'">COMPONENTS PARTNER <span style="font:600 8pt 'Poppins';color:var(--muted)">· in-kind</span></div>
  <div style="font:500 8.8pt 'Poppins';color:#E6E1FF;line-height:1.45;margin-top:1mm">Sensors, dev boards, PCB fabrication or store vouchers for the winners, credited at retail value to the matching tier.</div></div></div>
</div>
'''))

# ---------------- 10 KEEP ALIVE TIERS + BUNDLES ----------------
def nines(n,c): return f' <span class="mono" style="font-size:11pt;color:{c}">{n}</span>'
bundles = [("FULL STACK","Actuator + Five Nines","₹50,000","₹45,000"),("DUAL CORE","Processor + Four Nines","₹30,000","₹27,000"),("SIGNAL PAIR","Sensor + Three Nines","₹12,500","₹11,000")]
bd = ''.join(f'<div class="bdl"><div class="bn">{n}</div><div class="bc">{c}</div><div class="bo">{o}</div><div class="bp">{p}</div></div>' for n,c,o,p in bundles)
pages.append(frame(10, TCSS + f'''
<style>
.bds{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:4mm}}
.bdl{{text-align:center;padding:4mm 2mm 3.5mm;border-radius:4mm;background:linear-gradient(180deg,#3A1460,#22114E);border:.5mm solid var(--hot)}}
.bn{{font:400 14.5pt 'Lilita One';color:#fff}} .bc{{font:500 7.6pt 'Poppins';color:#E6C6E0;margin-top:.6mm}}
.bo{{font:500 8.4pt 'JetBrains Mono';color:#B9A6CF;text-decoration:line-through;margin-top:2.5mm}}
.bp{{font:400 22pt 'Lilita One';color:var(--gold);line-height:1.1}}
</style>
<div class="content" style="top:21mm">
 <div class="kicker">KEEP ALIVE '26 · SPONSOR TIERS</div>
 <h1 class="h lg" style="margin-top:3mm">GUARANTEE <span class="pink">THE UPTIME</span></h1>
 {tier("b_diamond.png","FIVE NINES",nines("99.999%","#34A853"),"Prize Partner","1 slot","₹25,000",[
   "<b>“KEEP ALIVE '26 prize pool powered by You”</b>",
   "Logo at the top of posters, Unstop and the finale screen",
   "2 dedicated reels + 2 dedicated posts",
   "Judge seat, and present the prizes on stage",
   "Your brand on the winners' certificates",
   "Meet the top teams for internship interviews"],"#34A853")}
 {tier("b_plat.png","FOUR NINES",nines("99.99%","#4285F4"),"Award Partner","2 slots · Fastest Recovery · Best Postmortem","₹15,000",[
   "Name an award: <b>“Fastest Recovery by You”</b>",
   "Present your award on stage, plus a judge seat",
   "1 dedicated reel + 1 dedicated post",
   "Logo on posters, banners and the Unstop listing"],"#4285F4")}
 {tier("b_gold.png","THREE NINES",nines("99.9%","#FBBC04"),"Supporting Partner","Open slots","₹7,500",[
   "Logo on posters and the Unstop listing",
   "1 dedicated post",
   "Standee at the finale war-room",
   "Your flyer in every finalist kit"],"#FBBC04")}
 <div class="kicker tfk" style="margin-top:6mm"><img src="a/line_l.png"><span>SPONSOR BOTH EVENTS · BUNDLES</span><img class="r" src="a/line_l.png"></div>
 <div class="bds">{bd}</div>
</div>
'''))

# ---------------- 11 LOCAL PARTNERS ----------------
lad = [("b_bronze.png","LOCAL FRIEND","₹2,500",["Your logo on our “Nagpur Partners” post","“Official Partner” certificate"],"#E9A27A"),
       ("b_silver.png","COMMUNITY PARTNER","₹5,000",["Everything in Local Friend","Instagram story shoutout","Your flyer in every participant kit"],"#D6DCE8"),
       ("b_gold.png","SPOTLIGHT PARTNER","₹10,000",["Everything in Community","A dedicated Instagram post","A stall or sampling spot at the fest","Your logo on the event banner"],"#FFD36B")]
ld = ''.join(f'<div class="card ld" style="border-color:{c}"><img src="a/{b}"><div class="ldn" style="color:{c}">{n}</div><div class="price" style="font-size:25pt;margin-top:1.5mm">{p}</div><ul class="tick" style="margin-top:4.5mm;text-align:left">{"".join(f"<li>{x}</li>" for x in bl)}</ul></div>' for b,n,p,bl,c in lad)
ink = [("coffee","Midnight Fuel","Snacks and coffee for the <span class=nw>24-hour</span> build"),("gift","Goodies &amp; Merch","T-shirts, stickers, totes and lanyards"),
       ("cpu","Components","Sensors, boards and tool vouchers"),("printer","Printing","Standees, certificates and ID cards"),
       ("book","Learning","Course seats and scholarships"),("mega","Media","Coverage before and after the fest")]
ik = ''.join(f'<div class="ik"><div class="iki">{ic(i,"#F5AE1A","7.5mm",1.8)}</div><div class="ikt">{t}</div><div class="ikd">{d}</div></div>' for i,t,d in ink)
pages.append(frame(11, f'''
<style>
.lds{{display:grid;grid-template-columns:repeat(3,1fr);gap:4.5mm;margin-top:7mm;align-items:stretch}}
.ld{{padding:5.5mm 4.5mm;text-align:center}}
.ld img{{height:17mm}}
.ldn{{font:800 9pt 'Poppins';letter-spacing:.1em;margin-top:2mm}}
.iks{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:4mm}}
.ik{{text-align:center;padding:4.5mm 3mm;background:rgba(20,15,66,.85);border-radius:3.5mm;border:.4mm solid rgba(224,166,43,.6)}}
.iki{{width:13mm;height:13mm;border-radius:50%;border:.5mm solid var(--gold);margin:0 auto 2mm;display:flex;align-items:center;justify-content:center}}
.ikt{{font:400 12pt 'Lilita One';color:#fff}}
.ikd{{font:500 7.8pt 'Poppins';color:#D2CDF2;line-height:1.4;margin-top:.8mm}}
</style>
<div class="content" style="top:23mm">
 <div class="kicker">FOR CAFÉS · SHOPS · BRANDS · INSTITUTES</div>
 <h1 class="h lg" style="margin-top:3mm">NAGPUR <span class="pink">LOCAL PARTNERS</span></h1>
 <p class="body center" style="margin-top:6mm">Partnerships sized for Nagpur businesses. Pick a tier, or support us <b>in kind</b> with your products and services.</p>
 <div class="lds">{ld}</div>
 <div class="kicker tfk" style="margin-top:8mm"><img src="a/line_l.png"><span>PREFER TO GIVE PRODUCT INSTEAD OF CASH?</span><img class="r" src="a/line_l.png"></div>
 <div class="iks">{ik}</div>
 <p style="font:500 8pt 'Poppins';color:#CFC9F2;text-align:center;margin-top:4mm">In-kind support is credited at retail value to the matching tier, with an “Official Partner” title.</p>
</div>
'''))

# ---------------- 12 DELIVERABLES ----------------
Y='<img class="tk" src="a/tick.png">'; N='<span class="n">—</span>'
def t(x): return f'<span class="tx">{x}</span>'
rows = [("“Powered by” naming",[Y,N,N,N,N,N]),("Named track / award",[N,Y,t("Sensor"),N,N,N]),("Logo on the Unstop listing",[Y,Y,Y,N,N,N]),
        ("Logo on posters &amp; banners",[Y,Y,Y,t("Banner"),N,N]),("Logo on the Tantrafiesta website",[Y,Y,Y,N,N,N]),
        ("Dedicated reels",[t("2"),t("1"),N,N,N,N]),("Dedicated Instagram posts",[t("2"),t("1"),t("1"),t("1"),N,N]),
        ("Instagram story shoutout",[Y,Y,Y,Y,Y,N]),("“Nagpur Partners” post",[Y,Y,Y,Y,Y,Y]),
        ("WhatsApp community shoutouts",[t("3"),t("2"),t("1"),N,N,N]),("Standee / stall at venue",[t("Stall"),t("Standee"),t("Standee"),t("Stall"),N,N]),
        ("Present on stage",[Y,Y,t("Award"),N,N,N]),("Judge seat",[Y,Y,N,N,N,N]),
        ("Flyer in participant kits",[Y,Y,Y,Y,Y,N]),("Meet top teams for internships",[Y,Y,N,N,N,N]),
        ("“Official Partner” certificate",[Y,Y,Y,Y,Y,Y]),("Post-event report",[Y,Y,Y,N,N,N])]
hdr = [("TITLE","Actuator · Five Nines","₹25K"),("CORE","Processor · Four Nines","₹15K"),("SUPPORTING","Sensor · Three Nines","₹5K–7.5K"),("SPOTLIGHT","Local partner","₹10K"),("COMMUNITY","Local partner","₹5K"),("FRIEND","Local partner","₹2.5K")]
th = '<th class="perk">PERKS</th>' + ''.join(f'<th><div class="a">{a}</div><div class="b">{b}</div><div class="c">{c}</div></th>' for a,b,c in hdr)
tb = ''.join(f'<tr><td class="perk">{r}</td>' + ''.join(f'<td>{v}</td>' for v in vals) + '</tr>' for r,vals in rows)
pages.append(frame(12, f'''
<style>
table.dv{{width:100%;border-collapse:separate;border-spacing:0;margin-top:8mm;border:.6mm solid var(--frame);border-radius:4mm;overflow:hidden;background:rgba(20,15,66,.9)}}
.dv th{{background:linear-gradient(180deg,#B0226C,#7E1650);color:#fff;padding:2.8mm 1mm;text-align:center;vertical-align:middle;border-left:.3mm solid rgba(255,255,255,.18)}}
.dv th .a{{font:400 10.5pt 'Lilita One';color:var(--gold2)}}
.dv th .b{{font:500 5.8pt 'Poppins';color:#F8D9EA;line-height:1.25;margin-top:.5mm}}
.dv th .c{{font:700 8pt 'JetBrains Mono';color:#fff;margin-top:.7mm}}
.dv th.perk{{font:400 13pt 'Lilita One';color:var(--gold2);border-left:0;text-align:left;padding-left:4mm}}
.dv td{{text-align:center;padding:2.75mm 1mm;font:500 8.3pt 'Poppins';border-top:.3mm solid rgba(224,166,43,.28);border-left:.3mm solid rgba(224,166,43,.18)}}
.dv td.perk{{text-align:left;padding-left:4mm;font:600 8.4pt 'Poppins';color:#fff;border-left:0;width:50mm}}
.dv tr:nth-child(even) td{{background:rgba(255,255,255,.035)}}
.dv .tk{{height:4.2mm;display:block;margin:0 auto}} .dv .n{{color:#6F68A8}} .dv .tx{{color:var(--pink);font-weight:700;font-size:7.8pt}}
</style>
<div class="content">
 <h1 class="h lg">DELIVERABLES</h1>
 <table class="dv"><tr>{th}</tr>{tb}</table>
 <p style="font:500 7.8pt 'Poppins';color:#CFC9F2;margin-top:4mm;line-height:1.55">On-campus branding is displayed during event days. In-kind partners receive the deliverables of the tier matching their retail value. Final perks are as per the MoU signed.</p>
</div>
'''))

# ---------------- 13 HOW TO PARTNER + POLICIES ----------------
steps3 = [("1","Pick your slot","Choose a tier, an award, a track or an in-kind category."),("2","Sign the MoU","We formalise the amount and perks in an MoU with IIIT Nagpur."),("3","Pay &amp; share assets","Transfer the amount and send us your logo and brand assets.")]
s3 = ''.join(f'<div class="s3"><div class="s3n">{n}</div><div class="s3t">{t_}</div><div class="s3d">{d}</div></div>' for n,t_,d in steps3)
pol = ["All cheques / DDs are to be drawn in favour of <b>IIIT Nagpur Gymkhana</b>.",
       "All payments are eligible for deduction under <b>Section 80(G)</b> of the Income Tax Act, 1961. IIIT Nagpur is CSR-registered.",
       "Every partnership is formalised through an <b>MoU with IIIT Nagpur</b>; perks are event-specific and as per the MoU signed.",
       "Slots are limited and allotted on a first-come, first-served basis on MoU signature.",
       "Any other proposal or counter-offer is welcome before signing; no changes after the MoU is signed.",
       "On-campus branding, stalls and sampling run during event days.",
       "Logos and brand assets should reach us at least 7 days before the event for print.",
       "Decisions on the final offering rest solely with the organisers."]
pl = ''.join(f'<li>{x}</li>' for x in pol)
pages.append(frame(13, f'''
<style>
.s3s{{display:grid;grid-template-columns:repeat(3,1fr);gap:4.5mm;margin-top:8mm}}
.s3{{text-align:center;padding:6.5mm 3.5mm;background:rgba(20,15,66,.85);border:.5mm solid var(--frame);border-radius:4mm}}
.s3n{{width:12mm;height:12mm;border-radius:50%;margin:0 auto;background:var(--hot);color:#fff;font:400 17pt 'Lilita One';display:flex;align-items:center;justify-content:center;border:.8mm solid var(--gold)}}
.s3t{{font:400 13.5pt 'Lilita One';color:#fff;margin-top:2.5mm}} .s3d{{font:500 8.4pt 'Poppins';color:#D8D3F6;line-height:1.45;margin-top:1mm}}
ul.pol{{margin:7mm 0 0;padding:0;list-style:none}}
ul.pol li{{position:relative;padding-left:7mm;font:400 10.4pt 'Poppins';line-height:1.55;color:#EEEAFF;margin-bottom:5mm}}
ul.pol li b{{color:#fff;font-weight:600}}
ul.pol li::before{{content:'✦';position:absolute;left:0;top:0;color:var(--pink);font-size:10pt}}
</style>
<div class="content">
 <h1 class="h lg">HOW TO <span class="pink">PARTNER</span></h1>
 <div class="s3s">{s3}</div>
 <h1 class="h md" style="margin-top:13mm">ASSOCIATION <span class="pink">POLICIES</span></h1>
 <ul class="pol">{pl}</ul>
 <div class="band" style="margin-top:9mm">{ic("handshake","#1E1858","7mm",2.2)}<div><b>Have something else in mind?</b> Write to <a href="mailto:gdg@iiitn.ac.in" style="font-weight:700">gdg@iiitn.ac.in</a> and we'll tailor a partnership around your brand.</div></div>
</div>
'''))

# ---------------- 14 PAST PARTNERS ----------------
pages.append(frame(14, f'''
<style>.spimg{{display:block;margin:0 auto;border:.8mm solid var(--frame);border-radius:4mm}}</style>
<div class="content">
 <h1 class="h lg">PAST <span class="pink">PARTNERS</span></h1>
 <div class="kicker" style="margin-top:4.5mm">BRANDS THAT HAVE PARTNERED WITH TANTRAFIESTA</div>
 <img class="spimg" src="a/sp1.png" style="width:128mm;margin-top:6mm">
 <img class="spimg" src="a/sp2.png" style="width:128mm;margin-top:4.5mm">
</div>
'''))

# ---------------- 15 CONTACT ----------------
IG='https://www.instagram.com/gdg_iiitn/'
GC='https://gdg.community.dev/gdg-on-campus-indian-institute-of-information-technology-nagpur-india/'
lotus = '<img src="a/ic_lotus.png" style="height:8.5mm;display:block;margin:0 auto">'
pages.append(frame(15, f'''
<style>
.pp{{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:12mm}}
.pc{{text-align:center;padding:9mm 4mm}}
.pc .rl{{font:700 9.5pt 'Poppins';color:var(--gold);margin-top:2mm}}
.pc .nm{{font:700 19pt 'Poppins';color:#fff;line-height:1.2;margin-top:1.2mm}}
.pc .ln{{display:flex;align-items:center;justify-content:center;gap:2mm;font:600 9.6pt 'Poppins';color:#fff;margin-top:2.6mm}}
.pc a{{border-bottom:.3mm solid rgba(247,163,204,.6)}}
.so{{display:grid;grid-template-columns:repeat(3,1fr);gap:4.5mm;margin-top:6mm}}
.sc{{text-align:center;padding:7.5mm 3mm}}
.sc .qr{{width:36mm;height:36mm;border-radius:2.5mm;border:1mm solid #fff;margin:4mm auto 0;display:block}}
.sc .v{{font:700 9.4pt 'Poppins';color:#fff;margin-top:3mm;line-height:1.35}}
.sc .v a{{border-bottom:.3mm solid rgba(247,163,204,.6)}}
.sc .k{{font:600 7.6pt 'Poppins';color:var(--pink);letter-spacing:.16em;margin-top:4mm}}
.big-ic{{width:16mm;height:16mm;border-radius:50%;background:var(--mag);display:flex;align-items:center;justify-content:center;margin:0 auto}}
</style>
<div class="content">
 <h1 class="h xl">CONTACT <span class="pink">US</span></h1>
 <div class="pp">
  <div class="pc panel">{lotus}<div class="rl">Chapter Lead</div><div class="nm">Gobinath<br>Maruthalingam</div>
   <div class="ln">{ic("phone","#F7A3CC","4.6mm")} <a href="tel:+918903892943">+91 89038 92943</a></div>
   <div class="ln" style="font-size:8.8pt">{ic("mail","#F7A3CC","4.6mm")} <a href="mailto:gobinath.maruthalingam@gmail.com">gobinath.maruthalingam@gmail.com</a></div></div>
  <div class="pc panel">{lotus}<div class="rl">Corporate Lead</div><div class="nm">Aryan<br>Thakur</div>
   <div class="ln">{ic("phone","#F7A3CC","4.6mm")} <a href="tel:+916377295940">+91 63772 95940</a></div>
   <div class="ln" style="font-size:8.8pt">{ic("users","#F7A3CC","4.6mm")} GDG on Campus IIIT Nagpur</div></div>
 </div>
 <div class="kicker tfk" style="margin-top:14mm"><img src="a/line_l.png"><span>CONNECT WITH GDG ON CAMPUS IIIT NAGPUR</span><img class="r" src="a/line_l.png"></div>
 <div class="so">
  <div class="sc panel"><div class="big-ic">{ic("mail","#fff","8.5mm")}</div><div class="k">EMAIL</div>
   <div class="v" style="font-size:10.5pt;margin-top:5mm"><a href="mailto:gdg@iiitn.ac.in">gdg@iiitn.ac.in</a></div>
   <div style="font:500 8pt 'Poppins';color:#D2CDF2;margin-top:4mm;line-height:1.45">Write to us for partnerships, MoUs and brand assets.</div></div>
  <div class="sc panel"><div class="big-ic">{ic("insta","#fff","8.5mm")}</div><div class="k">INSTAGRAM</div><a href="{IG}"><img class="qr" src="a/qr_insta.png"></a><div class="v"><a href="{IG}">@gdg_iiitn</a></div></div>
  <div class="sc panel"><div class="big-ic">{ic("globe","#fff","8.5mm")}</div><div class="k">COMMUNITY PAGE</div><a href="{GC}"><img class="qr" src="a/qr_gdg.png"></a>
   <div class="v" style="font-size:8pt"><a href="{GC}">gdg.community.dev</a><br><a href="{GC}" style="white-space:nowrap">GDG on Campus IIIT Nagpur</a></div></div>
 </div>
 <div class="panel" style="display:flex;align-items:center;gap:4mm;padding:5.5mm 6mm;margin-top:9mm">{ic("pin","#F7A3CC","9mm")}
  <div><div style="font:400 13pt 'Lilita One';color:#fff">Indian Institute of Information Technology, Nagpur</div>
  <div style="font:500 8.6pt 'Poppins';color:#D8D3F6;margin-top:.6mm">Survey No. 140, 141/1, Waranga, PO Dongargaon (Butibori), Nagpur, Maharashtra 441108</div></div></div>
</div>
'''))

# ---------------- 16 BACK COVER ----------------
pages.append(frame(16, f'''
<style>
.bk{{position:absolute;top:26mm;left:12mm;right:12mm;height:136mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;text-align:center;z-index:10}}
.bk .t{{font:800 16pt 'Poppins';color:#fff;letter-spacing:.04em;line-height:1.35}}
.bk-tag{{font:400 34pt 'Lilita One';color:var(--gold);-webkit-text-stroke:1.5mm var(--mag);paint-order:stroke fill;text-shadow:0 1mm 0 #5D0F3B}}
.bk-row{{display:flex;justify-content:center;align-items:center;gap:7mm}}
.bk-lt{{text-align:center}}
.bk-lt .l1{{font:600 12.5pt 'Outfit';color:#fff;white-space:nowrap}}
.bk-lt .l2{{font:400 7.8pt 'Outfit';color:#D5D2EA;white-space:nowrap;margin-top:.6mm}}
.bk-lt .l2 b{{color:#6FA3FF;font-weight:600}}
.bk-c{{font:600 9.6pt 'Poppins';color:#E9E4FF;letter-spacing:.04em}}
.bk-c a{{border-bottom:.3mm solid rgba(247,163,204,.6)}}
.bk-b{{position:absolute;bottom:2.2mm;left:2.2mm;right:2.2mm;z-index:8}}
.bk-b img{{width:100%;display:block}}
</style>
<div class="bk">
 <img src="a/iiitn.png" style="height:34mm">
 <div class="t">INDIAN INSTITUTE OF INFORMATION<br>TECHNOLOGY, NAGPUR</div>
 <div class="bk-tag">LET'S BUILD IT TOGETHER.</div>
 <div class="bk-row"><img src="a/gdg_logo.png" style="height:12mm"><div class="bk-lt"><div class="l1">Google Developer Groups</div><div class="l2"><b>On Campus</b> · Indian Institute of Information Technology Nagpur</div></div><img src="a/tf_logo26.png" style="height:18mm"></div>
 <div class="bk-c"><a href="mailto:gdg@iiitn.ac.in">gdg@iiitn.ac.in</a> &nbsp;·&nbsp; <a href="tel:+918903892943">+91 89038 92943</a> &nbsp;·&nbsp; <a href="tel:+916377295940">+91 63772 95940</a></div>
</div>
<div class="bk-b"><img src="a/building.png"></div>
''', foot=False))

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' + ''.join(pages) + '</body></html>'
open('brochure.html','w').write(html)
print('pages', len(pages))
