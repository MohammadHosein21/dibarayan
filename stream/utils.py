import paramiko


def send_config_to_client(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # ssh connect
        client.connect(ip, username=username, password=password, port=22)
        # send config.yaml
        client.exec_command('touch config.yaml')
        client.exec_command(
            f'echo "sender_config:\n  server_ip: "192.168.1.4"\n  server_port: 6379\n  send_rate: 1000\n  celery_task_name: "stream.tasks.process_received_data"" > config.yaml')
        # run mock container
        stdin, stdout, stderr = client.exec_command(
            'docker run --network host -v /home/mmdhosein/config.yaml:/workspace/config.yaml mock')
        print("SSH connection estexitablished successfully!")
        print("Command Output:")
        print(stdout.read().decode())
        client.close()
        return stdout.read()
    except Exception as e:
        print(f"Failed to establish SSH connection: {e}")
    finally:
        client.close()
