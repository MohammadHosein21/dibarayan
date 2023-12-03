import yaml
import json
import subprocess
import paramiko
import docker


def send_config_to_client(ip, username, password, config):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip, username=username, password=password, port=22)
        # command = f"echo '{config}' > /workspace/config.yaml"
        client.exec_command('touch config.yaml')
        # print('suck')
        client.exec_command(
            f'echo "sender_config:\n  server_ip: "192.168.1.4"\n  server_port: 6379\n  send_rate: 1000\n  celery_task_name: "stream.tasks.process_received_data"" > config.yaml')
        # print('suck 2')
        # client.exec_command('docker run -v config.yaml:/home/mmdhosein/config.yaml mock')
        # client.exec_command('')
        stdin, stdout, stderr = client.exec_command(
            'docker run --network host -v /home/mmdhosein/config.yaml:/workspace/config.yaml mock')
        print("SSH connection estexitablished successfully!")
        print("Command Output:")
        print(stdout.read().decode())

        # Check for any errors
        if stderr.read():
            print("Command Error:")
            print(stderr.read().decode())
        return stdout.read()
    except Exception as e:
        print(f"Failed to establish SSH connection: {e}")
    finally:
        client.close()


def run_docker_container(client_ip, username, password):
    # client = docker.DockerClient(base_url=f"ssh://{username}:{password}@{client_ip}")
    client = docker.DockerClient(base_url=f"ssh -l {username} -p 22 {client_ip}")
    try:
        container = client.containers.run(
            'mock',
            command='docker run -it mock',
            volumes={'/workspace/config.yaml': {'bind': '/workspace/config.yaml', 'mode': 'rw'}},
            detach=True
        )
        return container.logs().decode('utf-8')
    except Exception as e:
        return str(e)
