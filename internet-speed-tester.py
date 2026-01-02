import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()

    print("Testing speed...")

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    st.get_best_server()
    ping = st.results.ping

    return{
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
    }

speed = check_internet_speed()

print(f"Download Speed: {speed['download']} Mbps")
print(f"Upload Speed: {speed['upload']} Mbps")
print(f"Ping: {speed['ping']} ms")