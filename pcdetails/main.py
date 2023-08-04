import psycopg2
import psutil

conn = psycopg2.connect(host= "localhost", dbname= "postgres", user="postgres", password= "admin")
cur = conn.cursor()

while True:
    cpu_usage = psutil.cpu_percent(interval=1)

    mem_info = psutil.virtual_memory()
    mem_percentage = mem_info.percent

    disk_info = psutil.disk_usage('/')
    disk_percentage = disk_info.percent

    connections = psutil.net_connections()

    cur.execute("INSERT INTO pcdetails (cpu,ram,disk,connections) VALUES (" + str(cpu_usage) + "," + str(
        mem_percentage) + "," + str(disk_percentage) + "," + str(len(connections)) + ")")
    conn.commit()