import re

# STOPWORDS in sections
NON_MEENING = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "corp", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na",
               "name", "company", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "kingdom", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz", ]
COUNTRIES = ['afghanistan', 'aland islands', 'albania', 'algeria', 'american samoa', 'andorra', 'angola', 'anguilla', 'antarctica', 'antigua and barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda', 'bhutan', 'bolivia, plurinational state of', 'bonaire, sint eustatius and saba', 'bosnia and herzegovina', 'botswana', 'bouvet island', 'brazil', 'british indian ocean territory', 'brunei darussalam', 'bulgaria', 'burkina faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'cayman islands', 'central african republic', 'chad', 'chile', 'china', 'christmas island', 'cocos (keeling) islands', 'colombia', 'comoros', 'congo', 'congo, the democratic republic of the', 'cook islands', 'costa rica', "c�te d'ivoire", 'croatia', 'cuba', 'cura�ao', 'cyprus', 'czech republic', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'ethiopia', 'falkland islands (malvinas)', 'faroe islands', 'fiji', 'finland', 'france', 'french guiana', 'french polynesia', 'french southern territories', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe', 'guam', 'guatemala', 'guernsey', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'heard island and mcdonald islands', 'holy see (vatican city state)', 'honduras', 'hong kong', 'hungary', 'iceland', 'india', 'indonesia', 'iran, islamic republic of', 'iraq', 'ireland', 'isle of man', 'israel', 'italy', 'jamaica', 'japan', 'jersey', 'jordan', 'kazakhstan', 'kenya', 'kiribati', "korea, democratic people's republic of", 'korea, republic of', 'kuwait', 'kyrgyzstan', "lao people's democratic republic", 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg',
             'macao', 'macedonia, republic of', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'martinique', 'mauritania', 'mauritius', 'mayotte', 'mexico', 'micronesia, federated states of', 'moldova, republic of', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nauru', 'nepal', 'netherlands', 'new caledonia', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'niue', 'norfolk island', 'northern mariana islands', 'norway', 'oman', 'pakistan', 'palau', 'palestinian territory, occupied', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'pitcairn', 'poland', 'portugal', 'puerto rico', 'qatar', 'r�union', 'romania', 'russian federation', 'rwanda', 'saint barth�lemy', 'saint helena, ascension and tristan da cunha', 'saint kitts and nevis', 'saint lucia', 'saint martin (french part)', 'saint pierre and miquelon', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'sint maarten (dutch part)', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south georgia and the south sandwich islands', 'spain', 'sri lanka', 'sudan', 'suriname', 'south sudan', 'svalbard and jan mayen', 'swaziland', 'sweden', 'switzerland', 'syrian arab republic', 'taiwan, province of china', 'tajikistan', 'tanzania, united republic of', 'thailand', 'timor-leste', 'togo', 'tokelau', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'turks and caicos islands', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states', 'united states minor outlying islands', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela, bolivarian republic of', 'viet nam', 'virgin islands, british', 'virgin islands, u.s.', 'wallis and futuna', 'yemen', 'zambia', 'zimbabwe']
CONTINENTS = ['africa', 'asia', 'europe', 'north america',
              'south america', 'america', 'australia', 'asiapacific']
CARDINAL = ['north', 'east', 'south', 'west']

USA_STATES = ["alaska", "alabama", "arkansas", "american samoa", "arizona", "california", "colorado", "connecticut", "district ", "of columbia", "delaware", "florida", "georgia", "guam", "hawaii", "iowa", "idaho", "illinois", "indiana", "kansas", "kentucky", "louisiana", "massachusetts", "maryland", "maine", "michigan", "minnesota", "missouri", "mississippi",
              "montana", "north carolina", "north dakota", "nebraska", "new hampshire", "new jersey", "new mexico", "nevada", "new york", "ohio", "oklahoma", "oregon", "pennsylvania", "puerto rico", "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "virginia", "virgin islands", "vermont", "washington", "wisconsin", "west virginia", "wyoming"]

USA_CITIES = ["aberdeen", "abilene", "akron", "albany", "albuquerque", "alexandria", "allentown", "amarillo", "anaheim", "anchorage", "ann arbor", "antioch", "apple valley", "appleton", "arlington", "arvada", "asheville", "athens", "atlanta", "atlantic city", "augusta", "aurora", "austin", "bakersfield", "baltimore", "barnstable", "baton rouge", "beaumont", "bel air", "bellevue", "berkeley", "bethlehem", "billings", "birmingham", "bloomington", "boise", "boise city", "bonita springs", "boston", "boulder", "bradenton", "bremerton", "bridgeport", "brighton", "brownsville", "bryan", "buffalo", "burbank", "burlington", "cambridge", "canton", "cape coral", "carrollton", "cary", "cathedral city", "cedar rapids", "champaign", "chandler", "charleston", "charlotte", "chattanooga", "chesapeake", "chicago", "chula vista", "cincinnati", "clarke county", "clarksville", "clearwater", "cleveland", "college station", "colorado springs", "columbia", "columbus", "concord", "coral springs", "corona", "corpus christi", "costa mesa", "dallas", "daly city", "danbury", "davenport", "davidson county", "dayton", "daytona beach", "deltona", "denton", "denver", "des moines", "detroit", "downey", "duluth", "durham", "el monte", "el paso", "elizabeth", "elk grove", "elkhart", "erie", "escondido", "eugene", "evansville", "fairfield", "fargo", "fayetteville", "fitchburg", "flint", "fontana", "fort collins", "fort lauderdale", "fort smith", "fort walton beach", "fort wayne", "fort worth", "frederick", "fremont", "fresno", "fullerton", "gainesville", "garden grove", "garland", "gastonia", "gilbert", "glendale", "grand prairie", "grand rapids", "grayslake", "green bay", "greenbay", "greensboro", "greenville", "gulfport-biloxi", "hagerstown", "hampton", "harlingen", "harrisburg", "hartford", "havre de grace", "hayward", "hemet", "henderson", "hesperia", "hialeah", "hickory", "high point", "hollywood", "honolulu", "houma", "houston", "howell", "huntington", "huntington beach", "huntsville", "independence", "indianapolis", "inglewood", "irvine", "irving", "jackson", "jacksonville", "jefferson", "jersey city", "johnson city", "joliet", "kailua", "kalamazoo", "kaneohe", "kansas city", "kennewick", "kenosha", "killeen", "kissimmee", "knoxville", "lacey", "lafayette", "lake charles", "lakeland", "lakewood", "lancaster", "lansing", "laredo", "las cruces", "las vegas", "layton", "leominster", "lewisville", "lexington", "lincoln", "little rock", "long beach", "lorain", "los angeles",
              "louisville", "lowell", "lubbock", "macon", "madison", "manchester", "marina", "marysville", "mcallen", "mchenry", "medford", "melbourne", "memphis", "merced", "mesa", "mesquite", "miami", "milwaukee", "minneapolis", "miramar", "mission viejo", "mobile", "modesto", "monroe", "monterey", "montgomery", "moreno valley", "murfreesboro", "murrieta", "muskegon", "myrtle beach", "naperville", "naples", "nashua", "nashville", "new bedford", "new haven", "new london", "new orleans", "new york", "new york city", "newark", "newburgh", "newport news", "norfolk", "normal", "norman", "north charleston", "north las vegas", "north port", "norwalk", "norwich", "oakland", "ocala", "oceanside", "odessa", "ogden", "oklahoma city", "olathe", "olympia", "omaha", "ontario", "orange", "orem", "orlando", "overland park", "oxnard", "palm bay", "palm springs", "palmdale", "panama city", "pasadena", "paterson", "pembroke pines", "pensacola", "peoria", "philadelphia", "phoenix", "pittsburgh", "plano", "pomona", "pompano beach", "port arthur", "port orange", "port saint lucie", "port st. lucie", "portland", "portsmouth", "poughkeepsie", "providence", "provo", "pueblo", "punta gorda", "racine", "raleigh", "rancho cucamonga", "reading", "redding", "reno", "richland", "richmond", "richmond county", "riverside", "roanoke", "rochester", "rockford", "roseville", "round lake beach", "sacramento", "saginaw", "saint louis", "saint paul", "saint petersburg", "salem", "salinas", "salt lake city", "san antonio", "san bernardino", "san buenaventura", "san diego", "san francisco", "san jose", "santa ana", "santa barbara", "santa clara", "santa clarita", "santa cruz", "santa maria", "santa rosa", "sarasota", "savannah", "scottsdale", "scranton", "seaside", "seattle", "sebastian", "shreveport", "simi valley", "sioux city", "sioux falls", "south bend", "south lyon", "spartanburg", "spokane", "springdale", "springfield", "st. louis", "st. paul", "st. petersburg", "stamford", "sterling heights", "stockton", "sunnyvale", "syracuse", "tacoma", "tallahassee", "tampa", "temecula", "tempe", "thornton", "thousand oaks", "toledo", "topeka", "torrance", "trenton", "tucson", "tulsa", "tuscaloosa", "tyler", "utica", "vallejo", "vancouver", "vero beach", "victorville", "virginia beach", "visalia", "waco", "warren", "washington", "waterbury", "waterloo", "west covina", "west valley city", "westminster", "wichita", "wilmington", "winston", "winter haven", "worcester", "yakima", "yonkers", "york", "youngstown"]
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']

STOPWORDS = NON_MEENING + COUNTRIES + CONTINENTS + \
    CARDINAL + MONTHS + USA_STATES + USA_CITIES


def find_in_text(word, text):
    list = text.lower().strip().split()
    return word.lower() in list  # in [w.lower() for w in list]


def only_letters(text, exception=""):
    regex = re.compile(f'[^a-zA-Z{exception} " "]')
    return regex.sub('', text)
