# Objective of this class is to include all rpc specific to juniper operation
# commands. Like(Show version, sh interface terse, sh bgp Summary)
# later this module can be used as a helper class for other highend tasks

from ncclient import manager as nc

class ncfrpc:

    def __init__(self,ip,username,password,po_ncf):
        self.host = ip
        self.uname = username
        self.passwd = password
        self.nport = po_ncf


    def get_interface(self):
        filter = '<get-interface-information><terse/></get-interface-information>'
        try:
            with nc.connect(host=self.host, username=self.uname, password=self.passwd, port=self.nport, hostkey_verify=False, device_params={'name':'junos'}) as jp:
                data = jp.rpc(filter)
                interfaces = data.xpath('//physical-interface/name')
                interfaces_status = data.xpath('//physical-interface/oper-status')
                for interface, interface_status in zip(interfaces,interfaces_status):
                    intf = interface.text.split('\n')[1]
                    intf_status = interface_status.text.split('\n')[1]
                    print(f"Interface: {intf:10}, Status: {intf_status.upper():10}")
        except Exception as e:
            print(f"Exception occured as {e}")

    def get_version(self):
        filter = '<get-software-information></get-software-information>'
        try:
            with nc.connect(host=self.host, username=self.uname, password=self.passwd, port=self.nport, hostkey_verify=False, device_params={'name':'junos'}) as jp:
                data = jp.rpc(filter)
                sv = data.xpath('software-information/junos-version')
                netElm = data.xpath('software-information/host-name')
                for data1, data2 in zip(sv, netElm):
                    print(f"\n\nDevice: {data2.text}, Software Version: {data1.text}\n\n")
        except Exception as e:
            print(f"Exception occured as {e}")
