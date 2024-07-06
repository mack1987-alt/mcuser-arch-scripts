import subprocess

class ArchConfig:
    def __init__(self):
        self.arch_config_path = "/etc/arch-config"

    def set_hostname(self, hostname):
        command = f"hostnamectl set-hostname {hostname}"
        subprocess.run(command, shell=True)

    def set_network_interface(self, interface, ip, netmask, gateway):
        network_config = f"""
        [Match]
        Name={interface}

        [Network]
        Address={ip}/{netmask}
        Gateway={gateway}
        """
        with open(f"{self.arch_config_path}/network.conf", "w") as f:
            f.write(network_config)

    def set_firewall_rules(self, rules):
        with open(f"{self.arch_config_path}/firewall.rules", "w") as f:
            f.write("\n".join(rules))

    def set_user_account(self, username, password):
        command = f"useradd -m -p {password} {username}"
        subprocess.run(command, shell=True)

    def apply_changes(self):
        command = "systemctl restart systemd-networkd"
        subprocess.run(command, shell=True)
        command = "systemctl restart firewalld"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    arch_config = ArchConfig()

    # Example usage:
    # Set hostname
    # arch_config.set_hostname("my-arch-machine")

    # Set network interface
    # arch_config.set_network_interface("eth0", "192.168.1.100", "24", "192.168.1.1")

    # Set firewall rules
    # arch_config.set_firewall_rules(["allow 80", "deny 22"])

    # Set user account
    # arch_config.set_user_account("john", "password123")

    # Apply changes
    # arch_config.apply_changes()