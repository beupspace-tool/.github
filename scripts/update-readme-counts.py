#!/usr/bin/env python3
# Updates only badge counts in profile/README.md, preserving all other content.
import subprocess, json, re

def count_topic(topic):
    r = subprocess.run(
        ['gh', 'repo', 'list', 'beupspace-tool', '--limit', '100', '--topic', topic, '--json', 'name'],
        capture_output=True, text=True
    )
    return len(json.loads(r.stdout))

p = count_topic('beup-product')
o = count_topic('beup-ops')
c = count_topic('client-work')
f = count_topic('fork-reference')

with open('profile/README.md', 'r') as fh:
    content = fh.read()

# Replace only the numbers inside badge URLs — leave everything else untouched
content = re.sub(r'(BEUP_Products-)\d+(_repos)', rf'\g<1>{p}\2', content)
content = re.sub(r'(BEUP_Ops-)\d+(_repos)', rf'\g<1>{o}\2', content)
content = re.sub(r'(Client_Work-)\d+(_repos)', rf'\g<1>{c}\2', content)
content = re.sub(r'(Fork_Reference-)\d+(_repos)', rf'\g<1>{f}\2', content)

with open('profile/README.md', 'w') as fh:
    fh.write(content)

print(f"Updated: product={p} ops={o} client={c} fork={f}")
