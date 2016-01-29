#README

---

This app demonstrates the Fedora add datastream and purge datastream API calls. It assumes you're working with [Islandora Vagrant](https://github.com/Islandora-Labs/islandora_vagrant)

#### Examples

**Purge a TN Datastream**

python3 datastreameditor.py -p test:56 -d TN -r purge

**Add a TN Datastream**

python3 datastreameditor.py -p test:56 -d TN -r add
