import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    width = float(match.group(1))
    if width <= 6.0:
        # Check if it already has >{\raggedright\arraybackslash} before it
        return f">_{{\\raggedright\\arraybackslash}}p{{{match.group(1)}cm}}"
    else:
        return match.group(0)

# But wait, what if it already HAS >{\raggedright\arraybackslash}p{4cm}?
# The regex will match p{4cm} and replace it AGAIN, resulting in:
# >{\raggedright\arraybackslash}>{\raggedright\arraybackslash}p{4cm}

# So let's match specifically p{Xcm} that is NOT immediately preceded by \arraybackslash}
# Or we can just clean it up.

# First, remove all existing >{\raggedright\arraybackslash} to start clean:
content = content.replace('>{\\raggedright\\arraybackslash}', '')

# Now apply it to all p{Xcm} where X <= 6.0
content = re.sub(r'p\{([0-9\.]+)cm\}', replacer, content)

with open('do_an_tot_nghiep.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print('Raggedright applied cleanly to all narrow columns.')
