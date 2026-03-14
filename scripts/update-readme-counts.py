#!/usr/bin/env python3
import subprocess, json, sys

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

readme = f"""# BEUP Space

[![BEUP Products](https://img.shields.io/badge/BEUP_Products-{p}_repos-4A90D9?style=for-the-badge)](https://github.com/search?q=org%3Abeupspace-tool+topic%3Abeup-product&type=repositories)
[![BEUP Ops](https://img.shields.io/badge/BEUP_Ops-{o}_repos-2ECC71?style=for-the-badge)](https://github.com/search?q=org%3Abeupspace-tool+topic%3Abeup-ops&type=repositories)
[![Client Work](https://img.shields.io/badge/Client_Work-{c}_repos-E67E22?style=for-the-badge)](https://github.com/search?q=org%3Abeupspace-tool+topic%3Aclient-work&type=repositories)
[![Fork Reference](https://img.shields.io/badge/Fork_Reference-{f}_repos-9B59B6?style=for-the-badge)](https://github.com/search?q=org%3Abeupspace-tool+topic%3Afork-reference&type=repositories)

---

| Category | Description |
|---|---|
| **BEUP Products** | Commercial tools & apps built for BEUP platform |
| **BEUP Ops** | Internal workspace, Claude config, operational tooling |
| **Client Work** | Consulting & client-specific projects |
| **Fork Reference** | External repos forked for reference or customization |
"""

with open('profile/README.md', 'w') as fh:
    fh.write(readme)
print(f"Updated: product={p} ops={o} client={c} fork={f}")
