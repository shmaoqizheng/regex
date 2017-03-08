import re
def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    matches = []
    for word in words:
        regex = r"v"
 	    if re.search(regex,word):
 		    matches.append(word)
        regex = r"(ss)"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"e$"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"b\wb"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"b\w+b"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"b\w*b"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"[Aa]\w+[eE]\w+[Ii]\w+[Oo]\w+[Uu]"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"[regular expression]*"
        if re.search(regex,word):
 		    matches.append(word)
        regex = r"(\w\w)"
        if re.search(regex,word):
 		    matches.append(word)
    return matches
