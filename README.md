# FQDN2IP
<img src="/sillypics/FQDN2IP_Meow.png" width="400">

Listen sis, if I catch you manually resolving a mountain of FQDNs one by one, we’re going to have a problem. Your time is important, and staring at a terminal waiting for individual pings is pretty icky. This script takes a raw list of FQDNs, resolves their A records, and exports the results into a fancy little spreadsheet.

TL;DR: Give txt file with FQDNs → get a spreadsheet with resolved IPs → move on with your life.

***

### FQDN2IP Python Dependencies 🐍
- [Python 3.14.64](https://www.python.org/downloads/release/python-3143/)
- [Pandas](https://pandas.pydata.org/)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [DNSPython](https://pypi.org/project/dnspython/)

***

### Installation 💿
1. Clone This Repo:
```git clone https://github.com/Hot-Dad69/FQDN2IP.git```

2. Change Dir:
```cd FQDN2IP```

3. Install Python Dependencies
```python -m pip install pandas openpyxl dnspython```

***

### Usage 👩‍💻
1. Create an input file with all FQDN's, with one domain per line
```fqdns.txt```

2. Run the script
```python fqdn2ip.py fqdns.txt```

3. Results
The script will generate:
```resolvedfqdns.xlsx```

| FQDN | A Records | 
| ------------------------- | ------------------------ | 
| pizza.com | 123.456.0.1 | 
| tacos.biz | 123.456.1.1, 123.456.6.9 | 
| pineappleonpizzaisbad.com | Domain does not exist |

***

## TY 👉👈
If this script saves you from manually resolving 500 domains like a smooth brain, please consider starring this repo! ⭐
