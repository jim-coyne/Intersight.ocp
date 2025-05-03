from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
vlan_template = env.get_template('1_vlanpolicy.j2')
port_template = env.get_template('2_portpolicy.j2')
switchpolicies_template = env.get_template('3_switchpolicies.j2')
domainprofile_template = env.get_template('4_domain_profile.j2')


prefix = 'prefix.'
organization = 'default'

vlan_range = range(70, 71)  
port_ids = range(1, 17)     
slot_id = 1 


ntpserver1 = '172.20.10.10'
ntpserver2 = '172.20.10.11'
timezone = 'America/New_York'
dns1 = '172.20.10.60'
dns2 = '172.20.10.59'
snmp_community_access = 'Disabled'
domain = 'domain'

snmp = {
    'CommunityAccess': snmp_community_access
}

with open('1_vlanpolicy.yaml', 'w') as vlan_output_file:
    for vlan in vlan_range:
        vlan_output = vlan_template.render(
            prefix=prefix,
            organization=organization,
            vlan=vlan,
            isNative='false'  
        )
        vlan_output_file.write(vlan_output + '\n')

with open('2_portpolicy.yaml', 'w') as port_output_file:
    for port_id in port_ids:
        port_output = port_template.render(
            prefix=prefix,
            organization=organization,
            port_id=port_id,
            slot_id=slot_id
        )
        port_output_file.write(port_output + '\n')

with open('3_switchpolicies.yaml', 'w') as switchpolicies_output_file:
    switchpolicies_output = switchpolicies_template.render(
        prefix=prefix,
        organization=organization,
        ntpserver1=ntpserver1,
        ntpserver2=ntpserver2,
        timezone=timezone,
        dns1=dns1,
        dns2=dns2,
        snmp=snmp  
    )
    switchpolicies_output_file.write(switchpolicies_output + '\n')

with open('4_domain_profile.yaml', 'w') as domainprofile_output_file:
    domainprofile_output = domainprofile_template.render(
        prefix=prefix,
        organization=organization,
        domain=domain
    )
    domainprofile_output_file.write(domainprofile_output + '\n')

print("Files '1_vlanpolicy.yaml', '2_portpolicy.yaml', '3_switchpolicies.yaml', and '4_domain_profile.yaml' have been overwritten with the rendered content.")
