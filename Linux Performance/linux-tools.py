# Version 1.98
import psutil
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

class LinuxPerformanceWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Linux Performance Observability Tools")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        # Filesystem
        filesystem_label = QLabel("Filesystem:")
        filesystem_text = QTextEdit()
        filesystem_text.setReadOnly(True)
        filesystem_text.setText(self.get_filesystem_info())
        layout.addWidget(filesystem_label)
        layout.addWidget(filesystem_text)

        # Volume Manager
        volume_manager_label = QLabel("Volume Manager:")
        volume_manager_text = QTextEdit()
        volume_manager_text.setReadOnly(True)
        volume_manager_text.setText(self.get_volume_manager_info())
        layout.addWidget(volume_manager_label)
        layout.addWidget(volume_manager_text)

        # Block Device
        block_device_label = QLabel("Block Device:")
        block_device_text = QTextEdit()
        block_device_text.setReadOnly(True)
        block_device_text.setText(self.get_block_device_info())
        layout.addWidget(block_device_label)
        layout.addWidget(block_device_text)

        # Net Device
        net_device_label = QLabel("Net Device:")
        net_device_text = QTextEdit()
        net_device_text.setReadOnly(True)
        net_device_text.setText(self.get_net_device_info())
        layout.addWidget(net_device_label)
        layout.addWidget(net_device_text)

        # IP
        ip_label = QLabel("IP:")
        ip_text = QTextEdit()
        ip_text.setReadOnly(True)
        ip_text.setText(self.get_ip_info())
        layout.addWidget(ip_label)
        layout.addWidget(ip_text)

        # Sockets
        sockets_label = QLabel("Sockets:")
        sockets_text = QTextEdit()
        sockets_text.setReadOnly(True)
        sockets_text.setText(self.get_sockets_info())
        layout.addWidget(sockets_label)
        layout.addWidget(sockets_text)

        # System Libraries
        system_libraries_label = QLabel("System Libraries:")
        system_libraries_text = QTextEdit()
        system_libraries_text.setReadOnly(True)
        system_libraries_text.setText(self.get_system_libraries_info())
        layout.addWidget(system_libraries_label)
        layout.addWidget(system_libraries_text)

        # Applications
        applications_label = QLabel("Applications:")
        applications_text = QTextEdit()
        applications_text.setReadOnly(True)
        applications_text.setText(self.get_applications_info())
        layout.addWidget(applications_label)
        layout.addWidget(applications_text)

        # Memory
        memory_label = QLabel("Memory:")
        memory_text = QTextEdit()
        memory_text.setReadOnly(True)
        memory_text.setText(self.get_memory_info())
        layout.addWidget(memory_label)
        layout.addWidget(memory_text)

        # Scheduler
        scheduler_label = QLabel("Scheduler:")
        scheduler_text = QTextEdit()
        scheduler_text.setReadOnly(True)
        scheduler_text.setText(self.get_scheduler_info())
        layout.addWidget(scheduler_label)
        layout.addWidget(scheduler_text)

        self.setLayout(layout)

    def get_filesystem_info(self):
        return subprocess.check_output(["df", "-h"]).decode("utf-8")

    def get_volume_manager_info(self):
        try:
            output = subprocess.check_output(["lvs", "--rows", "--units", "h"])
            return output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

    def get_block_device_info(self):
        return subprocess.check_output(["lsblk", "-d", "-o", "NAME,FSTYPE,MOUNTPOINT,SIZE"]).decode("utf-8")

    def get_net_device_info(self):
        return subprocess.check_output(["ip", "link", "show"]).decode("utf-8")

    def get_ip_info(self):
        return subprocess.check_output(["ip", "addr", "show"]).decode("utf-8")

    def get_sockets_info(self):
        return subprocess.check_output(["ss", "-tulpn"]).decode("utf-8")

    def get_system_libraries_info(self):
        return subprocess.check_output(["ldconfig", "-p"]).decode("utf-8")

    def get_applications_info(self):
        return subprocess.check_output(["ps", "-ef"]).decode("utf-8")

    def get_memory_info(self):
        return subprocess.check_output(["free", "-h"]).decode("utf-8")

    def get_scheduler_info(self):
        return subprocess.check_output(["ps", "-eo", "pid,ppid,priority,nice,rtprio,sched,cmd"]).decode("utf-8")

if __name__ == "__main__":
    app = QApplication([])
    window = LinuxPerformanceWindow()
    window.show()
    app.exec_()
