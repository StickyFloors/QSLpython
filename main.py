class Card:
    def __init__(self, callsign, user, year, graphic, colors, continent, country):
        self.callsign = callsign
        self.user = user
        self.year = year
        self.graphic = graphic
        self.colors = colors
        self.continent = continent
        self.country = country

    def __len__(self):
        return(len(self))

    def __repr__(self):
       return(f"In {self.year}, {self.user} with call sign {self.callsign} send KH6EFL a QSL card from {self.country} in {self.continent}.")



oa5g = Card("OA5G","George", "1961", ["ship", "map"],"green","South America", "Peru")
kh6eez = Card("KH6EEZ","Vic","1962","USSR Moscow","blue","Europe","USSR")
vao29048 = Card("VA029048", "Alexander", "1961",["moon", "smile", "sputnik","Soviet"], ["blue", "red"], "Asia", "USSR")
yu3yu = Card("YU3YU", "Ilinko", "1962", "landscape", "orange", "Europe", "Yugoslavia")
lz1i77 = Card("LZ1I77", "Nikola", "1965", "yellow rose", "yellow", "Europe", "Bulgaria")
ok3hm = Card("OK3HM", "Jozo Horsky", "1965","radio", "green", "Europe", "Czechoslovakia")
ok2qr = Card("OK2QR", "Rudolf Staigl", "1962", "bohemian glass", ["blue", "red", "peach"], "Europe", "Czechoslovakia")
dj1ak = Card("DJ1AK", "Richard Hack", "1962", "radio cartoon", "none", "Europe", "Germany")
k5oed = Card("K5OED", "Bob 'Doc' Trotter MD", "1961", ["horse", "carriage"], "orange", "North America", "USA")
kc4usp = Card("KC4USP", "USS Vance DER 387", "1962", ["penguin cartoon", "ship", "military logo"], "blue", "Antarctica", "maritime")
dl3dw = Card("DL3DW", "Rudolph Riedel", "1961", ["painting", "road sign", "woman"], "orange", "Europe", "Germany")
kp4atq = Card("KP4ATQ", "Sam", "1963", "ham shack", "blue", "North America", "USA")
w5egs = Card("W5EGS", "Roger D. Hoestenbach", "1961", "lightning bolts", "gold", "North America", "USA")
k7am = Card("K7AM", "Alvin R. Moore", "1961", ["american continents", "lightning bolts"], ["silver", "red"], "North America", "USA")
w7ads = Card("W7ADS", "Glenn Lay", "1961", "telegraph cartoon", "green", "North America", "USA")
w7bth = Card("W7BTH", "ER Johns", "1961", ["lightning bolts", "globe", "scroll"], ["red", "green"], "North America", "USA")
swlk8 = Card("SWLK8", "John Gerrick", "1965", "personal photo", "blue", "North America", "USA")
wa5cet = Card("WA5CET", "Jack C Holland", "1965", "personal photo", "black", "North America", "USA")
w5va = Card("W5VA", "T Frank Smith", "1962", ["colored boxes", "America outline"], ["red", "black"], "North America", "USA")
k5hrh = Card("K5HRH", "Dwight P Keller", "1961", ["earth orbits", "ARRL"], ["blue", "gold"], "North America", "USA")
kh6ewv = Card("KH6EWV", "Capt RJ Wallenborn USN", "1963", "world map", "blue", "North America", "USA")
kh6elu = Card("KH6ELU", "Jim", "1962", "hawaii map", ["salmon", "blue"], "North America", "USA")
kh6fje = Card("KH6FJE", "Dick Skiles", "1964", "caricature", "blue", "North America", "USA")
kh6ajf = Card("KH6AJF", ["Bob", "Fleet Marine Force Pacific"], "unknown", ["diamond head", "palm"], ["red", "yellow"], "North America", "USA")
kh6egf = Card("KH6EGF", "Cliff D Jones", "1961", "none", "green", "North America", "USA")
kh6eit = Card("KH6EIT", "Makiki Amateur Radio Club", "1963", "Hawaiian house", "black", "North America", "USA")
kh6dyu = Card("KH6DYU", "Walter Sone", "1961", "none", "red", "North America", "USA")
w6dkdmm = Card("W6DKD-MM", ["SS Hong Kong Bear", "Vance F Tara"], "1961", "ship and Fuji", "blue", "North America", "maritime")
w8twj = Card("W8TWJ", "Jerry Blumenthal", "1961", "none", ["black", "silver"], "North America", "Michigan")
kh6euv = Card("KH6EUV", "Maurice H Caldwell Jr", "1963", "none", "black", "North America", "USA")
w4yjl = Card("W4YJL", "Wib Rider", "1963", "world map", ["gold", "red"], "North America", "USA")
w3ach = Card("W3ACH", "Harold L Mercer", "1961", ["world map", "lighting bolts", "shriner"], ["blue", "red", "silver"], "North America", "USA")
w0btq = Card("W0BTQ", "Marshall Alperin MD", "1961", "doctor cartoon", ["silver", "red"], "North America", "USA")
k0yvc = Card("K0YVC", "Gordon N Hagin", "1961", "world map", "yellow", "North America", "USA")
w5drj = Card("W5DRJ", "Curtis N Christian", "1962", ["world map", "lightning bolts"], ["red", "silver"], "North America", "USA")
w1ypk = Card("W1YPK", "CW 'Bill' Bailey", "1961", "none", ["black", "red"], "North America", "USA")
k0oth = Card("K0OTH", "James Clagett", "1961", "none", "red", "North America", "USA")
wa4fqw = Card("WA4FQW", "JG Marty", "1965", "ham antenna", ["black", "red"], "North America", "USA")
wa6tvd = Card("WA6TVD", "George 'The TV Destroyer' McCulley", "1965", "TV Repair cartoon", ["silver", "pink", "blue", "red"], "North America", "USA")
wa0eua = Card("WA0EUA", "Randall Young", "1965", "US Map", "red", "North America", "USA")
w4iwc = Card("W4IWC", "Paul L Snyder", "1961", ["sunburst", "florida map"], ["blue", "yellow"], "North America", "USA")
w4ztj = Card("W4ZTJ", "Jack Zbar", "1961", "moonscape", ["red", "gold", "black"], "North America", "USA")
k4mss = Card("K4MSS", "AL 'Bud' Turner", "1961", "US Map", ["blue", "black"], "North America", "USA")
w2c0t = Card("W2COT", "FB 'Bruce' Parsons", "1961", "black dot", "black", "North America", "USA")
k7kre = Card("K7KRE", "Roy G Loughlin", "1961", "Portland cartoon", ["blue", "red"], "North America", "USA")
wa4hgn = Card("WA4HGN", "Bill Byrd", "1963", ["wilson dam", "heart over the south"], ["blue", "red"], "North America", "USA")
kl7azn = Card("KL7AZN", "Bering Amateur Radio Club", "1961", "alaska cartoon", "black", "North America", "USA")
w51kd = Card("W5IKD", "Jack B Collins", "1962", "US map", ["green", "black"], "North America", "USA")
k5sne = Card("K5SNE", "Burke Brumfield", "1961", "none", "black", "North America", "USA")
w5paa = Card("W5PAA", "FAA Aeronautical Center", "1961", "ARRL logo", ["copper", "black"], "North America", "USA")
k8eop = Card("K8EOP", "Carrol A Wilson", "1961", "world map", ["silver", "blue"], "North America", "USA")
k7awi = Card("K7AWI", "EA 'Pete' Marshall", "1961", "Grand Canyon photo", "multicolor", "North America", "USA")
w7bps = Card("W7BPS", "Jim Oliver", "1961", "Century 21 Exposition logo", ["blue", "green"], "North America", "USA")
ja8gg = Card("JA8GG", "H Yamazaki", "1962", "globe", ["green", "black"], "Asia", "Japan")
zl1wb = Card("ZL1WB", "Bruce", "1961", "border", ["red", "blue"], "Oceania", "New Zealand")
zs6ur = Card("ZS6UR", "W Ruurds", "1961", ["Africa", "lion cartoon"], ["black", "yellow"], "Africa", "South Africa")
sp1age = Card("SP1AGE", "Wiodek", "1962", "reciprocal triangles", "black", "Europe", "Poland")
ja8aa = Card("JA8AA", "Takeo Hama", "1961", "ARRL logo", "green", "Asia", "Japan")
ja3bek = Card("JA3BEK", "Yoshihiro Sano", "1962", "none", ["blue", "red"], "Asia", "Japan")
ja1em = Card("JA1EM", "Yoshihiko Akimoto", "1962", "none", ["black", "red"], "Asia", "Japan")
vk2app = Card("VK2APP", "Peter Page", "1961", ["Wireless Institute of Australia logo", "ram head"], ["green", "black", "red"], "Australia", "Australia")
vk2qj = Card("VK2QJ", "John W Birdsall", "1961", "aboriginee cartoon", "blue", "Australia", "Australia")
ja2aat = Card("JA2AAT", "Soichiro Hayashi", "1962", "none", "black", "Asia", "Japan")
ja1dln = Card("JA1DLN", "Takuya Yoshimoto", "1961", "rounded corners", ["black", "red"], "Asia", "Japan")
ka2ab = Card("KA2AB", "Vernon J Smith", "1961", "none", "black", "Asia", "Japan")
on4nc2 = Card("ON4NC-2", "unknown", "unknown", "St Bavo Cathedral", "yellow", "Europe", "Belgium")
lu2daw = Card("LU2DAW", "Ruben McLaren", "1961", "Argentina map", "blue", "South America", "Argentina")
cx8bm = Card("CX8BM", "Roberto Matho Puig", "1961", "none", ["blue", "red"], "South America", "Uruguay")
tg9ad = Card("TG9AD", "Roberto W Engel", "1961", "ox cart drawing", ["silver", "blue", "red"], "North America", "Guatemala")
fo8ac = Card("FO8AC", "Georges Vincent", "1961", "none", ["red", "black"], "Oceania", ["French Polynesia", "Tahiti"])
ze6ja = Card("ZE6JA", "Maurice D Cleave", "1961", "none", "green", "Africa", "Southern Rhodesia")
vk2axk = Card("VK2AXK", ["John Templeton", "R Gleeson", "Christopher Cole"], "1961", "christian brothers college boys radio club photo", "black", "Australia", "Australia")
kg1fr = Card("KG1FR", "C Fritz", "1961", "none", ["black", "green"], "North America", "Greenland")
kc4usb = Card("KC4USB", "Carl", "1961", "penguin cartoon", "black", "Antarctica", "Antarctica")
vrib = Card("VRIB", "Chas Hawker", "1961", "general electric tube department form 73a", ["black", "pink", "red"], "Oceania", "Tarawa")
on4nc = Card("ON4NC", "Christian J Nolf", "1962", "none", ["blue", "red", "black"], "Europe", "Belgium")
cp5ea = Card("CP5EA", "Hugo Moreno T", "1961", ["hemispheres", "lightning bolts"], ["black", "green", "red"], "South America", "Bolivia")
zl1wb = Card("ZL1WB", "Bruce", "1961", "operator photo", "black", "Oceania", "New Zealand")
xw8as = Card("XW8AS", "Clay", "1962", "elephants", "red", "Asia", "Laos")
et3rs = Card("ET3RS", "MC de Henseler", "1961", "lion cartoon", ["red", "black"], "Africa", "Ethiopia")
ja1gc = Card("JA1GC", "Keiichi 'Ken' Ishizuki", "1962", "port of Yokohama silhouettes", ["black", "red"], "Asia", "Japan")
g3tuf = Card("G3TUF", "Francis A Long", "1965", ["operator cartoon", "sunburst border"], ["black", "yellow", "red"], "Europe", "Great Britain")
wa6kmt = Card("WA6KMT", "Gary", "1961", "seabee logo", "black", "Oceania", "Midway Island")
cr6ca = Card("CR6CA", "Joao de Sacadura Cabral", "1961", "morse code", ["red", "blue"], "Africa", "Angola")
oh2bcz = Card("OH2BCZ", "Erkki Koskinen", "1965", "none", "black", "Europe", "Finland")
zs1ou = Card("ZS1OU", "JP Synman", "1961", ["Africa", "radiowaves"], ["red", "blue"], "Africa", "South Africa")
py2azd = Card("PY2AZD", "Armando Nascimento Jr", "1961", "none", "red", "South America", "Brazil")
vq1dr = Card("VQ1DR", "Dave", "1962", "none", ["green", "yellow"], "Africa", "Zanzibar")
kh6fbj = Card("KH6FBJ", "HC 'Clay' Sherrod Jr", "1963", "hawaiian ham shack", ["blue", "silver"], "North America", "USA")
kh6edy = Card("KH6EDY", "Bob", "1961", "none", ["black", "yellow"], "North America", "USA")
kb6br = Card("KB6BR", "Donald P Stewart", "1961", ["North America", "lightning bolts"], ["silver", "black", "red"], "Oceania", "Kanton Island")
fk8ac = Card("FK8AC", "Felix Franchette", "1961", "none", ["blue", "yellow"], "Oceania", "New Caledonia")
hr2db = Card("HR2DB", "Don Berry", "1961", "plane", "black", "North America", "Honduras")
kh6pd = Card("KH6PD", "Ray Westfall", "1961", "stripes", "black", "Oceania", "Wake Island")
kx6bu = Card("KX6BU", "John", "1961", "palm tree island cartoon", ["yellow", "blue", "red"], "Oceania", "Marshall Islands")
kg4ao = Card("KG4AO", "Dick Lambert", "1961", "none", ["blue", "green"], "North America", "Cuba")
ep2ag = Card("EP2AG", "George H Buchanan", "1961", "none", "black", "Asia", "Iran")
kr6lj = Card("KR6LJ", "Frank A Jerome", "1961", ["torii", "ARRL"], ["black", "red"], "Asia", "Japan")
kj6bv = Card("KJ6BV", "LG Owen", "1961", "none", "none", "Oceania", "Johnston Island")
kl7dne = Card("KL7DNE", "Bill Rohrer", "1961", "none", "black", "North America", "USA")
mp4bbw = Card("MP4BBW", "Ian Cable", "1961", "none", ["black", "red"], "Asia", "Bahrain")
xe1cv = Card("XE1CV", "Carlos de Leon Jr", "1961", "ARRL logo", "orange", "North America", "Mexico")
ve6tf = Card("VE6TF", "Len Tuckey", "1961", "none", ["gold", "red"], "North America", "Canada")
ce8ag = Card("CE8AG", "Roberto Bravo Navarro", "1961", "none", ["blue", "red"], "South America", "Chile")
k6cqv = Card("K6CQV", "Paul Hodges", "1961", "Pago Pago map", "black", "Oceania", "American Somoa")
g4mj = Card("G4MJ", "Ken Basterfield", "1965", "England map", ["green", "blue", "red", "black"], "Europe", "Great Britain")
du7sv = Card("DU7SV", "Voltaire Sotto", "1961", "none", "green", "Asia", "Philippines")
zs6cy = Card("ZS6CY", "Ernie Ormerod", "1961", "ham shack cartoon", ["green", "yellow"], "Africa", "South Africa")
n9m4jy = Card("9M4JY", "N Yatheendran", "1962", "none", "black", "Asia", "Singapore")
wa0nea = Card("WA0NEA", "Raymond G Stellhorn", "1966", "America map", ["black", "red"], "North America", "USA")
zl1ld = Card("ZL1LD", "Patricia Joseph", "1963", "NZART Logo", "black", "Oceania", "New Zealand")
ja2py = Card("JA2PY", "Tatsumi 'Tatsu' Ito", "1965", ["JARL Logo", "sakura blossom"], "blue", "Asia", "Japan")
ref12815 = Card("REF 12.815", "Michel Billard", "1963", ["REF logos", "tricolor corner"], ["green", "blue", "red"], "Europe", "France")
zs1tp = Card("ZS1TP", "Phil Rabie", "1961", ["Table Mountain", "radio tower", "SARL logo"], ["yellow", "blue"], "Africa", "South Africa")
ja21762 = Card("JA2-1762", "Akio Kasahara", "1962", "none", ["red", "blue"], "Asia", "Japan")
ja3yt = Card("JA3YT", "Toshio Yamamuro", "1962", "none", ["black", "green"], "Asia", "Japan")
ua1885 = Card("UA-1-885", "unknown", "1962", "St Isaac Cathedral drawing", ["red", "green"], "Europe", "USSR")
oh2hn = Card("OH2HN", "Altti Unkuri", "1965", "SRAL logo", "silver", "Europe", "Finland")
k9dtz = Card("K9DTZ", "Robert A Jurish", "1961", "atomic logo", ["silver", "black"], "North America", "USA")
w6rh = Card("W6RH", "Ralph M Heintz", "1961", ["eighth scale model train", "cassegrainian telescope", "ham shack drawing"], ["green", "red"], "North America", "USA")
onl383 = Card("ONL383", "Jean-Jacques Yerganian", "1962", "handdrawn", ["pink", "blue"], "Europe", "Belgium")
ha5031 = Card("HA5-031", "Ilan", "1962", "Elektroimpex array", ["orange", "black", "green"], "Europe", "Hungary")
h39fmo = Card("HE9FMO", "Kurt Brauer", "1965", ["USKA logo", "silhouette with globe"], ["black", "red"], "Europe", "Switzerland")
vs1lv = Card("VS1LV", "Bill", "1963", "none", ["black", "red"], "Asia", "Malaysia")
g3fkm = Card("G3FKM", "John Allaway", "1965", "lightning bolts", ["black", "green", "red"], "Europe", "Great Britain")
vs1lv = Card("VS1LV", "Corporal Bill Jones", "1963", "none", ["red", "black"], "Asia", "Malaysia")
ja7mj = Card("JA7MJ", "Makoto Chiba", "1965", "none", "blue", "Asia", "Japan")
kh6eez = Card("KH6EEZ", "Chris Johnson", "1965", "globe with lightning", ["silver", "blue"], "North America", "USA")
kh6efl = Card("KH6EFL", "Charles Johnson", "1961", "none", "copper", "North America", "USA")
sm6aek = Card("SM6AEK", "KG Svenbrant", "1965", "swedish beach", "blue", "Europe", "Sweden")
dl3zi = Card("DL3ZI", "Manfred Staar", "1965", "wife cartoon", "black", "Europe", "Germany")
g6zo = Card("G6ZO", "Jim M Kirk", "1962", "none", "blue", "Europe", "Great Britain")
zl3jc = Card("ZL3JC", "AB Thornton", "1965", "NZART logo", "black", "Oceania", "New Zealand")
z9m2cp = Card("9M2CP", "Phil Zeid", "1965", "tiger", ["red", "yellow"], "Asia", "Malaya")
w8jid = Card("W8JID", "Earl Kleeberger", "unknown", "ham radio photo", "black", "North America", "USA")
dj9gd = Card("DJ9GD", "Walter Misch", "1965", "none", ["black", "red"], "Europe", "Germany")
vk4ck = Card("VK4CK", "LFJ Schnitzerling", "1962", "dotted border", ["lavender", "black"], "Australia", "Australia")
ja2cir = Card("JA2CIR", "Syoju Kamata", "1962", "none", ["red", "pink"], "Asia", "Japan")
vk6ru = Card("VK6RU", "Jim", "1961", "commonwealth games cartoon", ["green", "red", "black", "blue", "yellow", "gold", "gray"], "Australia", "Australia")
oz9u = Card("OZ9U", "Walter Olsen", "1962", "DER logo", ["red", "blue"], "Europe", "Denmark")
ja6xd = Card("JA6XD", "Kazumoto Ishibashi", "1965", "sakura background", ["pink", "blue"], "Asia", "Japan")
zl1fg = Card("ZL1FG", "PD Mulgrew", "1962", "stamp", ["pink", "black"], "Oceania", "New Zealand")
ka2sb = Card("KA2SB", "John A Guyton", "1961", "japan map", ["red", "black"], "Asia", "Japan")
cx2co = Card("CX2CO", "Ricardo Sierra", "1961", "none", ["red", "blue"], "South America", "Uruguay")
onl161 = Card("ONL161", "Marcil Guillaume", "1962", "none", ["green", "blue"], "Europe", "Belgium")
lam4063 = Card("LAM4063", "Terje Steinkjer", "1963", "none", ["red", "black"], "Europe", "Norway")
sm7bvo = Card("SM7BVO", "Rolf Carlson", "1962", "viking ship", ["red", "gray"], "Europe", "Sweden")
vk7sm = Card("VK7SM", "Sam G Moore", "1962", ["decorated border", "Tasmania map"], ["green", "black", "red"], "Australia", "Australia")
ve79981 = Card("VE79981", "Alan T Spencer", "1962", ["RSGB logo", "eagle logo"], "blue", "North America", "Canada")
ve799812 = Card("VE79981", "Alan T Spencer", "1962", "none", "red", "North America", "Canada")
vk3ahj = Card("VK3AHJ", "Ron J Harrison", "1961", "op cartoon", ["black", "yellow"], "Australia", "Australia")
dl9192 = Card("DL9192", "Mathias Munter", "1962", "none", "green", "Europe", "Germany")
ja1fi = Card("JA1FI", "Kiyoshi Naka", "1962", "none", "green", "Asia", "Japan")
ok1zl = Card("OK1ZL", "Zdenek Mensik", "1962", "none", "red", "Europe", "Czechoslovakia")
hm4aq = Card("HM4AQ", "Park Sung Kun", "1961", "wave border", "green", "Asia", "South Korea")
ok2qr2 = Card("OK2QR", "Rudolf Staigl", "1962", "op photo", ["blue", "red"], "Europe", "Czechoslovakia")
kr6ar = Card("KR6AR", "LM Hanson", "1962", "none", "black", "Asia", "Japan")
vk4wo = Card("VK4WO", "Howarde Tilse", "1962", "Brisbane City Hall drawing", ["purple", "green"], "Australia", "Australia")
dj8cb = Card("DJ8CB", "Lothar Kaiser", "1965", ["DARC logo", "Westfalen emblem"], ["green", "yellow"], "Europe", "Germany")
vk2aqu = Card("VK2AQU", "Colonel Harvey", "1961", "C130 Hercules photo", "blue", "Australia", "Australia")
ve4cn = Card("VE4CN", "Cameron Chernecki", "1965", "bloodshot eye", ["red", "black"], "North America", "Canada")
wb6nhf = Card("WB6NHF", "Mark 'Squelch' Nelson", "1965", ["glitter", "globe", "planets"], ["gold", "red"], "North America", "USA")
wa4kxc = Card("WA4KXC", "Steve Corbitt", "1965", "none", "red", "North America", "USA")
kh6fbjkj6 = Card("KH6FBJ-KJ6", "H Clay Cherrod Junior", "1965", "tropical ham shack", "green", "Oceania", "Johnson Island")
k3oks = Card("K3OKS", "Vaughan Simmons", "1964", "lightning sword", ["black", "red", "yellow"], "North America", "USA")

