`Risheyab`

## Created by Lord_SMH

This project is a comprehensive subdomain finder tool designed to discover subdomains of a given domain using multiple methods. The tool leverages several powerful libraries and techniques to ensure a thorough search and validation of subdomains.

### Features
- **Brute-force Search**: Enable brute-force search with Sublist3r.
- **DNSRecon Search**: Use DNSRecon to find additional subdomains.
- **MassDNS Validation**: Validate discovered subdomains using MassDNS.
- **Flexible Output**: Save valid subdomains to a specified output file or print them directly to the console.

### Strengths
- **Multiple Search Methods**: Combines various techniques for a comprehensive search.
- **Efficient and Fast**: Utilizes multithreading and efficient libraries to ensure quick results.
- **Customizable**: Users can choose different search options based on their needs.
- **Easy to Use**: Simple command-line interface with clear options and help documentation.

### Prerequisites
Before running this tool, ensure you have the following dependencies installed:
- Python 3.x
- `sublist3r` library
- `pyfiglet` library
- `dnsrecon` tool
- `massdns` tool

- you need edit part of code about <resolvers.txt location> replace your username on the code !! line 38 , 47 

You can install the required Python libraries using:
```bash
pip install sublist3r pyfiglet
```
Make sure `dnsrecon` and `massdns` are installed and accessible from your command line.

### Usage
To use this subdomain finder tool, run the `risheyab.py` script with the appropriate options:

```bash
python risheyab.py [OPTIONS] domain
```

#### Options:
- `-d   --domain`       The domain to search for subdomains
- `-b,  --bruteforce`:  Enable brute-force search with Sublist3r.
- `-dr, --dnsrecon`:    Enable DNSRecon search.
- `-o,  --output FILE`: Output file to save valid subdomains.

#### Examples:
- Simple subdomain search:
  ```bash
  python risheyab.py -d example.com
  ```

- Enable brute-force search:
  ```bash
  python risheyab.py -b example.com
  ```

- Enable DNSRecon search:
  ```bash
  python risheyab.py -dr example.com
  ```

- Save results to a file:
  ```bash
  python risheyab.py -o subdomains.txt example.com
  ```
## Help
For detailed help, refer to the [help](https://github.com/lordsmh/risheyab-/blob/main/help.txt) file included with the project.

## Author
Tool developed by `lord_smh`.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy using risheyab!

