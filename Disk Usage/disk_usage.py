import matplotlib.pyplot as plt
import psutil

# Get disk partitions and their usage
partitions = psutil.disk_partitions()
sizes = []
labels = []

# Custom names for partitions (if needed)
custom_names = {
  '/': 'Root',
  '/home': 'Home',
  'swap': 'Swap',
  '/boot': 'Boot',
  '/run/media/mcuser/fcf2d773-e506-40ef-b739-d5584ea6f6a0': 'mmcblk0p1'
}

# Print out the mount points for debugging
print("Detected partitions and their mount points:")
for partition in partitions:
  print(f"Mount point: {partition.mountpoint}")

for partition in partitions:
  # Skip partitions with "loop" in their device name
  if 'loop' in partition.device:
      continue

  usage = psutil.disk_usage(partition.mountpoint)
  sizes.append(usage.total / (1024 ** 3))  # Convert bytes to GB
  # Use custom name if available, otherwise use the mountpoint
  labels.append(custom_names.get(partition.mountpoint, partition.mountpoint))

# Create a donut chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', labeldistance=1.1)
circle = plt.Circle((0, 0), 0.8, color='white')
plt.gca().add_artist(circle)
plt.title('Disk Usage of System Partitions')
plt.show()