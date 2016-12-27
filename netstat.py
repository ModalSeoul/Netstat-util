import requests


class IPInfo:
    """This shouldn't  be a class.
    Expanding upon it will happen... eventually"""

    def req_ip(self, ip):
        r = requests.get('http://ipinfo.io/%s' % ip)
        return r.json()

    def req_ip_list(self, ips):
        ip_info_list = []
        for ip in ips:
            r = self.req_ip(ip)
            ip_info_list.append(r.json())
        return ip_info_list

    def save_output(self, information, file_name):
        with open(file_name, 'w') as outfile:
            outfile.write(str(information))


def analyze_netstat(file_name):
    with open(file_name) as infile:
        log = infile.readlines()
        for ip in log:
            print(ip)


Info = IPInfo()
dns = Info.req_ip('8.8.8.8')
Info.save_output(dns, 'dns.txt')
analyze_netstat('log.txt')
