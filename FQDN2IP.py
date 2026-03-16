import dns.resolver
import pandas as pd

#   Hot-Dad69 / FQDN2IP
#   A lazy script that uses Python packages to convert a text file of FQDNs and converts them into a resolved XLSX format.
#   Modules req: Python 3.14, Pandas, openpyxl & dnspython
#   python -m pip install pandas openpyxl dnspython

def resolve_fqdn(fqdn):
    try:
        # Query for A records
        answers = dns.resolver.resolve(fqdn, 'A')
        # Collect IP addresses
        a_records = [rdata.address for rdata in answers]
        return ', '.join(a_records)  # Return a comma-separated string of IPs
    except dns.resolver.NoAnswer:
        return 'No A record found'
    except dns.resolver.NXDOMAIN:
        return 'Domain does not exist'
    except Exception as e:
        return str(e)

def read_fqdns_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_results_to_excel(results, output_filename):
    df = pd.DataFrame(results, columns=['FQDN', 'A Records'])
    df.to_excel(output_filename, index=False, engine='openpyxl')

def main():
    input_file =  (r"C:path\fqdns.txt") # replace with your input txt file
    output_file = (r"C:path\resolvedfqdn.xlsx") # replace with your desired name for Excel
    
    fqdns = read_fqdns_from_file(input_file)
    results = []
    
    for fqdn in fqdns:
        a_records = resolve_fqdn(fqdn)
        results.append({'FQDN': fqdn, 'A Records': a_records})
    
    write_results_to_excel(results, output_file)
    print(f'Results have been written to {output_file}')

if __name__ == '__main__':
    main()
