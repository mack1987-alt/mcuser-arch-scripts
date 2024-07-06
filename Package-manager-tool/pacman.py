import subprocess

class Pacman:
    def __init__(self):
        self.pacman_path = "/usr/bin/pacman"

    def install(self, package_name):
        command = f"{self.pacman_path} -S {package_name}"
        subprocess.run(command, shell=True)

    def remove(self, package_name):
        command = f"{self.pacman_path} -R {package_name}"
        subprocess.run(command, shell=True)

    def update(self):
        command = f"{self.pacman_path} -Syu"
        subprocess.run(command, shell=True)

    def search(self, package_name):
        command = f"{self.pacman_path} -Ss {package_name}"
        result = subprocess.run(command, shell=True, capture_output=True)
        return result.stdout.decode("utf-8")

    def list_installed_packages(self):
        command = f"{self.pacman_path} -Q"
        result = subprocess.run(command, shell=True, capture_output=True)
        return result.stdout.decode("utf-8").split("\n")

if __name__ == "__main__":
    pacman = Pacman()

    # Example usage:
    # Install a package
    # pacman.install("python-requests")

    # Remove a package
    # pacman.remove("python-requests")

    # Update all packages
    pacman.update()

    # Search for a package
    # print(pacman.search("python-requests"))

    # List all installed packages
    # print(pacman.list_installed_packages())